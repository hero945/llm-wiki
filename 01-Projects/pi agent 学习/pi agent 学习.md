# pi agent 学习

> 学习目标：熟悉 pi coding agent 的架构设计与使用方式，逐步掌握定制与扩展能力。
> 官方安装位置：`C:\Users\admin\AppData\Roaming\npm\node_modules\@earendil-works\pi-coding-agent\`

---

## 一、pi 架构设计概览

### 核心理念：极简内核 + 激进可扩展

**"让 pi 适应你的工作流，而不是反过来"**。内核刻意保持最小，砍掉了同类工具内置的功能（MCP、子代理、计划模式、权限弹窗、内置 TODO、后台 bash），全部交给扩展系统实现。

### 分层架构（monorepo）

```
┌─────────────────────────────────────┐
│  pi-coding-agent (CLI harness)      │  ← 直接使用的入口
├─────────────────────────────────────┤
│  pi-tui        终端 UI 组件          │
│  pi-client     RPC 客户端            │
│  pi-protocol   进程间通信协议         │
├─────────────────────────────────────┤
│  pi-agent-core Agent 框架（循环、工具）│
├─────────────────────────────────────┤
│  pi-ai         LLM 工具包（各厂商接入）│
└─────────────────────────────────────┘
```

### 四种运行模式

| 模式 | 用途 |
|------|------|
| Interactive | 交互式 TUI（默认） |
| Print / JSON | `-p` 一次性输出；`--mode json` 输出事件流 |
| RPC | `--mode rpc`，stdin/stdout 上跑 JSONL 协议，供其他进程集成 |
| SDK | 作为库嵌入自己的应用（`createAgentSession`） |

### 工具系统

默认只给模型 **4 个工具**：`read`、`write`、`edit`、`bash`（另有 `grep`、`find`、`ls`）。模型靠这几个原语组合完成一切任务。

### 扩展机制（四个层级）

1. **Extensions** — TypeScript 模块：自定义工具、命令、快捷键、事件钩子、UI 组件
2. **Skills** — 遵循 Agent Skills 标准的 Markdown 能力包，按需加载
3. **Prompt Templates** — 可复用提示词模板，`/name` 展开
4. **Themes** — 主题，支持热重载

可打包成 **Pi Packages**，通过 npm 或 git 分享（`pi install git:github.com/user/repo`）。

### 会话设计

- 会话存为 **JSONL 文件**，内部是**树结构**：每条记录有 `id` 和 `parentId`
- 支持原地分支（`/tree`）、分叉（`/fork`）、克隆（`/clone`）
- 长会话通过 **compaction**（压缩摘要）控制上下文，手动 `/compact` 或自动触发

### 安全/信任模型

启动时对项目目录做 **trust 判定**：未信任的项目不加载其本地设置和扩展，防止恶意仓库注入。可用 `--approve` / `--no-approve` 临时控制。

### 配置层级

- 全局：`~/.pi/agent/`（settings、扩展、技能、会话）
- 项目：`.pi/`（覆盖全局）
- 上下文文件：`AGENTS.md` / `CLAUDE.md` 从父目录逐级拼接；`SYSTEM.md` 可替换系统提示词

---

## 二、学习路径（从用到改，五个阶段）

### 阶段 1：日常使用起来
- 在真实项目里跑 `pi`，让它读代码、改 bug、跑测试
- 熟悉编辑器：`@` 引用文件、Tab 补全、`!command` 跑命令、Ctrl+V 粘贴图片
- 学会中断引导：工作中按 **Enter** 发引导消息，**Escape** 中止
- 切换模型：Ctrl+L 选模型、Shift+Tab 调思考等级
- 📖 参考：`README.md` Interactive Mode、`docs/keybindings.md`

### 阶段 2：掌握会话管理（pi 的杀手锏）
- `/tree` 会话树跳转、开分支
- `/fork` 从历史点分叉、`/resume` 恢复旧会话
- 长任务体验 `/compact` 压缩
- 读 `docs/session-format.md` 了解 JSONL 树结构

### 阶段 3：轻量级定制（只写 Markdown）
1. **AGENTS.md** — 项目约定、常用命令
2. **Prompt Templates** — 重复提示词模板化
3. **Skills** — 工作流程写成 SKILL.md
- 📖 参考：`docs/prompt-templates.md`、`docs/skills.md`

### 阶段 4：写 Extension（真正的威力）
按难度递进：
1. 注册自定义命令
2. 注册自定义工具给模型调用
3. 监听事件（如 `tool_call`）做权限校验或日志
4. 定制 UI（状态栏、页脚）
- 📖 精读 `docs/extensions.md`，抄 `examples/extensions/` 的例子改

### 阶段 5：深度集成与底层
- **SDK**：嵌入自己的 Node 应用（`docs/sdk.md` + `examples/sdk/`）
- **RPC 模式**：从非 Node 程序驱动 pi（`docs/rpc.md`）
- 读底层包源码：`pi-ai`（模型接入）、`pi-agent-core`（agent 循环）
- 研究别人如何用扩展实现子代理、计划模式等"官方不做"的功能

---

## 三、学习建议

> 不要急着读源码，先在真实工作里用一两周。遇到问题（"要是能……就好了"）时，往往就是学扩展系统的最佳切入点——pi 的设计就是为这个准备的。

## 参考资料

- 官方文档：`C:\Users\admin\AppData\Roaming\npm\node_modules\@earendil-works\pi-coding-agent\docs`
- 官网：https://pi.dev
- 设计哲学博客：https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
