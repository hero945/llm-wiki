---
tags:
  - 里程碑
  - 执行计划
  - 项目管理
  - M11
  - AI方案撰写
status: 已细化
related:
  - "[[1、AI方案撰写_竞品分析与架构]]"
  - "[[2、项目决策记录]]"
  - "[[4、技术里程碑与执行计划]]"
  - "[[5、架构决策记录]]"
  - "[[技术选型]]"
---

# L. 项目里程碑与第一周行动项

> 本文档记录项目各阶段里程碑、技术启动周任务、阶段一任务以及第一周可执行的行动清单。
> 定稿日期：2026-08-20

---

## 1. 项目里程碑总览

| 阶段 | 时间 | 目标 | 核心交付物 |
|---|---|---|---|
| **技术启动周** | 第 1 周 | 仓库、骨架、Schema、网关、第一个 Skill | 可本地跑的项目 + 元数据/Skill 初稿 |
| **阶段一** | 第 1-2 月 | 跑通第 1.1.1 章端到端 | 第一个章节的 Word 初稿 + 盲评 baseline |
| **阶段二** | 第 2-4 月 | 扩展章节 + 反馈闭环 | 第 1 章全章 + 第 3/4/5 章 + 修改痕迹回流 |
| **阶段三** | 第 4-6 月 | 完整覆盖 + 平台化 | 14 章 + Docker Compose 交付包 |

---

## 2. 技术启动周任务（第 1 周）

### 2.1 工程骨架

| 任务 | 产出物 | 优先级 |
|---|---|---|
| 初始化 Python 项目 | `pyproject.toml`、目录结构 | P0 |
| 配置 uv + ruff + mypy + pytest | 可运行的 lint/test 命令 | P0 |
| 搭 FastAPI 骨架 | `src/api/main.py` 可启动 | P0 |
| 搭 worker 骨架 | `scripts/run_worker.py` 可运行 | P0 |
| MySQL + MinIO Docker Compose | `docker-compose.yml` | P0 |
| Alembic 迁移 | 初始 schema | P0 |

### 2.2 核心模块

| 任务 | 产出物 | 优先级 |
|---|---|---|
| 迁移 Extractor | `src/extractor/` | P0 |
| 定义 Pydantic 模型 | `src/models/` | P0 |
| LLM 网关（基于 LiteLLM） | `src/llm/gateway.py` | P0 |
| Skill Loader | `src/skills/loader.py` | P0 |
| 第一个 Skill 1.1.1 | `skills/chapter_1_1_1/v1.0.0.yaml` | P0 |
| Generator 骨架 | `src/generator/generator.py` | P0 |
| Word Renderer | `src/renderer/word_renderer.py` | P1 |

### 2.3 验证

| 任务 | 产出物 | 优先级 |
|---|---|---|
| 跑通第一个端到端 | `example_synopsis.txt` → `chapter_1_1_1.docx` | P0 |
| 模型 bake-off 方案 | 2-3 个候选模型对比方案 | P1 |
| 黄金样本集初稿 | 3 个样本 | P1 |

---

## 3. 阶段一任务（第 1-2 月）

| 模块 | 关键任务 | 验收标准 |
|---|---|---|
| Extractor | 完善规则、接入 LLM 增强 | 3 份样例元数据完整提取 |
| 确认工作台 | 后端 API + 前端页面 | 低置信度字段可确认/修改 |
| Generator | 完善 1.1.1 Skill、Prompt 优化 | 生成内容符合 M11 结构 |
| Word Renderer | 样式、占位符高亮、Issue 清单 | Word 可编辑、占位符红色 |
| 一致性检查器 | 6 条基础规则 | blocker=0 |
| 评估体系 | 自动评估指标 | 可输出评估报告 |
| 回归测试 | 3 个黄金样本 | Skill 升级可对比 |
| 医学专家盲评 | 3-5 份生成结果 | 修改比例 ≤ 40% |

---

## 4. 第一周行动清单（细化到每天）

### Day 1-2：工程骨架

- [ ] 初始化 `protocol-copilot/` 仓库
- [ ] `pyproject.toml` + uv 配置
- [ ] FastAPI 主应用可启动
- [ ] MySQL + MinIO docker-compose 可启动
- [ ] Alembic 初始化，创建 tasks/jobs 表

### Day 3-4：核心模块迁移

- [ ] 把 `metadata_extractor.py` 迁到 `src/extractor/`
- [ ] 定义 `Task`、`Job`、`Metadata` Pydantic 模型
- [ ] 实现基于 LiteLLM 的 LLM 网关
- [ ] 实现 Skill Loader

### Day 5：第一个端到端

- [ ] 编写 `chapter_1_1_1/v1.0.0.yaml`
- [ ] 实现 Generator 骨架
- [ ] 实现 Word Renderer
- [ ] 跑通：`example_synopsis.txt` → `chapter_1_1_1.docx`

---

## 5. 当前状态与依赖

### 已确认决策

| 原决策 | 更新后 |
|---|---|
| PostgreSQL | MySQL 8.0 |
| 当前目录迁移 | 新起 `protocol-copilot/` 文件夹 |
| LLM 网关自研 | 基于 LiteLLM 封装 |
| 前端 Vue/React 争议 | 确定 React + 门户嵌入 + 设计系统规范 |

### 未决依赖

| 依赖 | 状态 | 影响 |
|---|---|---|
| 数据合规结论 | 待法务 | 决定能否用云端 API |
| 真实方案样本 | 待获取 | 阶段一可用公开/虚构摘要先跑 |
| 医学专家时间 | 待确认 | 影响 Skill 质量和盲评 |

---

## 6. 第一周风险

| 风险 | 概率 | 应对 |
|---|---|---|
| 数据合规禁止云端 API | 中 | 网关已预留私有化配置 |
| MySQL 8.0 环境踩坑 | 低 | 用 Docker 标准化 |
| LiteLLM 某些模型支持不完善 | 中 | 准备 2 个 provider 备选 |
| 医学专家时间不到位 | 中 | 先用公开摘要做技术验证 |

---

## 7. 本周最优先的 3 件事

1. **初始化 `protocol-copilot/` 工程骨架**
   - pyproject.toml、FastAPI、Docker Compose、MySQL

2. **跑通 LLM 网关 + 第一个 Skill**
   - LiteLLM 能调通，Prompt 能渲染

3. **实现第一个端到端链路**
   - synopsis → metadata → chapter → Word

---

## 8. 关联文档

- `笔记/4、技术里程碑与执行计划.md`：更早期的里程碑初稿
- `笔记/5、架构决策记录.md`：架构层面的决策依据
- `笔记/技术选型.md`：技术栈默认选型
- `笔记/启动会速查卡.md`：P0 资源与验收指标
