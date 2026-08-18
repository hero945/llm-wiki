---
tags: [CSR, 临床试验, 适应症机会, 立项, briefing]
created: 2026-07-13
---

# 适应症机会 Briefing 字段字典

## 定位

对应上层链路起点：

`研发假设/适应症机会 → 临床开发策略 → ...`

本字典用于把「疾病/竞品 briefing」落成可填充、可追溯的结构化模板。  
AI 可生成草稿，**不能替代医学/注册/商业判断**；每条关键结论须绑定来源。

相关：

- [[02-从新药或适应症扩展到CSR的全流程]]
- [[07-上层业务流程AI提效节点]]
- [[10-公开源最小采集方案骨架]]

## 一、文档级元数据

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `briefing_id` | string | 是 | 唯一编号，如 `IND-OPP-2026-001` |
| `title` | string | 是 | briefing 标题 |
| `asset_name` | string | 是 | 分子/产品/项目名 |
| `hypothesis_type` | enum | 是 | `new_molecular` / `new_indication` / `new_dose_combo_population` |
| `target_indication` | string | 是 | 拟评估适应症 |
| `geography_focus` | string[] | 否 | 如 `CN`, `US`, `EU`, `JP` |
| `as_of_date` | date | 是 | 情报截止日 |
| `authors` | string[] | 是 | 撰写/汇总人 |
| `reviewers` | string[] | 否 | 医学/注册/商业审阅人 |
| `status` | enum | 是 | `draft` / `in_review` / `approved` / `archived` |
| `decision_draft` | enum | 否 | `go` / `no_go` / `hold`（仅草稿，终裁人工） |

## 二、疾病分析（Disease）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `disease.name` | string | 是 | 疾病名称（中英可并存） |
| `disease.definition` | text | 是 | 定义与分型 |
| `disease.epidemiology` | text | 是 | 发病率/患病率/患者池，带来源年份 |
| `disease.standard_of_care` | text | 是 | 当前标准治疗路径 |
| `disease.unmet_need` | text | 是 | 未满足需求 |
| `disease.diagnosis_criteria` | text | 否 | 诊断/分期标准摘要 |
| `disease.guideline_refs` | SourceRef[] | 否 | 指南来源列表 |

## 三、科学假设（Hypothesis）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `hypothesis.statement` | text | 是 | 一句话假设：药—病—人群—预期获益 |
| `hypothesis.mechanism_rationale` | text | 是 | 机制依据 |
| `hypothesis.supporting_evidence` | EvidenceItem[] | 是 | 支持证据（文献/早期数据等） |
| `hypothesis.counter_evidence` | EvidenceItem[] | 否 | 反证或不确定性 |
| `hypothesis.target_population` | text | 是 | 目标人群描述 |
| `hypothesis.what_to_prove` | text | 是 | 若立项，后续要证明什么 |

## 四、竞品格局（Competitive）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `competitors[]` | CompetitorItem[] | 是 | 竞品列表，可为 0 条但字段结构保留 |
| `competitive_summary` | text | 是 | 格局一句话总结 |
| `differentiation_opportunity` | text | 是 | 差异化机会 |
| `endpoint_trends` | text | 是 | 同类试验/标签中的终点趋势 |

### CompetitorItem

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `name` | string | 是 | 药名/代号 |
| `company` | string | 否 | 公司 |
| `status` | enum | 是 | `approved` / `phase3` / `phase2` / `phase1` / `preclinical` / `unknown` |
| `approved_indications` | string[] | 否 | 已批适应症 |
| `key_endpoints` | string[] | 否 | 关键疗效终点 |
| `key_safety` | text | 否 | 关键安全性要点 |
| `dose_regimen` | text | 否 | 剂量与给药方案 |
| `geography` | string[] | 否 | 批准/开发地区 |
| `label_source` | SourceRef | 否 | 标签来源 |
| `trial_sources` | SourceRef[] | 否 | 相关试验来源 |

## 五、开发与监管线索（Pathfinder）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `path.similar_dev_paths` | text | 否 | 同类药开发路径摘要 |
| `path.likely_phases` | string | 否 | 粗判 I/II/III 起点（非最终策略） |
| `path.regulatory_notes` | text | 否 | FDA/EMA/CDE 相关关注点 |
| `path.guidance_refs` | SourceRef[] | 否 | 指导原则来源 |

> 详细临床开发策略属于下一节点（CDP/TPP），此处只保留线索，避免越级定案。

## 六、商业与可行性粗判（可选）

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `business.patient_pool_note` | text | 否 | 患者池粗估与假设 |
| `business.competitive_window` | text | 否 | 竞争窗口 |
| `feasibility.recruitment_note` | text | 否 | 入组/中心可行性粗判 |
| `feasibility.expert_inputs` | text | 否 | 专家访谈要点（内部源） |

## 七、结论与待决问题

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `conclusion.worth_doing` | text | 是 | 值不值得做（含理由） |
| `conclusion.what_to_prove` | text | 是 | 要证明什么 |
| `conclusion.open_questions` | string[] | 是 | 待决问题清单 |
| `conclusion.next_step` | text | 是 | 建议下一步（如补非临床、开 CDP） |
| `internal_evidence_needed` | string[] | 否 | 还需哪些内部证据（CSR/IB/RWD 等） |

## 八、公共类型定义

### SourceRef

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `source_id` | string | 是 | 如 `SRC-CTGOV-NCT01234567` |
| `source_type` | enum | 是 | `label` / `trial` / `literature` / `guidance` / `rwd` / `internal` / `expert` / `other` |
| `title` | string | 是 | 来源标题 |
| `url` | string | 否 | 可访问 URL |
| `publisher` | string | 否 | 发布方 |
| `version_or_date` | string | 是 | 版本或发布/检索日期 |
| `excerpt` | text | 否 | 支撑结论的原文片段 |
| `accessed_at` | datetime | 是 | 访问/采集时间 |

### EvidenceItem

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `claim` | text | 是 | 主张 |
| `strength` | enum | 否 | `strong` / `moderate` / `weak` / `signal_only` |
| `source` | SourceRef | 是 | 来源 |

## 九、JSON 模板

```json
{
  "briefing_id": "IND-OPP-2026-001",
  "title": "示例分子-示例适应症 机会判断",
  "asset_name": "示例分子",
  "hypothesis_type": "new_indication",
  "target_indication": "示例适应症",
  "geography_focus": ["CN", "US"],
  "as_of_date": "2026-07-13",
  "authors": ["医学科学"],
  "reviewers": ["注册", "商业"],
  "status": "draft",
  "decision_draft": "hold",
  "disease": {
    "name": "",
    "definition": "",
    "epidemiology": "",
    "standard_of_care": "",
    "unmet_need": "",
    "diagnosis_criteria": "",
    "guideline_refs": []
  },
  "hypothesis": {
    "statement": "",
    "mechanism_rationale": "",
    "supporting_evidence": [],
    "counter_evidence": [],
    "target_population": "",
    "what_to_prove": ""
  },
  "competitors": [],
  "competitive_summary": "",
  "differentiation_opportunity": "",
  "endpoint_trends": "",
  "path": {
    "similar_dev_paths": "",
    "likely_phases": "",
    "regulatory_notes": "",
    "guidance_refs": []
  },
  "business": {
    "patient_pool_note": "",
    "competitive_window": ""
  },
  "feasibility": {
    "recruitment_note": "",
    "expert_inputs": ""
  },
  "conclusion": {
    "worth_doing": "",
    "what_to_prove": "",
    "open_questions": [],
    "next_step": ""
  },
  "internal_evidence_needed": [],
  "sources": []
}
```

## 十、最小填写清单（先出 1 页 briefing）

必须填：

1. `hypothesis.statement`
2. `disease.unmet_need`
3. `competitive_summary` + 至少 1–3 个 `competitors`
4. `endpoint_trends`
5. `conclusion.worth_doing` / `what_to_prove` / `open_questions`
6. 关键结论对应的 `SourceRef`

可后补：商业粗估、监管细节、专家访谈、内部 CSR/IB。
