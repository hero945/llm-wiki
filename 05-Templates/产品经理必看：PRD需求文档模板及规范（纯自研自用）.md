
## Prd相关描述

文档归属说明：依赖哪个项目或者产品，又哪个团队或成员负责

版本变更记录：版本号，时间，内容描述及标注，变更人

## 一 需求背景及分析（为什么要做）

### 1.1 需求背景

介绍需求的来源和出发点，简单描述，方便研发或运营同事了解需求产生的背景，包括市场趋势、行业特点、技术发展等，有助于把握需求的来龙去脉，为后续的需求分析和产品落地（或项目实施）提供参考。

当然最好就是列举数据，分析覆盖多少用户，有多少提升？对研发团队来说有什么收益或者好处。

### 1.2 产品目的

可以从如下角度展开介绍或分析：

1. **战略角度** ：考虑软件如何支持公司或组织的长期战略目标，包括市场定位、营销策略、长远目标设定以及资源规划。
2. **产品角度** ：从产品迭代、竞品对齐角度出发，关注软件的功能设计、技术可行性以及如何打造差异化优势，以满足市场需求并提升竞争力。
3. **用户角度** ：通过用户反馈、工单或投诉、用户画像变化分析等，深入理解用户需求、优化用户体验以及建立有效的用户反馈机制，确保软件设计符合用户期望并提供持续改进的基础。

### 1.3 用户故事地图

![](https://pic2.zhimg.com/v2-c1df0e602e864837965d65f8166b92f9_1440w.jpg)

## 二 需求概览（做什么）

### 2.1、明确需求目标：

需求背景要澄清该需求所要解决的问题或达到的目标，以便判断需求价值和制定解决方案的基础。期望实现时间等。

### 2.2、需求分范围：

需要所需要覆盖的终端、版本（B端、C端产品都会有不同的版本，如PC、WEB、APP、小程序等）

| 终端 | 版本号 | 期望上线时间 | 是否需要走查 |
| --- | --- | --- | --- |
| PC、WEB、APP、小程序 | 1.2.1、2.3.5 | 2024年8月20日 | 是 |

### 2.3、需求清单（结构）：

简单罗列需求，包括： **功能、交互、数据、算法、 [策略规则](https://zhida.zhihu.com/search?content_id=247116927&content_type=Article&match_order=1&q=%E7%AD%96%E7%95%A5%E8%A7%84%E5%88%99&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODQwOTE3NjMsInEiOiLnrZbnlaXop4TliJkiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNDcxMTY5MjcsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.05MKgD3PDEg0g3J1R-t1jvLuUUDj1twFZo00wT308w4&zhida_source=entity)** 等要点即可，不需要展开。

| 需求清单 |  |
| --- | --- |
| 产品模块/功能1 | 产品/功能点罗列：   [数据加工逻辑](https://zhida.zhihu.com/search?content_id=247116927&content_type=Article&match_order=1&q=%E6%95%B0%E6%8D%AE%E5%8A%A0%E5%B7%A5%E9%80%BB%E8%BE%91&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODQwOTE3NjMsInEiOiLmlbDmja7liqDlt6XpgLvovpEiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNDcxMTY5MjcsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.5avJMFcEzPAZt0HnIPYBtzQ4oUBybGAHY6V5tnNvqzs&zhida_source=entity) 或存储要求：（如有）   算法要求和期望：（如有）   策略规则：（如有） |
| 产品模块/功能2 | 产品/功能点罗列：   数据加工逻辑或存储要求：（如有）   算法要求和期望：（如有）   策略规则：（如有） |
| [埋点需求](https://zhida.zhihu.com/search?content_id=247116927&content_type=Article&match_order=1&q=%E5%9F%8B%E7%82%B9%E9%9C%80%E6%B1%82&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODQwOTE3NjMsInEiOiLln4vngrnpnIDmsYIiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNDcxMTY5MjcsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.TMLdkF-_GNtPw_wkwG0WtvICuYsgyizZfvTa6DSVJNk&zhida_source=entity) 数据分析需求 | 埋点事件触发条件或场景   埋点事件名称   埋点事件属性及值      实现后需要分析什么数据：   曝光点击率、活跃率、渗透率、留存率、转化率等。   可以区分时间（日周月）、区分对象（按次、按用户、但客户/商家） |
| [GTM策略](https://zhida.zhihu.com/search?content_id=247116927&content_type=Article&match_order=1&q=GTM%E7%AD%96%E7%95%A5&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODQwOTE3NjMsInEiOiJHVE3nrZbnlaUiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNDcxMTY5MjcsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.wPn0lLSrPWnTNqrtt200pVBrfYVdhzN4rtSzYgdoSCs&zhida_source=entity) | 时间点，面向群体和渠道、物料、培训计划 |

### 2.4、管理预期和协调资源：

需求还要考虑公司的战略方向和资源配置，确保需求实施时能得到所需的支持并符合公司的长远发展。

无特殊情况，也可以不写。

## 三 需求说明（具体怎么做）

### 3.1需求功能流程图：

需要遍历所有流程和场景，包括向前向后的闭环

![](https://pic1.zhimg.com/v2-e9b8f543c5ad1621b7e3be83b5360726_1440w.jpg)

### 3.2、功能1：

**3.1.1 功能权限区分**

- 有哪些用户和角色？不同用户、不同角色的功能入口区分
- 需要说明具体以什么标准或状态识别并区分权限

**3.1.2 有哪些功能？其功能入口分别在哪？**

- 在原型或者页面中标记对应的功能入口，说明调整或者页面变化逻辑
- 需要贴上用例图与原型图示意，不然研发可能理解偏差
- 新功能引导（图文）
- **原型稿及交互逻辑**

**3.1.3 功能界面有哪些信息以及这些信息怎么展示？**

注意不同终端的差异，如电商系统的前端和后台的差异

- 展示什么字段的信息，数据来自于哪？
- 数据信息的展示需要做什么转换？
- **原型稿及交互逻辑**
![](https://pic2.zhimg.com/v2-4fe80baad5c7ee37b3b0260156358927_1440w.jpg)

![](https://pic1.zhimg.com/v2-d814ca5b4b8643ab07f615666b541eda_1440w.jpg)

![](https://pic4.zhimg.com/v2-de8c1c616ffa362f6dd013b426f72a17_1440w.jpg)

**3.1.4** **用户交互操作有哪些？操作以后会发生什么？（数据变化、页面调整）**

- 有什么类型的操作（增删改查）
- 操作范围（单个、多个、全部）
- 操作后现象是什么？
- 操作后数据有什么变化？
- 操作是否会需要有潜在条件，或蕴含检查的信息需要兼顾？
- **原型稿及交互逻辑**

### 3.3、数据加工说明：(如有)

一般重度依赖数据的产品模块需要，如BI、画像

- 数据有哪些
- 具体加工口径是什么？
- 数据加工要求有哪些？（时效性等）

### 3.4、算法逻辑、策略规则说明：(如有)

**目的：** 帮助用户自动识别、解析、生成某些内容或结果

**数据来源/对象** ：用户输入生成内容的要求，字段1、字段2、字段3

**处理逻辑或使用模型：** 机器学习/深度学习：特征工程+模型选型；大模型：提示prompt+RAG+Agent

**输出结果要求：** 准确率、长度、性能要求、成本限制

**处理约束（如有）：** 1天XX次/用户，

![](https://pic3.zhimg.com/v2-5dcbba1bce4ad09a6ae30e9de19e54f6_1440w.jpg)

## 四 埋点需求与数据析需求（用数据说话）

| 事件埋点名称 | 事件描述 | 事件属性 |
| --- | --- | --- |
| click\_seachresults | 点击某个搜索结果 | 点击结果序号：item\_index   点击结果ID：item\_ID   归属搜索触发ID：search\_ID |

## 五 GTM方案（怎么触达用户）

什么时间完成上线？什么时候内部验证？

什么时候宣传，向谁宣传？通过什么方式什么内容宣传？（该产品或迭代的受众）

宣传侧重点是什么？（该产品或迭代的卖点或解决的问题）

内部怎么协同？出现问题以什么机制接收和处理？

## 六 产品验证计划（验证产品效果）

### 6.1数据分析：

分析埋点以及相关页面或功能数据指标是否符合预期？

### 6.2用户拜访：

体验评价（评分收集）

体验反馈（线上或线下拜访，收集反馈意见）

**6.3 潜在应对方案**

罗列方向