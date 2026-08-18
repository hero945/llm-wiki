---
created: 2026-07-12
tags:
  - obsidian
  - ollama
  - copilot
  - embedding
---

# Obsidian 使用本地 Ollama 模型经验

这次目标是让 Obsidian 里的 Copilot 插件使用本机 Ollama 部署的模型，聊天模型使用 `gemma4:latest`，向量/嵌入模型使用 `nomic-embed-text`。

## 最终可用配置

Ollama 服务地址：

```text
http://localhost:11434
```

聊天模型：

```text
gemma4:latest
```

Embedding 模型：

```text
nomic-embed-text
```

Copilot 里最终使用的是 Ollama provider，而不是 OpenAI-compatible provider。

聊天模型 key：

```text
gemma4:latest|ollama
```

Embedding 模型 key：

```text
nomic-embed-text|ollama
```

本地 Ollama 不需要真正的 API Key。插件如果强制要填，可以填空或填一个占位值，例如：

```text
ollama
```

但 native Ollama provider 一般可以不填。

## 为什么 gemma4 不能当 embedding 模型

都是“模型”，但用途不同。

`gemma4:latest` 是聊天/文本生成模型。它的工作是读问题、生成回答，像一个会说话的助手。

`nomic-embed-text` 是 embedding 模型。它不负责聊天，也不负责写文章。它的工作是把一段文字变成一串数字向量，让系统能判断两段文字的语义距离。

可以这样理解：

- 聊天模型：负责“回答你”。
- Embedding 模型：负责“帮系统找相关笔记”。

Copilot 做 vault QA 时，通常流程是：

1. 用 embedding 模型把笔记内容转成向量。
2. 用户提问时，也把问题转成向量。
3. 根据向量相似度找出最相关的笔记片段。
4. 把这些片段交给聊天模型。
5. 聊天模型根据片段生成回答。

所以它们不是互相替代，而是配合工作。

## 下载模型

查看本机已有模型：

```bash
ollama list
```

下载 embedding 模型：

```bash
ollama pull nomic-embed-text
```

下载成功后，`ollama list` 应该能看到类似：

```text
nomic-embed-text:latest    274 MB
gemma4:latest              9.6 GB
```

注意：有些图形界面不会把 `nomic-embed-text` 显示在聊天模型列表里，因为它不是聊天模型。以 `ollama list` 为准。

## 验证 Ollama 是否可用

测试聊天模型：

```bash
curl http://localhost:11434/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemma4:latest",
    "messages": [
      {"role": "user", "content": "say OK"}
    ],
    "stream": false
  }'
```

测试 embedding 模型：

```bash
curl -s http://localhost:11434/api/embeddings \
  -H 'Content-Type: application/json' \
  -d '{"model":"nomic-embed-text","prompt":"测试 Obsidian embedding"}' \
  | jq '.embedding | length'
```

如果输出：

```text
768
```

说明 `nomic-embed-text` 正常工作。

## Obsidian Copilot 设置经验

这次 OpenAI-compatible 的配置方式连接不稳定，虽然 Ollama 的 OpenAI 兼容接口本身能用，但 Copilot 里会出现连接失败。

最后可用的方式是使用 Copilot 的 native Ollama provider：

聊天模型配置重点：

```json
{
  "name": "gemma4:latest",
  "provider": "ollama",
  "enabled": true,
  "baseUrl": "http://localhost:11434",
  "apiKey": "",
  "isEmbeddingModel": false,
  "stream": false,
  "displayName": "myllm"
}
```

Embedding 模型配置重点：

```json
{
  "name": "nomic-embed-text",
  "provider": "ollama",
  "enabled": true,
  "baseUrl": "http://localhost:11434",
  "apiKey": "",
  "isEmbeddingModel": true,
  "displayName": "nomic-embed-text"
}
```

配置写入后，需要重启 Obsidian，或者关闭再开启 Copilot 插件，让它重新读取配置。

## 怎么确认 Obsidian 真用上了 embedding

1. 重启 Obsidian 或重启 Copilot 插件。
2. 打开 Copilot 设置，确认 embedding model 显示为 `nomic-embed-text` 或 `nomic-embed-text|ollama`。
3. 在 Copilot 里执行 `Index vault`、`Refresh vault index` 或类似的重新索引操作。
4. 终端里查看当前 Ollama 运行模型：

```bash
ollama ps
```

如果索引期间看到 `nomic-embed-text:latest`，说明 Obsidian 正在调用它。

更实际的验证方式：重新索引后，问 Copilot 一个只存在于自己笔记里的问题。如果它能根据笔记回答，说明“embedding 检索 + 聊天模型回答”的链路基本通了。

## 这次踩坑总结

- Ollama 本地模型不需要真正申请 API Key。
- `gemma4:latest` 能聊天，但不能代替 embedding 模型。
- `nomic-embed-text` 是给检索/索引用的，不会出现在很多聊天模型选择框里。
- Copilot 里优先用 `provider: ollama`，不要优先走 OpenAI-compatible。
- base URL 使用 `http://localhost:11434`，不是 `http://localhost:11434/v1`。
- 如果改了 Copilot 配置，要重启 Obsidian 或重启插件。
- 终端验证比插件界面更可靠：`ollama list` 看模型是否下载，embedding API 看模型是否能用。

## 常用命令

```bash
# 查看本地模型
ollama list

# 查看正在运行的模型
ollama ps

# 下载 embedding 模型
ollama pull nomic-embed-text

# 测试 embedding 输出长度
curl -s http://localhost:11434/api/embeddings \
  -H 'Content-Type: application/json' \
  -d '{"model":"nomic-embed-text","prompt":"测试"}' \
  | jq '.embedding | length'
```
