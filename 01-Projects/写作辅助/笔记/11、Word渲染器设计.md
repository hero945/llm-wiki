---
tags:
  - Word
  - 渲染
  - python-docx
  - 占位符
  - M11
  - AI方案撰写
status: 已创建
related:
  - "[[8、生成模块设计]]"
  - "[[10、一致性检查器设计]]"
  - "[[5、架构决策记录]]"
---

# 11. Word 渲染器设计

> 本文档记录 M11 方案生成 Copilot 的 Word 渲染器设计，包括 Markdown 转 Word、占位符高亮、Issue 清单写入等。
> 定稿日期：2026-08-20

---

## 1. 模块定位

Word 渲染器是生成链路的最后一步，负责把 `ChapterContent` 渲染为可编辑的 Word 文档：

```
ChapterContent + Issue 清单
   ↓
WordRenderer
   ↓
chapter_xxx.docx
```

阶段一不依赖真实 M11 Word 模板（模板 PDF 无法直接填充），先用 `python-docx` 直接构建文档。阶段二引入 `docxtpl` 填充真实 M11 Word 模板。

---

## 2. 输入 / 输出

### 2.1 输入

| 输入 | 类型 | 说明 |
|---|---|---|
| `chapter_content` | ChapterContent | 生成的章节内容和 Issue 清单 |
| `template_path` | str | 可选，M11 Word 模板路径 |
| `output_path` | str | 输出 Word 文件路径 |

### 2.2 输出

- `.docx` 文件
- 包含章节标题、正文、占位符高亮、Issue 清单

---

## 3. 阶段一实现

### 3.1 基于 python-docx

```python
from docx import Document
from docx.shared import RGBColor, Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

class WordRenderer:
    def render_chapter(
        self,
        chapter_content: ChapterContent,
        output_path: str,
    ):
        doc = Document()

        # 标题
        doc.add_heading(
            f"{chapter_content.chapter_id} {chapter_content.chapter_title}",
            level=1,
        )

        # 正文
        for para in chapter_content.content.split("\n\n"):
            para = para.strip()
            if not para:
                continue
            self._add_paragraph(doc, para)

        # Issue 清单
        if chapter_content.issues:
            doc.add_page_break()
            doc.add_heading("生成 Issue 清单", level=2)
            for issue in chapter_content.issues:
                self._add_issue_paragraph(doc, issue)

        doc.save(output_path)

    def _add_paragraph(self, doc: Document, text: str):
        if text.startswith("##"):
            level = text.count("#", 0, 4)
            doc.add_heading(text.lstrip("#").strip(), level=level)
        else:
            p = doc.add_paragraph()
            self._render_inline(p, text)

    def _render_inline(self, paragraph, text: str):
        # 处理占位符：<输入...内容...> 红色粗体
        import re
        parts = re.split(r"(<输入[^>]*>)", text)
        for part in parts:
            run = paragraph.add_run(part)
            if part.startswith("<输入") and part.endswith(">"):
                run.bold = True
                run.font.color.rgb = RGBColor(255, 0, 0)

    def _add_issue_paragraph(self, doc: Document, issue: Issue):
        p = doc.add_paragraph(style="List Bullet")
        run = p.add_run(f"[{issue.severity.upper()}] {issue.message}")
        if issue.severity == "blocker":
            run.font.color.rgb = RGBColor(255, 0, 0)
        elif issue.severity == "warning":
            run.font.color.rgb = RGBColor(255, 165, 0)
        if issue.suggestion:
            p.add_run(f"\n建议：{issue.suggestion}")
```

---

## 4. Markdown 支持

阶段一支持的 Markdown 语法：

| Markdown | Word 样式 |
|---|---|
| `# 标题` | Heading 1 |
| `## 标题` | Heading 2 |
| `### 标题` | Heading 3 |
| `**粗体**` | 粗体 |
| `*斜体*` | 斜体 |
| `- 列表项` | List Bullet |
| `1. 列表项` | List Number |
| `<输入... >` | 红色粗体 |

阶段二再支持表格、复杂嵌套列表等。

---

## 5. 占位符样式

所有不确定信息统一使用 `<输入...内容...>` 格式：

| 元素 | 样式 |
|---|---|
| 字体 | 红色（RGB 255, 0, 0） |
| 粗细 | 粗体 |
| 大小 | 与正文相同 |

示例：

```
本试验旨在评估 X 药治疗 <输入适应症> 的有效性。
```

---

## 6. Issue 清单渲染

Issue 清单放在文档末尾或单独一页：

```
生成 Issue 清单

[BLOCKER] 生成内容中未出现主要终点：第 16 周 PASI 75 应答率
建议：检查生成结果是否遗漏主要终点描述

[WARNING] 发现禁用词：证明
建议：将'证明'改为'评估'
```

Blocker 用红色，Warning 用橙色，Info 用黑色。

---

## 7. 阶段二：基于真实 M11 模板

阶段二引入 `docxtpl`：

```python
from docxtpl import DocxTemplate

class TemplateWordRenderer:
    def render(self, chapter_content: ChapterContent, template_path: str, output_path: str):
        doc = DocxTemplate(template_path)
        context = {
            "chapter_id": chapter_content.chapter_id,
            "chapter_title": chapter_content.chapter_title,
            "content": chapter_content.content,
            "issues": chapter_content.issues,
        }
        doc.render(context)
        doc.save(output_path)
```

真实模板的优势：
- 样式与公司模板完全一致
- 自动继承页眉页脚
- 便于医学专家直接审阅

---

## 8. 文件存储

生成的 Word 文件存入 MinIO：

```python
{
  "task_id": "task-001",
  "chapter_id": "1.1.1",
  "file_path": "tasks/task-001/chapter_1_1_1.docx",
  "generated_at": "2026-08-20T10:00:00Z",
  "version": "1.0.0"
}
```

同时在 `task_outputs` 表中记录元数据。

---

## 9. 阶段一验收标准

- [ ] 能渲染章节标题
- [ ] 能渲染 Markdown 正文
- [ ] 占位符显示为红色粗体
- [ ] Issue 清单写入文档末尾
- [ ] 生成的 Word 文件可正常打开编辑
- [ ] 文件存入 MinIO 并记录元数据

---

## 10. 关联文档

- `笔记/8、生成模块设计.md`：ChapterContent 的来源
- `笔记/10、一致性检查器设计.md`：Issue 清单的来源
- `笔记/12、反馈闭环设计.md`：Word 修订模式的解析
