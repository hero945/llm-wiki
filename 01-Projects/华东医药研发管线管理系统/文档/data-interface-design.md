# 华东医药研发管线管理系统数据结构与接口设计

## 1. 设计原则

- 以 `Program -> Project -> Study` 作为主数据层级。
- Excel 中的 sheet 不直接等同于数据库表；系统按业务对象建模。
- 列表接口默认支持分页、筛选、排序。
- 关键数据变更统一写入审计日志。
- 枚举和字典尽量可配置，避免硬编码。
- 一期权限做到角色 + 模块级，不做字段级权限。

## 2. 核心实体

### 2.1 User

系统自管用户账号。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 用户ID |
| username | string | 登录账号，唯一 |
| displayName | string | 用户姓名 |
| department | string | 部门 |
| email | string | 邮箱 |
| phone | string | 手机号，可用于MFA |
| status | enum | ACTIVE、DISABLED、LOCKED |
| roleIds | string[] | 角色ID列表 |
| mfaEnabled | boolean | 是否启用MFA |
| mfaMethod | enum | TOTP、SMS、EMAIL |
| lastLoginAt | datetime | 最近登录时间 |
| createdAt | datetime | 创建时间 |
| updatedAt | datetime | 更新时间 |

### 2.2 Role / Permission

角色与模块权限。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| role.id | string | 角色ID |
| role.name | string | 角色名称 |
| role.description | string | 角色说明 |
| permission.module | enum | PIPELINE、STUDY、TEAM、RISK、TIMELINE、PROGRESS、USER、AUDIT、DICTIONARY |
| permission.actions | enum[] | VIEW、CREATE、UPDATE、DELETE、IMPORT、EXPORT、MANAGE |

### 2.3 Program

产品或化合物层级主数据。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | Program ID |
| productName | string | Product |
| moa | string | MOA |
| programCode | string | Program编号或名称 |
| source | enum/string | Source |
| origin | enum/string | Origin |
| status | enum | ACTIVE、ON_HOLD、CLOSED |
| createdAt | datetime | 创建时间 |
| updatedAt | datetime | 更新时间 |

### 2.4 Project

Program + Indication 层级。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | Project ID |
| programId | string | 所属Program |
| projectCode | string | Project编号 |
| indication | string | 适应症 |
| ta | string | 治疗领域 |
| currentStage | enum | 当前汇总阶段 |
| approvalDate | date | 获批日期 |
| status | enum | ACTIVE、ON_HOLD、CLOSED |
| createdAt | datetime | 创建时间 |
| updatedAt | datetime | 更新时间 |

### 2.5 Study

临床研究明细和状态来源。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | Study ID |
| projectId | string | 所属Project |
| studyNo | string | Study编号 |
| indication | string | 适应症 |
| phase | enum | Pre-IND、IND、Ph1、Ph2、Pre-3、Ph3-1、Ph3-2、Pre-NDA/BLA、NDA/BLA |
| status | enum | PLANNED、ACTIVE、ON_HOLD、CLOSED |
| plannedStartDate | date | 计划开始日期 |
| actualStartDate | date | 实际开始日期 |
| plannedEndDate | date | 计划结束日期 |
| actualEndDate | date | 实际结束日期 |
| ownerUserId | string | 负责人 |
| createdAt | datetime | 创建时间 |
| updatedAt | datetime | 更新时间 |

### 2.6 TeamAssignment

团队职责分配。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 分配ID |
| projectId | string | 所属Project |
| studyId | string | 可选，所属Study |
| functionRole | enum/string | PL、APL、PM、APM、RA、CM、CP、PV、CO、Lab等 |
| userId | string | 负责人 |
| backupUserId | string | 备份负责人 |
| status | enum | ACTIVE、ON_HOLD、CLOSED |

### 2.7 RiskItem

风险管理记录。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 风险ID |
| programId | string | 所属Program |
| projectId | string | 所属Project |
| studyId | string | 所属Study |
| sequenceNo | number | 序号 |
| riskStatement | text | 风险描述 |
| impactScore | number | 影响评分，1-5 |
| likelihoodScore | number | 可能性评分，1-5 |
| detectabilityScore | number | 可检测性评分，1-5 |
| riskScore | number | 自动计算分值 |
| riskOwner | string | 风险归属部门和负责人 |
| existingControl | text | 目前已有风险控制方法 |
| communicationPlan | text | 风险管理沟通 |
| interimEvaluationDate | date | 阶段性评估日期 |
| additionalControlActions | text | 额外风险控制措施 |
| actionOwner | string | 所采取行动的负责人 |
| completionDate | date | 完成日期 |
| reassessmentCause | text | 触发再评估的原因 |
| followUpActions | text | 评估后需要采取的措施 |

### 2.8 Milestone

里程碑计划和实际进度。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 里程碑ID |
| projectId | string | 所属Project |
| studyId | string | 可选，所属Study |
| phaseGroup | enum/string | PreIND、IND、Pre3、Protocol、Site、FPI等 |
| milestoneName | string | 里程碑名称 |
| planVersion | string | 计划版本 |
| plannedDate | date | 计划日期 |
| actualStartDate | date | 实际开始 |
| actualEndDate | date | 实际结束 |
| note | text | 延迟或提前说明 |

### 2.9 ProgressUpdate

周期性职能进展。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 进展ID |
| projectId | string | 所属Project |
| studyId | string | 可选，所属Study |
| functionName | enum/string | CM、CP、PV、CO、Lab、Supply、ST、PG、DM、MW、RA、CMC等 |
| reportPeriodStart | date | 汇报周期开始 |
| reportPeriodEnd | date | 汇报周期结束 |
| content | text | 进展内容 |
| updatedBy | string | 更新人 |
| updatedAt | datetime | 更新时间 |

### 2.10 PipelineDictionary

管线配置字典。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 字典项ID |
| category | enum | SOURCE、ORIGIN、PRODUCT、MOA、PROGRAM、INDICATION、PROJECT、TA、FUNCTION_ROLE |
| value | string | 字典值 |
| label | string | 显示名称 |
| status | enum | ACTIVE、DISABLED |
| sortOrder | number | 排序 |

### 2.11 AuditLog

关键操作日志。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 日志ID |
| actorUserId | string | 操作人 |
| actorUsername | string | 操作账号快照 |
| action | enum | LOGIN、CREATE、UPDATE、DELETE、IMPORT、EXPORT、PERMISSION_CHANGE、PASSWORD_RESET、MFA_CHANGE |
| module | enum | AUTH、PIPELINE、STUDY、TEAM、RISK、TIMELINE、PROGRESS、USER、AUDIT、DICTIONARY |
| objectType | string | 业务对象类型 |
| objectId | string | 业务对象ID |
| beforeValue | json | 变更前值 |
| afterValue | json | 变更后值 |
| ipAddress | string | 来源IP |
| deviceInfo | string | 设备信息 |
| result | enum | SUCCESS、FAILED |
| createdAt | datetime | 操作时间 |

## 3. 状态汇总规则

Project 的 `currentStage` 默认由其下 Study 数据自动汇总生成。

一期建议规则：

1. 取 Project 下状态为 ACTIVE 或 ON_HOLD 的 Study。
2. 按阶段顺序取最靠后的阶段作为 Project 当前阶段。
3. 如果没有 ACTIVE 或 ON_HOLD Study，则按最近更新时间取 CLOSED Study 的最高阶段。
4. 人工不直接编辑 Project 的 `currentStage`，如需修正，应修改 Study 数据。

阶段顺序：

```text
Pre-IND -> IND -> Ph1 -> Ph2 -> Pre-3 -> Ph3-1 -> Ph3-2 -> Pre-NDA/BLA -> NDA/BLA
```

## 4. 权限设计

| 角色 | 主要权限 |
| --- | --- |
| 超级管理员 | 用户、角色、字典、全部业务数据、审计日志 |
| PM | 管线、Project、Study、Timeline、Progress维护 |
| 职能用户 | 对应职能的Team、Risk、Progress维护 |
| 只读用户 | 管线、Project、Study、Risk、Progress查看 |

权限动作统一为：

```text
VIEW, CREATE, UPDATE, DELETE, IMPORT, EXPORT, MANAGE
```

## 5. 接口边界

接口命名使用复数资源名，列表接口支持分页。

### 5.1 Auth / User

- `POST /api/auth/login`
- `POST /api/auth/mfa/verify`
- `POST /api/auth/logout`
- `GET /api/users`
- `POST /api/users`
- `PATCH /api/users/{userId}`
- `POST /api/users/{userId}/reset-password`
- `PATCH /api/users/{userId}/mfa`
- `GET /api/roles`
- `POST /api/roles`
- `PATCH /api/roles/{roleId}`

### 5.2 Pipeline

- `GET /api/programs`
- `POST /api/programs`
- `PATCH /api/programs/{programId}`
- `GET /api/projects`
- `POST /api/projects`
- `PATCH /api/projects/{projectId}`
- `GET /api/projects/{projectId}`
- `GET /api/projects/{projectId}/studies`

### 5.3 Study / Team / Risk / Timeline / Progress

- `GET /api/studies`
- `POST /api/studies`
- `PATCH /api/studies/{studyId}`
- `GET /api/team-assignments`
- `POST /api/team-assignments`
- `PATCH /api/team-assignments/{assignmentId}`
- `GET /api/risks`
- `POST /api/risks`
- `PATCH /api/risks/{riskId}`
- `GET /api/milestones`
- `POST /api/milestones`
- `PATCH /api/milestones/{milestoneId}`
- `GET /api/progress-updates`
- `POST /api/progress-updates`
- `PATCH /api/progress-updates/{progressUpdateId}`

### 5.4 Dictionary / Audit / Import Export

- `GET /api/dictionaries`
- `POST /api/dictionaries`
- `PATCH /api/dictionaries/{dictionaryId}`
- `GET /api/audit-logs`
- `POST /api/imports/{module}`
- `GET /api/exports/{module}`

## 6. 通用接口约定

### 6.1 分页响应

```json
{
  "data": [],
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "totalItems": 0,
    "totalPages": 0
  }
}
```

### 6.2 错误响应

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request data",
    "details": {}
  }
}
```

常用状态码：

- `400`：请求格式错误。
- `401`：未登录。
- `403`：无权限。
- `404`：资源不存在。
- `409`：数据冲突。
- `422`：业务校验失败。
- `500`：服务端错误。

## 7. 审计日志触发点

必须记录审计日志的操作：

- 登录成功、登录失败、登出。
- 创建、编辑、删除 Program、Project、Study。
- 创建、编辑、删除 TeamAssignment、RiskItem、Milestone、ProgressUpdate。
- 导入、导出任一业务模块数据。
- 创建、编辑、停用用户。
- 角色、权限变更。
- 密码重置。
- MFA 启用、停用、重置。
- 字典配置变更。

不记录普通列表查看、详情查看、筛选、排序和列宽调整。

## 8. 验收标准

- 研发可以基于本文档绘制 ER 图。
- 每个 Excel 关键模块都有对应实体或接口范围。
- 风险分值计算规则明确。
- Project 状态汇总规则明确。
- 用户、角色、MFA、操作日志纳入一期数据模型。
- API 列表接口具备分页、筛选、排序扩展空间。
