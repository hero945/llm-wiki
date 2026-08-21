# study-management 发布流程总结

> 提炼自 Cursor 会话「发布师傅」（2026-07-31 ~ 08-17），记录了临床研发管线系统的线上部署、压测与排障过程。
> 已做成 pi 命令：项目根目录 `.pi/prompts/deploy.md`，在项目中输入 `/deploy` 即可一键发布。

---

## 一、环境架构

**服务器**：阿里云 ECS（吉隆坡），`admin@47.250.155.94`，2 核 2 GiB，OpenClaw 镜像

同一台机器上 3 个独立 Docker 容器：

| 容器 | 作用 | 端口/内存 |
|------|------|-----------|
| `study-management-app1-1` | Java 21 Spring Boot 应用 | `127.0.0.1:8081`，上限 1.5 GiB |
| `pm-mysql` | MySQL 8.0.46 | `3306`，上限 512 MiB |
| `searxng` | 搜索（OpenClaw 自带） | `127.0.0.1:8080` |

- 部署目录：`/opt/study-management`（docker compose）
- 镜像仓库：阿里云 ACR `crpi-abxyd61kmc2rryuv.../huadong_project/study-management:master`
- 访问地址：https://pm.fanwiselabs.com/PLM/（Nginx 反代 + `/PLM/` rewrite）
- JVM 监控：Actuator 9090 端口**仅容器内可达**，需 `docker exec` 或 SSH 后 curl

## 二、标准发布流程

```
拉取镜像 → 对比 digest → compose 重建 app1 → 健康检查 → 公网验证
```

```bash
ssh -i ~/.ssh/huqmiyao-new.pem admin@47.250.155.94
cd /opt/study-management
sudo docker pull crpi-abxyd61kmc2rryuv.cn-hangzhou.personal.cr.aliyuncs.com/huadong_project/study-management:master
sudo docker compose --env-file .env up -d app1 --pull always --force-recreate --no-deps
```

验证：容器 healthy（约 35s）→ readiness UP → `https://pm.fanwiselabs.com/PLM/` 返回 200 → 提醒用户 Ctrl+Shift+R 强刷。

**红线**：不动 `pm-mysql`、不删卷 `pm-mysql-data`（业务数据）、不动 `searxng`。

## 三、踩过的坑（经验教训）

1. **SSH 连不上（Permission denied publickey）**：密钥未绑定到实例的 `authorized_keys`。解法：Workbench 登录后手动追加公钥。
2. **私网 IP 不能直连**：`172.18.x.x` 仅 VPC 内可达；Workbench Token 只用于浏览器会话。
3. **镜像 "up to date" 但以为有新版**：master 标签未更新 = CI 没 push 成功，需先确认 CI。
4. **白屏 / 静态资源 401**：前端构建 base 路径与访问路径不一致。
   - 镜像按 `/` 构建却从 `/PLM/` 访问 → 资源 401
   - 后改为按 `/PLM/` 构建 + Nginx rewrite（内部去前缀，不做 301，否则 ES module 加载失败）
5. **浏览器缓存**：每次发布后静态资源 hash 变化，必须强刷。

## 四、压测要点（VU=10 基线）

- 本机无 k6 时用 Node 脚本替代（`ops/loadtest/query-apis.mjs`）
- 登录流程：先取 CSRF token → POST 登录 → 带 Cookie 访问
- 结果：21 个查询接口，4478 请求，14.88 RPS，错误率 0%，P95 约 1.1–1.5s
- **瓶颈预判**：MySQL 容器已占 512 MiB 上限的 ~80%（MySQL 8 固定开销，非数据量问题），宿主机仅 2 GiB，压测时先盯数据库内存
- HTML 可视化报告：`ops/loadtest/generate-html-report.mjs` + 1 秒采样脚本

## 五、运维速查

```bash
# JVM 基线（容器内）
docker exec study-management-app1-1 curl -s http://127.0.0.1:9090/actuator/prometheus | grep -E '^jvm_|^hikaricp_' | head -30

# 容器资源占用
docker stats --no-stream

# MySQL 数据是否安全：重启容器不丢（卷 pm-mysql-data），删卷才丢
```

## 参考资料

- 原始对话导出：[[发布师傅]]
- pi 命令：`项目根目录/.pi/prompts/deploy.md`
