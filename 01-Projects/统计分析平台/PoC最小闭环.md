# PoC 最小闭环

工作区：`C:\Users\admin\Desktop\workspace\sce-poc`

## 运行

```powershell
cd C:\Users\admin\Desktop\workspace\sce-poc
python server.py    # 然后浏览器打开 http://localhost:8080
```

命令行版：`python demo.py`（与网页共用同一条管线）

## 演示内容

点"运行一轮任务"走完整个闭环：

1. **执行任务**：2 个 SAS TLF 程序（mock 执行器，有 SAS 环境设 `SCE_SAS_EXE` 即切真实执行）
2. **日志扫描**：自动判定 clean / warn / fail，展开可见触发规则的日志行
3. **差异比较**：本次输出 vs 基线，红绿高亮显示哪张表哪几行数字变了
4. **登记留痕**：运行记录 append-only 追加到 `outputs/runs.json`

## 模块与平台组件对应

| PoC 模块 | 平台组件 |
|---|---|
| src/executor.py | 执行层：任务队列 + SAS 计算节点 |
| src/logscan.py | 质量中心：日志自动扫描（QC） |
| src/diffcmp.py | 质量中心：输出差异比较（回归测试） |
| src/runmeta.py | 治理层：元数据 + 审计留痕 |

## 下一步扩展方向

- 任务定义文件化（宏参数注入，"刷新某 study 全部表格"批任务）
- RTF/PDF 真实格式比对（pdfplumber）
- runs.json → 真正的数据库表
- 差异报告页加复核签字（对接"复核留痕"场景）
