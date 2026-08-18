# 华东医药研发管线管理系统

一期需求沟通与研发建模文档。代码仓库：`Desktop/workspace/int-service-study-management`。

## 目录

```text
华东医药研发管线管理系统/
├── 文档/     PRD、蓝图、接口、部署笔记
├── 原型/     Figma V2 画板
└── 参考/     现有 Excel 模板
```

## 文档

- [[prd-v3]]：产品需求（v3）
- [[business-blueprint|业务蓝图]]：面向业务使用方
- [[data-interface-design|数据结构与接口设计]]：对象、字段、权限、接口边界
- [[figma-pages-v2]]：页面清单
- [[HTTPS与Nginx部署知识库]]：证书、反向代理、上线排查

## 原型与参考

- 浏览器打开 `原型/figma-v2-reference-style/index.html`
- `参考/Program Dashboard_Template v4.1_20260707.xlsx`：一期要复刻的 Excel 管线表

## 一期定位

一期目标是复刻并优化现有 Excel 管理方式。核心层级 `Program -> Project -> Study`，覆盖管线配置、管线总览、Study 台账、团队、风险、里程碑、职能进展、用户管理和操作日志。

## 默认决策

- 系统形态：Web 系统。
- 登录体系：系统自建账号，不接入公司 SSO、LDAP 或 AD。
- 交互方式：优先保留 Excel 式表格体验，支持筛选、排序、批量编辑、导入和导出。
- 权限模型：角色 + 模块权限，不做字段级权限。
- 状态汇总：Study 台账驱动 Project 管线总览状态。
- 审计范围：记录关键操作和关键数据变更，不记录普通页面查看和筛选行为。

下一期需求先对照以上决策和 [[可复用资产索引]]，再改 PRD；改了默认决策必须回写本页并登记 [[产出台账]]。
