---
tags:
  - 部署
  - 运维
  - Docker
  - FastAPI
  - React
  - M11
  - AI方案撰写
status: 已细化
related:
  - "[[O、数据合规与隐私保护]]"
  - "[[R、安全与权限设计]]"
  - "[[M、成本估算与预算]]"
---

# P. 部署与运维方案

> 本文档记录 M11 方案生成 Copilot 的部署架构、Docker Compose 配置、CI/CD、监控和备份策略。
> 定稿日期：2026-08-20

---

## 1. 部署架构

```
                    ┌─────────────┐
                    │   Nginx     │
                    │ 反向代理/SSL │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │   React     │ │  FastAPI    │ │   Worker    │
    │   Frontend  │ │   Backend   │ │   Process   │
    └─────────────┘ └──────┬──────┘ └──────┬──────┘
                           │               │
                           ▼               ▼
                    ┌─────────────┐ ┌─────────────┐
                    │   MySQL 8   │ │   MinIO     │
                    │  tasks/jobs │ │  文件存储    │
                    │  metadata   │ │  方案文档    │
                    │  llm_calls  │ │             │
                    └─────────────┘ └─────────────┘
```

### 1.1 服务说明

| 服务 | 技术 | 职责 |
|---|---|---|
| Frontend | React + Vite + Nginx | 静态资源、门户嵌入 |
| Backend | FastAPI + Gunicorn/Uvicorn | API、任务管理、SSE |
| Worker | Python 独立进程 | 竞争消费 jobs 表 |
| MySQL | 8.0 | 任务、元数据、日志 |
| MinIO | 对象存储 | 上传文件、生成 Word |
| Nginx | 反向代理 | SSL、路由、静态文件 |

---

## 2. Docker Compose 配置

```yaml
version: "3.8"

services:
  mysql:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
    volumes:
      - mysql_data:/var/lib/mysql
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped
    networks:
      - backend

  minio:
    image: minio/minio
    command: server /data --console-address ":9001"
    environment:
      MINIO_ROOT_USER: ${MINIO_ROOT_USER}
      MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD}
    volumes:
      - minio_data:/data
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped
    networks:
      - backend

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - MINIO_ENDPOINT=${MINIO_ENDPOINT}
      - MINIO_ACCESS_KEY=${MINIO_ACCESS_KEY}
      - MINIO_SECRET_KEY=${MINIO_SECRET_KEY}
      - LLM_API_KEY=${LLM_API_KEY}
      - JWT_SECRET=${JWT_SECRET}
    depends_on:
      mysql:
        condition: service_healthy
      minio:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    restart: unless-stopped
    networks:
      - backend

  worker:
    build:
      context: ./backend
      dockerfile: Dockerfile
    command: python -m scripts.run_worker
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - MINIO_ENDPOINT=${MINIO_ENDPOINT}
      - MINIO_ACCESS_KEY=${MINIO_ACCESS_KEY}
      - MINIO_SECRET_KEY=${MINIO_SECRET_KEY}
      - LLM_API_KEY=${LLM_API_KEY}
    depends_on:
      - mysql
      - minio
    restart: unless-stopped
    deploy:
      replicas: 2
    networks:
      - backend

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    depends_on:
      - backend
    restart: unless-stopped
    networks:
      - frontend
      - backend

  nginx:
    image: nginx:1.27-alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/ssl:/etc/nginx/ssl:ro
    depends_on:
      - frontend
      - backend
    restart: unless-stopped
    networks:
      - frontend
      - backend

volumes:
  mysql_data:
  minio_data:

networks:
  frontend:
  backend:
    internal: true
```

---

## 3. 环境规划

| 环境 | 用途 | 部署方式 |
|---|---|---|
| **本地开发** | 工程师本地调试 | `docker-compose up`，源码挂载 |
| **测试环境** | 功能测试、集成测试 | 单机 Docker Compose |
| **预发布** | 医学专家试用 | 独立服务器 |
| **生产** | 真实项目使用 | Docker Compose 或 K8s |

### 阶段一目标

本地开发 + 测试环境能跑通即可，预发布环境视情况搭建。

---

## 4. CI/CD 流水线

| 阶段 | 工具 | 动作 |
|---|---|---|
| **代码提交** | GitHub/GitLab | 触发 CI |
| **Lint/Format** | ruff, mypy, prettier | 代码检查 |
| **单元测试** | pytest, vitest | 运行测试 |
| **构建镜像** | Docker | 构建 backend/frontend 镜像 |
| **安全扫描** | Trivy | 扫描镜像漏洞 |
| **部署测试环境** | docker-compose | 自动更新测试环境 |
| **回归测试** | pytest | 跑黄金样本集 |
| **部署预发布/生产** | 人工审批 | 蓝绿或滚动更新 |

### 关键触发

| 变更 | 触发动作 |
|---|---|
| backend 代码 | 重新构建 backend + worker 镜像 |
| frontend 代码 | 重新构建 frontend 镜像 |
| Skill YAML | 触发回归测试，但不自动升级生产版本 |
| Alembic 迁移 | 自动执行 `alembic upgrade head` |

---

## 5. 监控与可观测性

### 5.1 LLM 可观测性

2026 年推荐 **Langfuse** 作为开源 LLM 可观测性平台：

| 工具 | 用途 | 部署方式 |
|---|---|---|
| **Langfuse** | LLM trace、prompt 版本、eval、cost | 自托管 |
| **Prometheus** | 指标采集 | Docker |
| **Grafana** | 可视化看板 | Docker |
| **Loki** | 日志聚合 | Docker |
| **Alertmanager** | 告警 | Docker |

### 5.2 监控指标

| 指标 | 说明 |
|---|---|
| LLM 调用延迟 | 按模型/章节分位值 |
| LLM 调用成本 | 每日/每周累计 |
| 任务成功率 | 解析/生成/渲染各环节 |
| Worker 队列长度 | 待处理 jobs 数量 |
| Worker 处理耗时 | 按 job_type 分桶 |
| API 请求量/QPS | 按接口统计 |
| 错误率 | 5xx、job failed |
| 磁盘/内存/CPU | 基础资源 |

### 5.3 告警规则

| 告警 | 条件 | 通知 |
|---|---|---|
| Worker 队列堆积 | pending > 10 超过 10 分钟 | 钉钉/企业微信 |
| LLM 调用失败率 | > 5% | 钉钉/企业微信 |
| 任务失败率 | > 10% | 钉钉/企业微信 |
| 磁盘使用率 | > 80% | 钉钉/企业微信 |
| LLM 成本激增 | 单日 > 预算 150% | 邮件 |

---

## 6. 日志策略

| 日志类型 | 收集方式 | 保留策略 |
|---|---|---|
| 应用日志 | 容器 stdout + Loki | 30 天 |
| 访问日志 | Nginx 日志 | 90 天 |
| LLM 调用日志 | MySQL + Langfuse | 长期（合规要求） |
| 审计日志 | MySQL | 长期 |
| 错误日志 | Sentry/Loki | 90 天 |

### 日志格式

```json
{
  "timestamp": "2026-08-20T10:00:00Z",
  "level": "INFO",
  "service": "backend",
  "request_id": "req-123",
  "task_id": "task-456",
  "message": "LLM generation completed",
  "duration_ms": 2500,
  "model": "claude-sonnet-4.6"
}
```

---

## 7. 备份策略

| 数据 | 备份方式 | 频率 |
|---|---|---|
| MySQL 数据库 | mysqldump + 增量 binlog | 每日全量 + 实时 binlog |
| MinIO 对象 | mc mirror 到异地 | 每日同步 |
| Skill 仓库 | Git 多 remote | 每次提交 |
| 配置文件 | Git + 加密存储 | 每次变更 |

### 恢复目标

| 指标 | 目标 |
|---|---|
| RPO（恢复点目标） | 数据库 ≤ 1 小时，文件 ≤ 24 小时 |
| RTO（恢复时间目标） | ≤ 4 小时 |

---

## 8. 阶段一最小部署方案

```yaml
# docker-compose.dev.yml
services:
  mysql:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: dev
      MYSQL_DATABASE: protocol_copilot
      MYSQL_USER: dev
      MYSQL_PASSWORD: dev
    volumes:
      - mysql_data:/var/lib/mysql
    ports:
      - "3306:3306"

  minio:
    image: minio/minio
    command: server /data --console-address ":9001"
    environment:
      MINIO_ROOT_USER: minio
      MINIO_ROOT_PASSWORD: minio123
    ports:
      - "9000:9000"
      - "9001:9001"

  backend:
    build: ./backend
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=mysql+pymysql://dev:dev@mysql:3306/protocol_copilot
      - MINIO_ENDPOINT=minio:9000
    depends_on:
      - mysql
      - minio

  worker:
    build: ./backend
    command: python -m scripts.run_worker
    volumes:
      - ./backend:/app
    environment:
      - DATABASE_URL=mysql+pymysql://dev:dev@mysql:3306/protocol_copilot
    depends_on:
      - mysql
      - minio

  frontend:
    build: ./frontend
    ports:
      - "5173:80"
```

### 阶段一不做

- Kubernetes
- 多可用区部署
- 自动扩缩容
- 完整监控看板
- 异地灾备

这些阶段二/三再引入。

---

## 9. 关键运维 SOP

| 场景 | 操作 |
|---|---|
| 更新 backend | `docker-compose up -d --build backend worker` |
| 更新数据库 schema | `docker-compose exec backend alembic upgrade head` |
| 查看 worker 日志 | `docker-compose logs -f worker` |
| 扩展 worker | 修改 `deploy.replicas` 后 `docker-compose up -d` |
| 数据库备份 | `docker-compose exec mysql mysqldump ...` |
| 恢复服务 | 从备份恢复 MySQL + MinIO |

---

## 10. 关联文档

- `笔记/O、数据合规与隐私保护.md`：部署模式与数据驻留
- `笔记/R、安全与权限设计.md`：安全控制措施
- `笔记/M、成本估算与预算.md`：基础设施成本

---

## 11. 参考来源

- [FastAPI Best Practices for Production: Complete 2026 Guide](https://fastlaunchapi.dev/blog/fastapi-best-practices-production-2026)
- [Production-Ready FastAPI Deployment Using Docker and Uvicorn](https://seenode.com/blog/deploy-fastapi-docker-and-uvicorn)
- [LLM Observability Tools: 2026 Comparison](https://lakefs.io/blog/llm-observability-tools/)
- [Langfuse Review 2026](https://llmtools.cc/tool/langfuse/)
