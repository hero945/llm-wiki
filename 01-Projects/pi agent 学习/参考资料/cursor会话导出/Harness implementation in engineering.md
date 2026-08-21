# Harness implementation in engineering

> 导出自 Cursor 会话 (6297ed45-9f24-4bcb-9005-51fa38c87478)，共 49 条消息

---

## 👤 用户

harness到底是什么，工程上一般怎么实现

## 🤖 助手

先确认你说的 harness 更可能是测试框架、评测套件，还是 AI Agent 外围那层编排，我查一下近期对话里有没有具体语境。

## 🤖 助手

上一轮对话里你在看极简 AI Agent 框架，所以这里按 **Agent Harness** 来讲；工程里这个词还有测试套件的意思，我会一并对照。

## 🤖 助手

**Harness 是套在模型外面的运行时骨架：模型负责想，harness 负责让它能干活、停得住、可复现。**

工程里这个词最常见有两层。你上一轮看的极简 AI 编程 Agent，说的是第二层。

## 词从哪来

Harness 原意是马具、线束：把马力接到车上，或把电线接到设备上。软件里借这个隐喻——**被驱动的东西很强，但自己不会按流程工作，需要一套固定的夹具、回路和接口把它接进系统。**

| 语境 | 指什么 | 典型例子 |
|---|---|---|
| 传统测试 | Test harness：驱动被测对象、喂输入、收输出、判对错 | JUnit runner、pytest、gtest |
| LLM 评测 | Eval harness：统一跑题、记分、对比模型 | EleutherAI `lm-evaluation-harness` |
| AI Agent | Agent harness：模型周围的循环、工具、权限、记忆、停止条件 | Cursor Agent、Claude Code、你看的那类极简框架 |

核心不是“又一个框架”，而是：**模型是概率引擎，harness 是确定性工程。** 能力上限在模型，能不能稳定变成产品在 harness。

## Agent Harness 到底管什么

一个裸模型只能吐文本。要变成能改代码、跑命令、调 API 的 Agent，外面必须有一层：

1. **收用户目标**，拼成带工具定义、系统提示、规则、文件上下文的请求
2. **调模型**，解析它是“直接回答”还是“要调工具”
3. **执行工具**（读文件、改文件、shell、MCP……），把结果写回对话
4. **再调模型**，直到它认为完成、或撞上停止条件
5. **全程管预算、权限、日志、失败重试**

这整套循环就是 harness。Cursor 里你看到的工具调用、权限确认、子 Agent、待办、后台 bash，都是 harness 能力，不是模型自带的。

极简框架常故意**不内置**子 Agent、Plan、权限弹窗、待办——那是在减 harness 表面积，把编排权交给你的工作流。

## 工程上一般怎么实现

几乎所有实现都落成同一个循环，伪代码如下：

```python
def run(goal, tools, policy):
    messages = [system_prompt, user(goal)]
    while not should_stop(messages, policy):
        response = llm.chat(messages, tools=tools.schemas())
        if response.is_final_text():
            return response.text
        for call in response.tool_calls:
            if not policy.allow(call):
                messages.append(denied(call))
                continue
            result = tools.execute(call)   # 超时、沙箱、截断
            messages.append(tool_result(call, result))
        compact_or_summarize(messages)     # 控上下文
    return timeout_or_budget_exceeded()
```

落地时通常拆成这些模块，而不是一个大脚本：

**1. Agent Loop（编排内核）**  
while 循环 + 停止条件：模型说结束、连续失败、步数/token/墙钟超时、用户取消。这是 harness 的心脏。

**2. Tool Runtime（工具运行时）**  
统一接口：`name / json schema / execute(args) -> string | artifact`。内部再分：
- 本地：读文件、补丁、grep、shell
- 远程：HTTP、MCP
- 副作用边界：超时、工作目录、环境变量、输出截断

工具适配工作流，而不是反过来——就是把这一层做成可插拔，而不是写死“必须有 Plan / 子 Agent”。

**3. Policy / Permission（策略）**  
哪些命令能跑、能不能写 `.env`、要不要弹窗确认、网络是否允许。模型没有安全边界，边界在 harness。

**4. Context Assembly（上下文装配）**  
系统提示、`AGENTS.md` / rules、打开的文件、检索到的代码、历史压缩。工程难点往往在这里：既要给够信号，又不能把窗口塞爆。

**5. Memory / State（状态）**  
会话消息、待办、后台任务、git 工作树、artifact 路径。模型是无状态的；跨步记忆全靠 harness 存。

**6. Observability（可观测）**  
每一步：提示、工具入参、耗时、token、退出码、截断原因。没有日志的 Agent 几乎无法调试。

**7. Eval 挂钩（可选但关键）**  
同一套 loop 用固定任务集回归：给定仓库 + 目标，看它是否提交对、测试是否绿。这就是 agent 版 test harness。

## 一个最小可跑的结构

```
harness/
  loop.py          # 上面那个 while
  llm.py           # 供应商适配（OpenAI/Anthropic/...）
  tools/
    fs.py
    shell.py
    grep.py
  policy.py        # allowlist / 确认
  context.py       # 拼 prompt、压缩历史
  session.py       # 消息与 checkpoint
```

再往上加的，都是 harness 的“产品层”：子 Agent、Plan 模式、权限 UI、待办、后台 bash、MCP。它们不是 Agent 的定义，而是这个骨架上的插件。

## 和“普通 Agent 框架”差在哪

LangChain / LlamaIndex 一类更像**组件库**（链、检索、记忆抽象）。  
Harness 更像**运行时**：固定的执行循环 + 工具沙箱 + 权限 + 停止条件 + 日志。

可以记成：

- **模型**：判断“下一步做什么”
- **Harness**：保证“做的时候怎么接电、怎么限流、怎么停、怎么验收”

传统 test harness 夹的是函数/服务；agent harness 夹的是模型。形状一样：驱动 → 观察 → 判定 → 隔离副作用。只是被驱动对象从确定性代码换成了会胡来的 LLM。

如果你要往下拆，我可以按「最小 200 行可跑 harness」画一版模块边界，或对照 Cursor / Claude Code 这类完整产品，标出哪些是循环内核、哪些是产品插件。

## 👤 用户

可以，最好是图片的形式

## 🤖 助手

按你的要求做成可对照的架构图：一层是最小可跑 harness，一层标出循环内核和产品插件。先把画布组件和设计约束读清楚。

## 🤖 助手

接下来做成一张可切换的架构图：执行循环、最小模块、以及 Cursor / Claude Code 的内核与插件对照。

## 🤖 助手

类型检查里 `key` 不能直接写在这些组件上，我改成包一层再标 key。

## 🤖 助手

三张架构图已经画好，可以点开 [Agent Harness 架构](C:\Users\admin\.cursor\projects\empty-window\canvases\agent-harness-architecture.canvas.tsx) 在聊天旁边查看。这是一块 Canvas：可交互的可视化面板，比静态截图更适合对照模块。

顶部三个标签对应三种切面：

1. **执行循环** — 用户目标进入虚线框（harness 边界），模型只出现一次；右侧虚线把工具结果喂回去，循环才成立。点方块看每一层在工程里干什么。
2. **最小模块** — 约 200 行怎么切：`loop.py` 是心脏，下面是 context / llm / policy / session，再下面是 fs / shell / grep。子 Agent、Plan、权限弹窗都不进这层。
3. **产品对照** — 三座塔共用同一底座。最小框架插件层留空；Cursor 和 Claude Code 堆的是产品插件，循环形状不变。

底部卡片会跟着你点的模块更新。若图是空白的，用上面的链接打开该文件即可。

