---
title: "01-领域现状（promo） - 研发部"
author:
  - "[[李力5]]"
created: 2026-06-30
description:
tags:
  - "tuhu"
---
[转至元数据结尾](#page-metadata-end) [转至元数据起始](#page-metadata-start)

## 一、领域标准定义（改造完成后的理想定义）

## 1.1，领域概述

**优惠定义：** 为满足业务营销运营目标，基于线上/线下不同的销售平台、渠道或活动场景，在商品定价基础之上，面向特定客户限时提供一系列的营销推广、促销手段。客户在交易过程中，通过资格享受多种促销手段组合，降低自己的成交成本。客户所享受的促销差价，即为业务主体（平台或门店）为满足特定营销目标所承担的促销成本。

基于以上优惠定义，可以明确以下几点 **基础信息** ：

1） **服务业务目标** ：优惠的配置一定是以某个或某些业务营销运营目标服务；

2） **涵盖线上/线下** ：优惠面向的客户不仅仅是线上交易的客户，还可以是线下到店的客户；

3） **不同平台/渠道** ：优惠可以针对不同平台（自有平台、第三方平台\[天猫、京东等\]）、渠道（APP、H5、小程序等）等灵活配置；

4） **特定活动场景** ：优惠可以针对特定的节假日大促特殊设定；

5） **目标客户** ：会针对不同客户进行圈层、筛选，提高业务目标达成效率；

6） **限时** ：优惠一定会有时间限制，不可能无限期享受；

7） **促销改价** ：优惠不会改变商品定价，而是在其基础之上叠加，来改变用户最终的交易成交价格（或成本）；

8） **促销组合** ：优惠促销手段多种多样，不同促销手段彼此之间，可共享也可互斥，客户可以基于组合规则叠加享受；

9） **促销资格** ：客户在享受某些促销手段时，会消耗优惠资格（全局/每月/每天等）；

10） **促销形式** ：促销手段的展现形式可以多种多样（券、立减、满减、打折、返现、赠品等），可以根据具体的营销运营目标灵活选择；

11） **促销成本** ：业务提供方（平台或门店）为满足业务运营目标所预估的成本一定有限额，且客户消耗促销成本时必须有清晰记录，以用于后续的业务资金结算；

基于优惠定义，可以明确优惠域的 **领域涉众** ：

1） **平台** ：途虎自身，优惠域提供相关系统所依赖的业务平台；

2） **用户** ：享受并使用优惠的目标客户；

3） **第三方门店** ：在优惠域相关系统上进行优惠管理配置的第三方门店维护人员等；

4） **运营** ：在优惠域相关系统上进行优惠管理配置的相关运营人员；

\*\*\* 特别说明：在途虎平台上，部分角色会重叠（例如：有些涉众既是平台的第三方门店，又是平台的用户）；

基于上述明确的基础信息和涉众，可以初步明确包含的2大 **核心领域实体** ：

1） **优惠活动** ：门店或平台运营配置具体优惠时，所创建的核心领域实体（包含或关联优惠的促销形式、限制条件、促销规则等）；

2） **优惠标识** ：用户享受并使用具体某种优惠活动时，所创建的核心领域实体（用户具体享受某种优惠时的凭证，以及后续使用时的核销等信息）；

基于上述领域涉众和核心领域实体，概括优惠的 **核心生命周期** ：

![](../attachments/image2020-2-4_19-44-29_11970c90.png)

## 1.2，领域经典流程

围绕上述优惠的领域涉众、核心领域实体和生命周期，梳理优惠域的主要流程如下：

### 1.2.1 优惠配置流程

![](../attachments/image2020-2-5_16-6-13_cf6d4fa6.png)

### 1.2.2 优惠领取流程

![](../attachments/image2020-2-5_16-19-21_28f56842.png)

### 1.2.3 优惠展示流程

![](../attachments/image2020-2-5_18-19-41_36f8b4a9.png)

### 1.2.4 优惠校验流程

![](../attachments/image2020-2-5_19-15-59_1d5febde.png)

### 1.2.5 优惠核销流程

![](../attachments/image2020-2-5_18-23-8_c926eacf.png)

### 1.2.6 优惠状态变更广播流程

![](../attachments/image2020-2-12_17-59-15_cb8191bb.png)

## 1.3，领域主要服务与能力

基于上述经典流程，总结优惠域所需提供的主要服务如下：

<table><colgroup><col> <col> <col></colgroup><tbody><tr><th>服务</th><th>主要接口/消息</th><th>接口描述</th></tr><tr><td rowspan="8">优惠配置服务</td><td>创建优惠活动</td><td>支持（运营、第三方门店等）不同角色人员创建</td></tr><tr><td>批量创建优惠活动</td><td>批量操作</td></tr><tr><td colspan="1">编辑优惠活动</td><td colspan="1">优惠活动创建之后的修改编辑（仅允许修改部分信息）</td></tr><tr><td colspan="1">审核优惠活动</td><td colspan="1">活动安全审核（包含系统风控自动审核、人工审批链）</td></tr><tr><td colspan="1">批量审核优惠活动</td><td colspan="1">批量操作</td></tr><tr><td colspan="1">查询优惠活动明细</td><td colspan="1">查询活动相关明细信息</td></tr><tr><td colspan="1">查询优惠活动列表</td><td colspan="1">不同过滤条件查询</td></tr><tr><td colspan="1">优惠活动状态变更</td><td colspan="1">支持（暂停、作废、结束、审核等）操作</td></tr><tr><td rowspan="2"><p>优惠领取服务</p><p>（目前仅优惠券支持领取操作）</p></td><td colspan="1">领取单种优惠</td><td colspan="1">（单用户、多用户）领取</td></tr><tr><td colspan="1">批量领取多种优惠</td><td colspan="1">（单用户、多用户）批量操作</td></tr><tr><td rowspan="3">优惠查询服务</td><td colspan="1">查询可用优惠活动列表</td><td colspan="1">查询单个（商品、门店、服务等）的可用优惠活动（一般用于详情页）</td></tr><tr><td colspan="1">批量查询可用优惠活动列表</td><td colspan="1">多个（商品、门店、服务等）批量操作（一般用于列表页）</td></tr><tr><td colspan="1">查询可用优惠活动最优组合列表</td><td colspan="1">查询（单个、多个）商品的可用优惠活动的最优组合（一般用于提单页）</td></tr><tr><td rowspan="2">优惠校验服务</td><td colspan="1">校验优惠</td><td colspan="1">（单个、多个）（商品、门店、服务等）校验是否可用某一个优惠活动</td></tr><tr><td colspan="1">批量校验优惠</td><td colspan="1">（单个、多个）（商品、门店、服务等）校验是否可用多个优惠活动</td></tr><tr><td rowspan="4">优惠核销服务</td><td colspan="1">核销优惠</td><td colspan="1">核销具体某一个优惠活动</td></tr><tr><td colspan="1">批量核销优惠</td><td colspan="1">批量操作核销多个优惠活动</td></tr><tr><td colspan="1">回退优惠</td><td colspan="1">核销优惠的反向操作</td></tr><tr><td colspan="1">批量回退优惠</td><td colspan="1">批量操作</td></tr><tr><td>优惠状态变更广播</td><td colspan="1">优惠相关状态变更广播MQ</td><td colspan="1">已创建/已领取/已使用/已作废/已回退等状态变更的MQ通知</td></tr></tbody></table>

针对上述主要服务种的一些共性逻辑，沉淀以下基础能力：

<table><colgroup><col> <col></colgroup><thead><tr><th><p>基础能力</p></th><th><p>能力描述</p></th></tr></thead><tbody><tr><td>优惠统一接入</td><td>提供优惠域相关服务对外统一封装和对内统一分发（领取、查询展示、校验、核销、回退等）</td></tr><tr><td colspan="1">优惠活动管理</td><td colspan="1">提供统一的优惠活动管理和状态流转控制</td></tr><tr><td colspan="1">条件计算</td><td colspan="1">提供通用的促销限制条件与促销规则计算与匹配（支持条件的与、或、非和基础运算）</td></tr><tr><td colspan="1">用户匹配</td><td colspan="1">提供通用的目标用户圈选（支持条件筛选、用户画像组合、算法动态匹配等），依赖营销通用的圈人服务</td></tr><tr><td colspan="1">商品索引</td><td colspan="1">提供通用的优惠关联对象（商品、门店、服务等）的筛选和索引查询，依赖营销通用的选单服务</td></tr><tr><td colspan="1">优惠库存</td><td colspan="1">提供通用的优惠库存管理（全局、分周期、分商品、分城市等）</td></tr><tr><td colspan="1">优惠资格</td><td colspan="1">提供通用的资格控制（支持用户、商品、周期等维度）</td></tr><tr><td colspan="1">营销预算</td><td colspan="1">提供与业务主体（平台、第三方门店）的预算对接</td></tr></tbody></table>

基于上述优惠定义和经典流程，在梳理领域主要服务和能力之后，对比不同促销形式的异同点，沉淀以下 **3种通用促销形式** ： **优惠券** 、 **优惠立减** 和 **返赠** 。

相同点：

1）3种通用促销形式，都有从配置、到展示、再到校验的一系列通用流程，且同样依赖类似的基础能力（规则计算、圈人、选单、库存、资格和预算等）。

2）3种通用促销形式，都跟交易流程强相关，涉及订单的优惠成本组成及后续资金结算。

不同点：

1） **优惠券** ：与其他2种促销形式不同的是，优惠券有前置的领取流程，且用户领取和核销有一定时间间隔，可灵活控制。基于优惠领取和核销流程分离，带来非常高的灵活度。

2） **优惠立减** ：无领取流程，所见即可享受，简单、直接，用户理解门槛低，通常营造一种即时、紧迫的促销氛围（例如：限时优惠、打折、特价等）。

3） **返赠** ：后置领取流程，用户需满足一定交易下单条件后才可后返，通常可利用返赠后的（券、卡等）带来二次消费。

除开上述通用促销形式之外，还有其他的一些促销形式，基本可以分为以下几大类：

1） **基于通用促销形式的二次包装** ：通常是通用促销形式的一种特殊类型的独立包装，或在其基础之上叠加一些用户交互的互动玩法形成的活动，如特价、打折、买三赠一、优惠定价、购后返券、赠虚拟物品卡券等

2） **独立促销活动** ：有自己一套相对较独立的活动流程，在活动流程中能够享受到优惠，如拼团、秒杀、众测等；

3） **一般优惠等价物** ：积分、E点/E卡等（有自己的一套相对较独立的产品流程）；

4） **优惠权益** ：把通用的促销形式或优惠等价物打包成权益，如黑卡；

## 1.4，领域维护的主要数据

基于上述核心生命周期和经典流程，围绕核心领域实体，扩展并给出领域通用促销形式主要维护的数据（领域实体）：

除此之外的拼团、秒杀、众测、积分、E卡等都有自己相对较独立的领域数据。

## 1.5，领域边界（跟其他领域的关联关系）

优惠域作为一个基础领域，面向各业务线提供基础优惠能力，向下依赖商品、预算、用户等基础领域。与其他领域的边界依赖关系如下所示：

## 二、现状描述

基于上述的领域定义，梳理目前现有系统存在的优惠促销形式主要有：

<table><colgroup><col> <col> <col> <col> <col> <col> <col></colgroup><tbody><tr><th></th><th>促销形式</th><th>分类</th><th>优惠生效时机</th><th>主要提供功能</th><th>目前所属维护团队</th><th>备注</th></tr><tr><td>1</td><td>优惠券</td><td><p>通用促销形式</p><p>（优惠券）</p></td><td>交易下单</td><td><p>提供一种用户可领取、有优惠凭证，时间周期非常灵活的促销手段，支持满减/直减/折扣等不同类型的券</p><p>围绕优惠券有配券、领券、查券、校验券、核销券、退券等功能</p></td><td>优惠活动组</td><td></td></tr><tr><td>2</td><td>优惠立减</td><td><p>通用促销形式</p><p>（优惠立减）</p></td><td>交易下单</td><td><p>提供实时、所见即所享受的即时促销手段，支持满减/立减/阶梯减/折扣减等多种形式</p><p>围绕立减有立减活动配置、立减优惠展示查询、立减校验、立减核销、立减回退等功能</p></td><td>-</td><td>暂无类似的系统</td></tr><tr><td>3</td><td>返赠</td><td><p>通用促销形式</p><p>（返赠）</p></td><td>交易成功</td><td><p>提供一种购后的优惠返还或赠送的促销手段，支持虚拟物品或实物返赠</p><p>围绕返赠主要有活动配置、标签展示、资格校验、优惠返赠等功能</p></td><td>-</td><td>暂无类似的系统</td></tr><tr><td>4</td><td>赠品</td><td><p>通用促销形式二次包装</p><p>（返赠）</p></td><td>交易成功</td><td>提供购后的优惠赠送功能，目前支持赠送卡券、实物商品</td><td>优惠活动组</td><td></td></tr><tr><td>5</td><td>打折</td><td><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td><p>提供实时的折扣模式的即时优惠</p><p>围绕打折有活动配置、标签展示、打折校验、打折核销等功能</p></td><td>优惠活动组</td><td></td></tr><tr><td>6</td><td>买X（赠/送）Y</td><td><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td><p>提供一种购买多份商品额外赠送同类商品的促销手段，本质上是享受某种商品的低价大量购买</p></td><td>优惠活动组</td><td>目前系统是通过赠品来实现，但本质上来看更像是一个满X份立减至Y元的立减</td></tr><tr><td>7</td><td>拼团</td><td><p>独立优惠活动</p><p>（拼团）</p></td><td>交易下单</td><td><p>提供一种多人组团可以享受较低优惠价购买指定商品的促销手段，可拼团的有实物商品，也可以是虚拟的优惠券</p><p>围绕拼团有活动配置、拼团下单、拼团成团、拼团未成团订单取消等功能</p></td><td>优惠活动组</td><td></td></tr><tr><td>8</td><td>限时抢购</td><td><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td><p>提供一种限定时间的实时特价抢购的促销手段</p><p>围绕限时抢购有活动配置、抢购下单、优惠资格校验等功能</p></td><td>优惠活动组</td><td></td></tr><tr><td>9</td><td>秒杀</td><td><p>独立优惠活动</p><p>（秒杀）</p><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td><p>提供一种限量的商品低价促销手段</p><p>围绕秒杀有活动配置、秒杀资格校验、秒杀下单等功能</p><p>也可以看作是基于优惠立减的立减至X元形式的二次独立包装</p></td><td>优惠活动组</td><td></td></tr><tr><td>10</td><td>全网活动</td><td><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td><p>提供指定某些商品的全渠道特价促销手段</p><p>功能上类似限时抢购</p></td><td>优惠活动组</td><td></td></tr><tr><td>11</td><td>砍价</td><td><p>独立优惠活动</p><p>（砍价）</p><p>通用促销形式二次包装</p><p>（优惠券、优惠立减）</p></td><td><p>交易下单</p><p>（部分返券/权益与交易流程无关）</p></td><td><p>提供一种通过分享好友助力来最终获取优惠利益的促销手段</p><p>围绕砍价主要提供活动配置、发起砍价、帮砍、砍价下单等功能</p><p>主要核心功能在发起砍价和帮砍，砍价成功后可以是获取优惠券、权益或低价下单资格等</p></td><td>优惠活动组</td><td></td></tr><tr><td>12</td><td>助力返现</td><td><p>通用促销形式二次包装</p><p>（返赠）</p></td><td><p>交易成功</p></td><td><p>提供一种通过分享助力，好友下单自己获取返利的促销手段</p><p>围绕助力返现主要提供活动配置、发起助力返现、好友助力下单、返现发放等功能</p><p>核心功能诉求是好友助力带来交易下单行为</p><p>返现可以是返现金、优惠券、E卡等</p></td><td>优惠活动组</td><td></td></tr><tr><td>13</td><td>朋友圈返现</td><td><p>通用促销形式二次包装</p><p>（返赠）</p></td><td>交易成功</td><td><p>提供一种用户交易履约成功后朋友圈分享返现的促销手段</p><p>围绕朋友圈发现主要提供活动配置、朋友券截图上传、返现资格审核、返现优惠发放等功能</p><p>核心功能诉求是需交易履约后触发返现</p><p>返现可以是现金、E卡等</p></td><td>优惠活动组</td><td></td></tr><tr><td>14</td><td>众测</td><td><p>独立优惠活动</p><p>（众测）</p></td><td>交易下单</td><td><p>提供一种用户报名参与商品/服务享受体验并最终以一定优惠价交易成交的促销手段</p><p>围绕众测主要提供活动报名、活动体验、体验后优惠价下单等流程</p><p>核心功能点是借着用户参与众测提升产品美誉度并回馈用户优惠价下单资格</p></td><td>优惠活动组</td><td></td></tr><tr><td>15</td><td>分享红包</td><td><p>通用促销形式二次包装</p><p>（返赠、优惠券）</p></td><td>交易成功</td><td><p>提供一种用户下单成功后获取红包并分享供他人领取的促销手段</p><p>围绕分享红包主要提供下单后红包分享、红包领取等功能</p><p>分享的红包主要是优惠券</p></td><td>优惠活动组</td><td></td></tr><tr><td>16</td><td>购后返券</td><td><p>通用促销形式二次包装</p><p>（返赠、优惠券）</p></td><td>交易成功</td><td><p>提供一种交易后返券的促销手段</p></td><td>优惠活动组</td><td></td></tr><tr><td>17</td><td>积分</td><td>优惠等价物</td><td><p>支付</p><p>（部分与交易流程无关）</p></td><td><p>提供一种与现金比例兑换的等价物，可以用来交易下单时抵扣部分金额，也可用在用在一些营销活动玩法</p><p>围绕积分主要提供有积分的发放、消耗、流转等核心功能</p><p>体现在优惠层面主要是下单抵扣、兑换优惠券或相关权益等</p></td><td>大前台业务组/金融支付</td><td></td></tr><tr><td>18</td><td>E点/E卡</td><td>优惠等价物</td><td><p>支付</p><p>（部分与交易流程无关）</p></td><td><p>提供与现金比例兑换的等价物，主要用来交易下单支付时抵扣部分金额</p><p>围绕E卡有E卡的制作、发放、核销、回退等功能</p></td><td>金融支付</td><td></td></tr><tr><td>19</td><td>黑卡</td><td>权益</td><td>权益的使用一般体现在交易下单</td><td><p>主要提供一些基础的权益封装，权益包含部分服务（洗车、补胎道路救援等）免费限次享受，会员价、优惠券等</p><p>围绕黑卡有卡的制作、开通、会员等级、权益使用等功能</p><p>体现在优惠层面主要是特定会员价购买指定商品、不同优惠力度的优惠券包</p></td><td>大前台业务组</td><td></td></tr><tr><td>20</td><td>支付渠道立减</td><td><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>支付</td><td><p>提供特殊支付渠道支付时的直减/满减的优惠</p><p>主要体现在（交易前）支付环节，相对比较独立，但从促销形式上看，是优惠立减中相对比较简单的一种优惠形式</p></td><td>金融支付</td><td></td></tr><tr><td>21</td><td>车品限时包安装</td><td><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td><p>提供一种车品下单免安装费的促销形式</p><p>目前主要通过商品库来配置，有优惠配置、标签展示、下单时减免等功能</p></td><td>车品业务线</td><td></td></tr><tr><td>22</td><td>车品晒图好评返券</td><td><p>通用促销形式二次包装</p><p>（返赠）</p></td><td>交易成功</td><td><p>提供一种交易成功（到店安装/到家签收）后的评论返的促销手段</p><p>主要功能在晒图评论、运营线下返券</p><p>后续可能不仅是返券、也可以返E卡、积分、现金等</p></td><td>车品业务线</td><td></td></tr><tr><td>23</td><td>洗美套餐</td><td><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td>提供多个商品组合套餐的优惠价促销形式</td><td>洗美业务线</td><td>业界有的做法，是把套餐打包作为一种新的商品类型，纳入到商品领域来支持</td></tr><tr><td>24</td><td>洗美年卡</td><td>权益</td><td>权益的使用一般体现在交易下单</td><td><p>主要提供一些基础的权益封装，权益包含部分洗美服务（洗车、 镀膜等）免费限次享受等</p><p>体现在优惠层面主要是一次性以一个较低的优惠价购买多次服务权益（权益是通过服务码的形式来承接）</p></td><td>洗美业务线</td><td></td></tr><tr><td>25</td><td>洗美团购</td><td><p>独立优惠活动</p><p>（团购）</p><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td><p>提供一种以团购优惠价来购买指定商品或服务的促销手段</p><p>目前是在商品基础之上，通过团购活动的方式来实现，可以看作是一种独立团购优惠活动、也可以看作基于优惠立减基础之上的一种直减</p></td><td>洗美业务线</td><td rowspan="4"><p>业界有的做法，是把团购直接作为一种商品类型，纳入到商品领域来支持。<br></p><p>洗美商品展示逻辑：<br>1. 洗美门店列表页：同一商品PID，团购、限时促销和原价商品只展示一个最优价格的商品，折扣、特价和原价商品只展示一个最优价格的商品（一个门店最多展示3个商品）；<br>2. 洗美门店详情页：同一商品PID，团购和限时促销只展示一个最优价格的商品，折扣和特价只展示一个最优价格的商品，原价商品始终展示。</p></td></tr><tr><td>26</td><td>洗美限时促销</td><td><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td><p>功能同（8）限时抢购</p></td><td>洗美业务线</td></tr><tr><td>27</td><td>洗美折扣</td><td><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td>功能同（5） 打折</td><td>目前已移交给优惠活动组</td></tr><tr><td>28</td><td>洗美特价</td><td><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td><p>提供指定某些服务的特价促销手段</p><p>功能同（27）折扣，只是直接指定一个优惠价</p></td><td>目前已移交给优惠活动组</td></tr><tr><td>29</td><td>洗美立减</td><td><p>通用促销形式</p><p>（优惠立减）</p></td><td>交易下单</td><td>功能同（2）优惠立减</td><td><p>目前已移交给优惠活动组</p></td><td>（产品规划中）</td></tr><tr><td>30</td><td>保养定价</td><td><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td><p>提供指定某些服务的特价促销手段</p><p>限定了商品范围，可能包含多个项目</p><p>功能同（28）洗美特价</p></td><td>保养业务线</td><td></td></tr><tr><td>31</td><td>保养打折</td><td><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td><p>功能同（5） 打折</p><p>限定了商品范围，可能包含多个项目</p></td><td>保养业务线</td><td></td></tr><tr><td>32</td><td>保养套餐</td><td><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td>提供机油商品多个项目组合套餐的优惠价促销</td><td>保养业务线</td><td></td></tr><tr><td>33</td><td>手工优惠</td><td><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td><p>提供一种人工直接调节订单价格的优惠促销形式</p><p>主要是供客服坐席人员处理客诉相关问题时，直接调价</p><p>以往是直接改商品售价下单再恢复售价，后续通过手工优惠的形式来记录这个优惠调价信息</p><p>本质上是一种无条件的直减</p></td><td>交易订单</td><td></td></tr><tr><td>34</td><td>汽配龙满减/折扣券</td><td><p>通用促销形式</p><p>（优惠券）</p></td><td>交易下单</td><td><p>功能同（1）优惠券</p><p>有平台券、商户券</p></td><td>汽配龙</td><td></td></tr><tr><td>35</td><td>汽配龙立减券</td><td><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td><p>功能同（2）优惠立减</p><p>有平台券、商户券</p><p>尽管是券的表现形式，但不需用户领取，下单时自动抵扣</p></td><td>汽配龙</td><td>通过券上绑定的条件来筛选用户资格</td></tr><tr><td>36</td><td>汽配龙现金券</td><td><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td><p>功能同（2）优惠立减</p><p>有平台券、商户券</p><p>下单时直接抵扣部分现金（相当于无门槛直减）</p></td><td>汽配龙</td><td></td></tr><tr><td>37</td><td>汽配龙满送券</td><td><p>通用促销形式二次包装</p><p>（返赠）</p></td><td><p>交易下单核销</p><p>交易成功后赠送</p></td><td><p>功能同（3）返赠</p><p>有平台券、商户券</p><p>下单时核销，交易成功后赠送实物商品</p></td><td>汽配龙</td><td></td></tr><tr><td>38</td><td>汽配龙单品促销</td><td><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td><p>功能同（2）优惠立减</p><p>提供单个商品特价促销售卖的功能</p></td><td>汽配龙</td><td></td></tr><tr><td>39</td><td>汽配龙组合促销</td><td><p>通用促销形式二次包装</p><p>（优惠立减）</p></td><td>交易下单</td><td><p>功能类似（23）洗美套餐和（32）保养套餐</p><p>提供多个商品组合套餐的优惠价促销形式</p></td><td>汽配龙</td><td></td></tr><tr><td>40</td><td>汽配龙赠品促销</td><td><p>通用促销形式二次包装</p><p>（返赠）</p></td><td><p>交易成功后赠送</p></td><td><p>功能同（4）赠品</p><p>交易成功后赠送实物商品</p></td><td>汽配龙</td><td></td></tr><tr><td colspan="1">41</td><td colspan="1">微信卡券</td><td colspan="1"><p>通用促销形式二次包装</p><p>（优惠券）</p></td><td colspan="1"><p>外部领取</p><p>交易下单</p></td><td rowspan="2"><p>外部领取卡券（同时关联到途虎的优惠券）</p><p>交易下单时，可抵扣</p><p>核销后同步核销外部卡券</p></td><td colspan="1">优惠活动组/微信</td><td colspan="1"></td></tr><tr><td colspan="1">42</td><td colspan="1">支付宝卡券</td><td colspan="1"><p>通用促销形式二次包装</p><p>（优惠券）</p></td><td colspan="1"><p>外部领取</p><p>交易下单</p></td><td colspan="1">优惠活动组/支付宝</td><td colspan="1"></td></tr><tr><td colspan="1">43</td><td colspan="1">外部渠道优惠</td><td colspan="1">优惠等价物</td><td colspan="1"><p>外部优惠凭证</p><p>外部渠道下单</p></td><td><p>外部渠道的优惠凭证（第三方售卖渠道提供管理后台配置），</p><p>交易下单后导单到途虎交易系统后会带有优惠凭证，实际也会消耗途虎营销预算</p><p>形式多样（外部券/减/各种促销活动）</p></td><td colspan="1">淘宝/天猫/京东/拼多多</td><td colspan="1">尽管交易下单流程在外部，但在外部渠道提供的配置后台仍然可尝试关联营销预算</td></tr></tbody></table>

综合上述优惠促销形式，梳理现有逻辑架构图如下：

![](../attachments/image2020-3-9_11-15-58_b9e6a3f1.png)

具体的数据E-R图、状态图、时序图，由于各个优惠形式都各自建设有一套，这里仅简单介绍下优惠券：

优惠券E-R图

![](../attachments/image2020-2-14_10-1-3_baf2078c.png)

优惠券状态图

![](../attachments/image2020-2-14_10-24-29_4addb2fd.png)

优惠券时序图

![](../attachments/image2020-3-5_20-57-31_f81f1e8b.png)

综合梳理的现有众多优惠促销形式，主要存在以下问题：

<table><colgroup><col> <col> <col></colgroup><tbody><tr><th>序号</th><th>问题分类</th><th>问题描述</th></tr><tr><td>1</td><td rowspan="3">模型抽象<br></td><td>一些不同优惠促销形式各自都独立建设有一套，但本质上类似，缺乏抽象沉淀</td></tr><tr><td colspan="1">2</td><td colspan="1">前期为支持业务快速发展，不同的业务线都存在不同程度的优惠促销能力的重复建设</td></tr><tr><td colspan="1">3</td><td colspan="1">一些的新的业务规则，限于现有的模型，无法灵活扩展，业务支持成本偏高</td></tr><tr><td colspan="1">4</td><td rowspan="3">服务划分</td><td colspan="1">部分优惠促销形式在建设时，要么服务划分不合理，要么没有划分</td></tr><tr><td>5</td><td>面向外部不同的使用方，缺乏统一的收归，需要上游理解优惠内部的不同促销形式的业务逻辑</td></tr><tr><td colspan="1">6</td><td colspan="1">面向运营/门店等配置端，各种促销形式独立一套，没有一个统一的一站式配置界面</td></tr><tr><td colspan="1">7</td><td colspan="1">能力沉淀</td><td colspan="1">一些优惠领域内公用的能力缺乏提炼和沉淀，扩展性和支撑效率有待提升</td></tr><tr><td colspan="1">8</td><td colspan="1">非功能性设计</td><td colspan="1">现有部分优惠促销活动，在服务安全/容量/一致性方面都存在一定挑战，需要进行针对性地考量和设计</td></tr></tbody></table>

## 2.1、流程-服务-能力-数据-外部关系描述

### 2.1.1 打折

<table><colgroup><col> <col> <col> <col> <col> <col> <col> <col> <col> <col> <col></colgroup><tbody><tr><td colspan="11"><strong>打折活动核心流程</strong></td></tr><tr><th>顺序编号</th><th><p>所经系统（比较大的不准确的概念）</p></th><th colspan="1">系统所属团队</th><th>所经服务（明确准确的概念）</th><th colspan="1"><p>服务如何触发运行</p></th><th>完成了哪些功能/能力</th><th colspan="1"><p>调用了哪些服务</p><p>对方完成什么主要功能</p></th><th colspan="1"><p>读了哪些数据库/表/关键字段</p></th><th colspan="1">写了哪些数据库/表/关键字段</th><th colspan="1"><p>对外Push了哪些消息及消息内容体概述</p></th><th colspan="1"><p>下游消费者有哪些服务</p><p>消费者完成什么主要功能</p></th></tr><tr><td colspan="1">1</td><td colspan="1">打折</td><td colspan="1">优惠活动组</td><td colspan="1">优惠活动配置</td><td colspan="1">运营方配置触发</td><td colspan="1"><p><strong>优惠活动配置</strong></p><p>活动基础信息配置</p><p>选品</p><p>审核</p></td><td colspan="1"><p>途虎通消息推送服务</p></td><td colspan="1"><p><strong>数据库：SQL Service</strong></p><p><strong>库名：Activity</strong></p><p>SalePromotionActivit<br>(打折活动信息表)</p><p>SalePromotionActivityProduct</p><p>(打折活动商品信息表)</p><p>SalePromotionActivityDiscount</p><p>（打折活动规则表）</p><p><strong>库名：Tuhu_log</strong></p><p align="left">SalePromotionActivityLog</p><p>（打折活动操作日志表）</p><p align="left">SalePromotionActivityLogDetail</p><p align="left">（打折活动操作日志详情表）</p><p align="left">SalePromotionActivityLogDescription</p><p align="left">(打折活动操作日志类型表)</p></td><td colspan="1"><p><strong>数据库：SQL Service</strong></p><p><strong>库名：Activity</strong></p><p>SalePromotionActivit<br>(打折活动信息表)</p><p>SalePromotionActivityProduct</p><p>(打折活动商品信息表)</p><p>SalePromotionActivityDiscount</p><p>（打折活动规则表）</p><p><strong>库名：Tuhu_log</strong></p><p align="left">SalePromotionActivityLog</p><p>（打折活动操作日志表）</p><p align="left">SalePromotionActivityLogDetail</p><p align="left">（打折活动操作日志详情表）</p><p align="left">SalePromotionActivityLogDescription</p><p align="left">(打折活动操作日志类型表）</p></td><td colspan="1">无</td><td colspan="1">无</td></tr><tr><td>2</td><td><p>打折</p></td><td colspan="1">优惠活动组</td><td><p>折扣优惠展示</p></td><td colspan="1"><p><strong>折扣商品标签</strong></p><p>2小时定时任务 触 发预刷新，配置后台变更事实刷新;</p><p>C端（前台系统）商品列表页展示触发调用</p><p><strong>C端商品详情</strong></p><p>C端（前台系统）商品详情页展示折后价/折扣规则调用</p></td><td><p><strong>优惠活动展示</strong></p><p>标签</p><p>折后价/折后规则</p></td><td colspan="1"><p>1，通用标签（ProductMarketing）服务，获取打折标签信息</p><p>2，通用标签（ProductMarketing）服务，定时任务将打折商品活动信息预加载</p></td><td colspan="1"><p><strong>数据库：SQL Service</strong></p><p><strong>库名：Activity</strong></p><p>SalePromotionActivit<br>(打折活动信息表)</p><p>SalePromotionActivityProduct</p><p>(打折活动商品信息表)</p><p>SalePromotionActivityDiscount</p><p>（打折活动规则表）</p></td><td colspan="1"></td><td colspan="1">无</td><td colspan="1">无</td></tr><tr><td colspan="1">3</td><td colspan="1"><p>打折</p></td><td colspan="1">优惠活动组</td><td colspan="1">折扣优惠校验</td><td colspan="1"><p><strong>C端提单页</strong></p><p>C端（前台系统）调用校验用户限购与库存，根据返回信息计算展示实际折后价</p></td><td colspan="1"><p><strong>商品限购</strong></p><p>单人限购</p><p>会场限购</p><p>总库存限购</p></td><td colspan="1"></td><td colspan="1"><p><strong>数据库：SQL Service</strong></p><p><strong>库名：Activity</strong></p><p>SalePromotionActivit<br>(打折活动信息表)</p><p>SalePromotionActivityProduct</p><p>(打折活动商品信息表)</p><p>SalePromotionActivityDiscount</p><p>（打折活动规则表）</p></td><td colspan="1"></td><td colspan="1">无</td><td colspan="1">无</td></tr><tr><td colspan="1">4</td><td colspan="1">打折</td><td colspan="1">优惠活动组</td><td colspan="1">折扣优惠核销</td><td colspan="1"><p><strong>折扣活动下单</strong></p><p>C端（前台系统）调用统一活动下单接口</p><p>营销（优惠活动）触发校验用户限购与库存，核销库存</p><p>营销（优惠活动）记录折扣商品下单信息</p></td><td colspan="1"><p><strong>折扣商品下单</strong></p><p>活动信息校验</p><p>限购校验</p><p>库存核销</p><p>折扣商品下单记录</p></td><td colspan="1"></td><td colspan="1"><p><strong>数据库：SQL Service</strong></p><p><strong>库名：Activity</strong></p><p>SalePromotionActivit<br>(打折活动信息表)</p><p>SalePromotionActivityProduct</p><p>(打折活动商品信息表)</p><p>SalePromotionActivityDiscount</p><p>（打折活动规则表）</p><p>SalePromotionDiscountOrder</p><p>（打折商品下单记录表）</p></td><td colspan="1"></td><td colspan="1">无</td><td colspan="1">无</td></tr><tr><td colspan="1">5</td><td colspan="1">打折</td><td colspan="1">优惠活动组</td><td colspan="1">退单</td><td colspan="1"><p><strong>折扣商品退单</strong></p><p>营销（优惠活动）订阅订单状态变更MQ处理</p></td><td colspan="1">折扣商品退单</td><td colspan="1"></td><td colspan="1"><p><strong>数据库：SQL Service</strong></p><p><strong>库名：Activity</strong></p><p>SalePromotionDiscountOrder</p><p>（打折商品下单记录表）</p></td><td colspan="1"></td><td colspan="1">无</td><td colspan="1">无</td></tr></tbody></table>

### 2.1.2 优惠券

<table><colgroup><col> <col> <col> <col> <col> <col> <col> <col> <col> <col> <col></colgroup><tbody><tr><td colspan="11"><strong>券模板审核流程</strong></td></tr><tr><th>顺序编号</th><th><p>所经系统（比较大的不准确的概念）</p></th><th>系统所属团队</th><th>所经服务（明确准确的概念）</th><th><p>服务如何触发运行</p></th><th>完成了哪些功能/能力</th><th><p>调用了哪些服务</p><p>对方完成什么主要功能</p></th><th><p>读了哪些数据库/表/关键字段</p></th><th>写了哪些数据库/表/关键字段</th><th><p>对外Push了哪些消息及消息内容体概述</p></th><th><p>下游消费者有哪些服务</p><p>消费者完成什么主要功能</p></th></tr><tr><td>1</td><td>优惠券</td><td>优惠活动组</td><td>工单系统</td><td><ul><li>RPC：工单系统审核获取审核人信息接口【promotion服务】</li></ul></td><td>获取工单审核人的信息</td><td><p>ConfigBaseService.GetBaseConfigList</p><p>获取审核人对应关系</p></td><td><p>Activity..GetCouponRuleAudit</p><p>Configuration..PromotionBusinessLineConfig</p><p>Configuration..CouponDepartmentUseSetting</p></td><td>无</td><td>无</td><td>无</td></tr><tr><td>2</td><td>优惠券</td><td>优惠活动组</td><td>MQ</td><td><ul><li>MQ：CouponGetRuleAuditFromWorkOrder生产者是工单服务</li></ul></td><td>同步工单的信息到券规则</td><td><p>CouponGetRuleService.UpdateCouponGetRuleAuditAsync</p><p>更新券规则</p></td><td><p>Activity..GetCouponRuleAudit</p></td><td>Activity..tbl_GetCouponRules</td><td>无</td><td>无</td></tr><tr><td colspan="11"><strong>发券流程</strong></td></tr><tr><th>顺序编号</th><th><p>所经系统（比较大的不准确的概念）</p></th><th>系统所属团队</th><th>所经服务（明确准确的概念）</th><th><p>服务如何触发运行</p></th><th>完成了哪些功能/能力</th><th><p>调用了哪些服务</p><p>对方完成什么主要功能</p></th><th><p>读了哪些数据库/表/关键字段</p></th><th>写了哪些数据库/表/关键字段</th><th><p>对外Push了哪些消息及消息内容体概述</p></th><th><p>下游消费者有哪些服务</p><p>消费者完成什么主要功能</p></th></tr><tr><td>1</td><td>优惠券</td><td>优惠活动组</td><td>配置后台【如砍价，拼团，返券】</td><td><ul><li>RPC调用：活动，砍价，拼团等配置后台</li></ul></td><td>投放：获取券模板信息</td><td>CreatePromotionService.GetCouponRulesByRuleGuidAsync</td><td><p>Activity..tbl_GetCouponRules</p><p>Activity..tbl_CouponRules</p></td><td>无</td><td>无</td><td>无</td></tr><tr><td>2</td><td>优惠券</td><td>优惠活动组</td><td><p>api</p><p>MQ</p><p>job</p></td><td><ul><li>RPC调用：活动，返券，三方卡券等服务</li><li>实时返券MQ，优惠券任务MQ等</li><li>运营job等</li></ul></td><td><p>领券</p><p>发券</p></td><td>CreatePromotionService.CreatePromotionNew</td><td><p>Activity..tbl_GetCouponRules</p></td><td><p>Gungnir..tbl_PromotionCode</p><p>Gungnir..tbl_PromotionCodeSell</p><p>Activity..tbl_GetCouponRules</p><p>Tuhu_log..PromotionOprLog</p></td><td><p>MQ：MKT.Coupon.CreateCouponSuccessBusiness</p><p>记录日志,更新库存,拼团价格</p></td><td><p>无</p></td></tr><tr><td colspan="11"><strong>用券流程</strong></td></tr><tr><th>顺序编号</th><th><p>所经系统（比较大的不准确的概念）</p></th><th>系统所属团队</th><th>所经服务（明确准确的概念）</th><th><p>服务如何触发运行</p></th><th>完成了哪些功能/能力</th><th><p>调用了哪些服务</p><p>对方完成什么主要功能</p></th><th><p>读了哪些数据库/表/关键字段</p></th><th>写了哪些数据库/表/关键字段</th><th><p>对外Push了哪些消息及消息内容体概述</p></th><th><p>下游消费者有哪些服务</p><p>消费者完成什么主要功能</p></th></tr><tr><td>1</td><td>优惠券</td><td>优惠活动组</td><td>api</td><td><ul><li>RPC：api，客服系统</li></ul></td><td><p>提单页：获取下单优惠券列表页</p></td><td><p>Member服务</p><p>SelectPromotionCodeByUserIdForOrderAsync<br></p></td><td><p>Gungnir..tbl_PromotionCode</p><p>Activity..tbl_GetCouponRules</p><p>Activity..tbl_CouponRules</p><p>Activity..tbl_CouponRules_ConfigProduct</p><p>Activity..tbl_CouponRules_ConfigShop</p><p>Activity..CouponRulesOrderConfig</p></td><td>无</td><td>无</td><td><p>产品服务</p><p>门店服务</p><p>订单服务</p><p>节假日服务</p></td></tr><tr><td>2</td><td>优惠券</td><td>优惠活动组</td><td><p>api</p><p>MQ</p><p>job</p></td><td><ul><li>RPC：api，客服系统</li></ul></td><td>下单页：检验用户所选优惠券是否可用</td><td><p>Member服务</p><p>PromotionCodeVerifyAsync</p></td><td><p>Gungnir..tbl_PromotionCode</p><p>Activity..tbl_GetCouponRules</p><p>Activity..tbl_CouponRules</p><p>Activity..tbl_CouponRules_ConfigProduct</p><p>Activity..tbl_CouponRules_ConfigShop</p><p>Activity..CouponRulesOrderConfig</p></td><td>无</td><td>无</td><td><p>产品服务</p><p>门店服务</p><p>订单服务</p><p>节假日服务</p></td></tr><tr><td>3</td><td>优惠券</td><td>优惠活动组</td><td>订单服务</td><td><ul><li>RPC：订单服务</li></ul></td><td>下单:获取优惠券类型已便计算价格</td><td><p>Member服务</p><p>GetPromotionIsPaidTypeAsync</p></td><td><p>Gungnir..tbl_PromotionCode</p><p>Activity..tbl_GetCouponRules</p><p>Activity..tbl_CouponRules</p></td><td>无</td><td>无</td><td>无</td></tr><tr><td>4</td><td>优惠券</td><td>优惠活动组</td><td>订单服务</td><td><ul><li>RPC：订单服务</li></ul></td><td>下单完成：核销优惠券</td><td><p>Member服务</p><p>UpdateUserPromotionCodeStatus</p></td><td>Gungnir..tbl_PromotionCode</td><td><p>Gungnir..tbl_PromotionCode</p><p>Tuhu_log..PromotionOprLog</p></td><td><p>如果是三方卡券：会发送MQ</p><p>核销三方卡券</p></td><td>三方卡券服务</td></tr><tr><td>5</td><td>优惠券</td><td>优惠活动组</td><td>订单服务</td><td><ul><li>RPC：订单服务</li></ul></td><td>取消订单：回退优惠券</td><td><p>Member服务</p><p>ReleasePromtionByOrderIdAsync</p></td><td>Gungnir..tbl_PromotionCode</td><td><p>Gungnir..tbl_PromotionCode</p><p>Tuhu_log..PromotionOprLog</p></td><td>无</td><td>无</td></tr><tr><td>6</td><td>优惠券</td><td>优惠活动组</td><td>订单服务</td><td><ul><li>RPC：订单服务</li></ul></td><td>红冲订单：复制优惠券</td><td><p>Member服务</p><p>CopyPromotionCodeAsync</p></td><td>Gungnir..tbl_PromotionCode</td><td><p>Gungnir..tbl_PromotionCode</p><p>Tuhu_log..PromotionOprLog</p></td><td>无</td><td>无</td></tr></tbody></table>

### 2.13 拼团

<table><colgroup><col> <col> <col> <col> <col> <col> <col> <col> <col> <col> <col></colgroup><tbody><tr><td colspan="11"><strong><strong>拼团开团服务列表</strong></strong></td></tr><tr><th>顺序编号</th><th><p>所经系统（比较大的不准确的概念）</p></th><th colspan="1">系统所属团队</th><th>所经服务（明确准确的概念）</th><th colspan="1"><p>服务如何触发运行</p></th><th>完成了哪些功能/能力</th><th colspan="1"><p>调用了哪些服务</p><p>对方完成什么主要功能</p></th><th colspan="1"><p>读了哪些数据库/表/关键字段</p></th><th colspan="1">写了哪些数据库/表/关键字段</th><th colspan="1"><p>对外Push了哪些消息及消息内容体概述</p></th><th colspan="1"><p>下游消费者有哪些服务</p><p>消费者完成什么主要功能</p></th></tr><tr><td rowspan="5">1<br></td><td rowspan="5">拼团系统<br></td><td rowspan="5">优惠活动组<br></td><td colspan="1">CheckGroupInfoByUserIdAsync（校验用户开团资格）</td><td colspan="1">WCF调用， <a href="https://elk.tuhu.cn/goto/26bbe65cc9a1ce0fdc9a5a02dd4f1b41">ELK链接</a></td><td colspan="1">校验产品库是否下架，是否已达限购单数，是否已抢完</td><td colspan="1">1，SelectProductAsync，查询产品信息</td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td>IncreaseSoldCountAsync（增加产品已售出数量）</td><td colspan="1"><p>WCF调用， <a href="https://elk.tuhu.cn/goto/469389f215a0b49f65c1f3d5cb4f5955">ELK链接</a></p></td><td><p>增加产品售出数量，同步Redis计数器</p></td><td colspan="1"></td><td rowspan="4"><p>Configuration库：</p><p>GroupBuyingProductConfig表</p><p>GroupBuyingProductGroupConfig表<br></p><p>Activity库：</p><p>tbl_GroupBuyingUserInfo表</p><p>tbl_GroupBuyingInfo表</p></td><td rowspan="4"><p>Activity库：</p><p>tbl_GroupBuyingUserInfo表</p><p>tbl_GroupBuyingInfo表</p></td><td colspan="1">notification.PinTuanProductStatusSyncQueue，库存到达上限的产品</td><td colspan="1">默认产品下架，非默认产品不显示</td></tr><tr><td colspan="1">CreateGroupBuyingAsync（用户创建新团）</td><td colspan="1">WCF调用， <a href="https://elk.tuhu.cn/goto/9cd40b1dd3d2b2dc69692fb7e6f8162e">ELK链接</a></td><td colspan="1">创建用户团信息和拼团订单</td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">ChangeGroupBuyingStatusAsync（团长付款改团状态）</td><td rowspan="2">MQ调用，notification.OrderGiftRecord（Pay服务）</td><td colspan="1">用户团状态更改为拼团中</td><td colspan="1"><p>1，CancelOrderForApp，更改团状态失败取消订单</p></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">ChangeUserStatusAsync（更改团长订单状态）</td><td colspan="1">订单状态更改为拼团中，推送开团成功消息</td><td colspan="1">1，CancelOrderForApp，更改订单状态失败取消订单</td><td colspan="1"></td><td colspan="1"></td></tr></tbody></table>

<table><colgroup><col> <col> <col> <col> <col> <col> <col> <col> <col> <col> <col></colgroup><tbody><tr><td colspan="11"><strong><strong>拼团参团服务列表</strong></strong></td></tr><tr><th>顺序编号</th><th><p>所经系统（比较大的不准确的概念）</p></th><th colspan="1">系统所属团队</th><th>所经服务（明确准确的概念）</th><th colspan="1"><p>服务如何触发运行</p></th><th>完成了哪些功能/能力</th><th colspan="1"><p>调用了哪些服务</p><p>对方完成什么主要功能</p></th><th colspan="1"><p>读了哪些数据库/表/关键字段</p></th><th colspan="1">写了哪些数据库/表/关键字段</th><th colspan="1"><p>对外Push了哪些消息及消息内容体概述</p></th><th colspan="1"><p>下游消费者有哪些服务</p><p>消费者完成什么主要功能</p></th></tr><tr><td rowspan="5">1<br></td><td rowspan="5">拼团系统<br></td><td rowspan="5">优惠活动组<br></td><td colspan="1">CheckNewUserAsync（校验新人）</td><td colspan="1">WCF调用， <a href="https://elk.tuhu.cn/goto/2ecb31f9e17c2bc91205b7e5295fe90d">ELK链接</a></td><td colspan="1">校验用户下单数量是否大于0（新人团）</td><td colspan="1">1，UserProfile——>GetAsync，获取用户下单量</td><td rowspan="5"><p>Configuration库：</p><p>GroupBuyingProductConfig表</p><p>GroupBuyingProductGroupConfig表<br></p><p>Activity库：</p><p>tbl_GroupBuyingUserInfo表</p><p>tbl_GroupBuyingInfo表</p></td><td rowspan="5"><p>Activity库：</p><p>tbl_GroupBuyingUserInfo表</p><p>tbl_GroupBuyingInfo表</p><p>tbl_GroupBuyingFreeCoupons表</p></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">CheckGroupInfoByUserIdAsync（校验用户参团资格）</td><td colspan="1">WCF调用， <a href="https://elk.tuhu.cn/goto/26bbe65cc9a1ce0fdc9a5a02dd4f1b41">ELK链接</a></td><td colspan="1">校验产品库是否下架，用户是否已参团，团状态是否已拼团成功，是否已达限购单数，是否已抢完</td><td colspan="1">1，SelectProductAsync，查询产品信息</td><td colspan="1"></td><td colspan="1"></td></tr><tr><td>IncreaseSoldCountAsync（增加产品已售出数量）</td><td colspan="1"><p>WCF调用， <a href="https://elk.tuhu.cn/goto/469389f215a0b49f65c1f3d5cb4f5955">ELK链接</a></p></td><td><p>增加产品售出数量，同步Redis计数器</p></td><td colspan="1"></td><td colspan="1">notification.PinTuanProductStatusSyncQueue，库存到达上限的产品</td><td colspan="1">默认产品下架，非默认产品不显示</td></tr><tr><td colspan="1">TakePartInGroupBuyingAsync（用户参与拼团）</td><td colspan="1">WCF调用， <a href="https://elk.tuhu.cn/goto/7f98e57cb0826b40aa9094377595709f">ELK链接</a></td><td colspan="1">创建用户拼团订单</td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">ChangeUserStatusAsync（更改团员订单状态）</td><td>MQ调用，notification.OrderGiftRecord（Pay服务）</td><td colspan="1">订单状态更改为拼团中；如果参团人数等于成团人数，则参团成功，将所有订单改为拼团成功；发放团长免单券；优惠券团发放优惠券；推送参团/拼团成功消息</td><td colspan="1"><p>1，CancelOrderForApp，更改订单状态失败取消订单</p><p>2、FetchOrderByOrderIdAsync，获取订单信息</p><p>3、 ExecuteOrderProcessAsync，设置订单流程为拼团成功</p></td><td colspan="1">notification.GroupBuyingCreateCouponQueue，优惠券团信息</td><td colspan="1">优惠券团发放优惠券</td></tr></tbody></table>

<table><colgroup><col> <col> <col> <col> <col> <col> <col> <col> <col> <col> <col></colgroup><tbody><tr><td colspan="11"><strong><strong>拼团取消订单服务列表</strong></strong></td></tr><tr><th>顺序编号</th><th><p>所经系统（比较大的不准确的概念）</p></th><th colspan="1">系统所属团队</th><th>所经服务（明确准确的概念）</th><th colspan="1"><p>服务如何触发运行</p></th><th>完成了哪些功能/能力</th><th colspan="1"><p>调用了哪些服务</p><p>对方完成什么主要功能</p></th><th colspan="1"><p>读了哪些数据库/表/关键字段</p></th><th colspan="1">写了哪些数据库/表/关键字段</th><th colspan="1"><p>对外Push了哪些消息及消息内容体概述</p></th><th colspan="1"><p>下游消费者有哪些服务</p><p>消费者完成什么主要功能</p></th></tr><tr><td rowspan="2">1<br></td><td rowspan="2">拼团系统<br></td><td rowspan="2">优惠活动组<br></td><td>CancelGroupBuyingOrderAsync（取消拼团订单）</td><td colspan="1"><p>WCF调用， <a href="https://elk.tuhu.cn/goto/c75e29c186aae295b5335ea4987bec17">ELK链接</a></p></td><td><p>拼团订单取消；减少参团人数；团长取消订单将团状态改为拼团失败，并减少已开团数，释放团长免单券</p></td><td colspan="1"><p>1，CancelOrderForApp，取消实际订单</p></td><td rowspan="2"><p>Configuration库：</p><p>GroupBuyingProductConfig表</p><p>GroupBuyingProductGroupConfig表<br></p><p>Activity库：</p><p>tbl_GroupBuyingUserInfo表</p><p>tbl_GroupBuyingInfo表</p></td><td rowspan="2"><p>Configuration库：</p><p>GroupBuyingProductGroupConfig表</p><p>Activity库：</p><p>tbl_GroupBuyingUserInfo表</p><p>tbl_GroupBuyingInfo表</p><p>tbl_GroupBuyingFreeCoupons表</p></td><td colspan="1">notification.PinTuanProductStatusSyncQueue，库存到达上限的产品</td><td colspan="1">默认产品下架，非默认产品不显示</td></tr><tr><td colspan="1">DecrementSoldCountAsync（减少产品已售出数量）</td><td colspan="1">内部调用，CancelGroupBuyingOrderAsync</td><td colspan="1">增加拼团产品虚拟库存；同步拼团产品状态</td><td colspan="1"></td><td colspan="1">notification.PinTuanProductStatusSyncQueue，库存恢复的产品</td><td colspan="1">展示非默认产品</td></tr></tbody></table>

### 2.1.4 赠品

<table><colgroup><col> <col> <col> <col> <col> <col> <col> <col> <col> <col> <col></colgroup><tbody><tr><td colspan="11"><strong><strong>赠品核心流程服务列表</strong></strong></td></tr><tr><th>顺序编号</th><th><p>所经系统（比较大的不准确的概念）</p></th><th colspan="1">系统所属团队</th><th>所经服务（明确准确的概念）</th><th colspan="1"><p>服务如何触发运行</p></th><th>完成了哪些功能/能力</th><th colspan="1"><p>调用了哪些服务</p><p>对方完成什么主要功能</p></th><th colspan="1"><p>读了哪些数据库/表/关键字段</p></th><th colspan="1">写了哪些数据库/表/关键字段</th><th colspan="1"><p>对外Push了哪些消息及消息内容体概述</p></th><th colspan="1"><p>下游消费者有哪些服务</p><p>消费者完成什么主要功能</p></th></tr><tr><td rowspan="5">1<br></td><td rowspan="5">赠品系统<br></td><td rowspan="5">优惠活动组<br></td><td>SelectProductGiftsAsync（产品详情页赠品接口）</td><td colspan="1"><p>WCF调用， <a href="https://elk.tuhu.cn/goto/65afb1a2873cb48378994716b577e98d">ELK链接</a></p></td><td>产品详情页查询赠品描述</td><td colspan="1"><p>1，SelectSkuProductListByPidsAsync，获取产品信息</p><p>2，searchPrice服务，查询买三送一价</p></td><td colspan="1"><p>Configuration库SE_GiftManageConfig表</p></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">SelectOrderGiftsForCResponseAsync（C端下单赠品接口）</td><td colspan="1">WCF调用， <a href="https://elk.tuhu.cn/goto/56562e588fc1470e899dea77254c7535">ELK链接</a></td><td colspan="1">C端下单时匹配赠送赠品</td><td colspan="1"><p>1，SelectSkuProductListByPidsAsync，获取产品信息</p><p>2，searchPrice服务，查询买三送一价</p></td><td colspan="1">Configuration库SE_GiftManageConfig表</td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">SelectProductDetailGiftsForByAsync（保养查询赠品接口）</td><td colspan="1">WCF调用， <a href="https://elk.tuhu.cn/goto/7cd84428e91ecfba333767a022c5e4c7">ELK链接</a></td><td colspan="1">保养详情页查询赠品描述</td><td colspan="1"></td><td colspan="1">Configuration库SE_GiftManageConfig表</td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">RecordGiftSendInfoLogAsync（记录赠品送出情况）</td><td colspan="1"><p>MQ调用，notification.OrderGiftRecord（业务系统），</p><p>CL.Gift.UpdateGiftStockWhenOrderCanceledQueue（监控订单）</p></td><td colspan="1">赠品下单/取消订单记录送出/退回</td><td colspan="1"></td><td colspan="1"></td><td colspan="1">Tuhu_log库RecordGiftSendInfoLog表</td><td colspan="1">notification.RefreshGiftSoldOutCacheConsumer，库存售罄/退回的赠品规则</td><td colspan="1">库存售罄/退回刷新牛皮藓缓存</td></tr><tr><td colspan="1">GetProductGiftPictureListAsync（获取产品赠品图片）</td><td colspan="1">WCF调用， <a href="https://elk.tuhu.cn/goto/861b30f919da5b1e3df76d2202996ad8">ELK链接</a></td><td colspan="1">产品详情/列表页获取赠品图片</td><td colspan="1"><p>1，SelectSkuProductListByPidsAsync，获取产品信息</p><p>2，searchPrice服务，查询买三送一价</p></td><td colspan="1">Configuration库SE_GiftManageConfig表</td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr></tbody></table>

### 2.1.5 助力返现

<table><colgroup><col> <col> <col> <col> <col> <col> <col> <col> <col> <col> <col></colgroup><tbody><tr><td colspan="11"><strong>订单返现助力核心流程</strong></td></tr><tr><th>顺序编号</th><th><p>所经系统（比较大的不准确的概念）</p></th><th>系统所属团队</th><th>所经服务（明确准确的概念）</th><th><p>服务如何触发运行</p></th><th>完成了哪些功能/能力</th><th><p>调用了哪些服务</p><p>对方完成什么主要功能</p></th><th><p>读了哪些数据库/表/关键字段</p></th><th>写了哪些数据库/表/关键字段</th><th><p>对外Push了哪些消息及消息内容体概述</p></th><th><p>下游消费者有哪些服务</p><p>消费者完成什么主要功能</p></th></tr><tr><td>1</td><td>订单返现</td><td>优惠活动组</td><td>返现规则配置</td><td><p>yunying.tuhu.cn</p><p>运营人员配置</p></td><td><p>业务线区分创建不同返现规则</p><p>支持紧急禁用禁止发起</p></td><td></td><td><p><strong>数据库：SQL Service</strong></p><p><strong>库名：Activity</strong></p><p>OrderCashBackConfig</p><p>(订单返现助力配置主表)</p><p>OrderCashBackConfigRule</p><p>(返现助力配置规则表)</p><p>OrderCashBackGlobalConfig</p><p>（返现助力全局配置）</p></td><td><p><strong>数据库：SQL Service</strong></p><p><strong>库名：Activity</strong></p><p>OrderCashBackConfig</p><p>(订单返现助力配置主表)</p><p>OrderCashBackConfigRule</p><p>(返现助力配置规则表)</p><p>OrderCashBackGlobalConfig</p><p>（返现助力全局配置）</p></td><td>无</td><td>无</td></tr><tr><td>2</td><td>订单返现</td><td>优惠活动组</td><td>开启助力</td><td>C端（前台系统） 下单成功触发</td><td><p>校验订单是开启助力资格</p></td><td><p>OrderQueryClient 订单服务</p><p>查询拆单信息</p><p>OrderApiForCClient 订单服务</p><p>订单基础信息</p></td><td><p><strong>数据库：SQL Service</strong></p><p><strong>库名：Activity</strong></p><p>OrderCashBackConfig</p><p>(订单返现助力配置主表)</p><p>OrderCashBackConfigRule</p><p>(返现助力配置规则表)</p></td><td><p><strong>数据库：SQL Service</strong></p><p><strong>库名：Activity</strong></p><p>OrderCashBackOwner</p><p>（返现助力发起记录表）</p></td><td>无</td><td>无</td></tr><tr><td colspan="1">3</td><td colspan="1">订单返现</td><td colspan="1">优惠活动组</td><td colspan="1">邀请助力</td><td colspan="1">C端（前台系统） 分享后小程序触发</td><td colspan="1"><p>分享</p><p>助力金额等信息展示</p><p>拉新助力</p></td><td colspan="1"><p>UserAccountClient 用户服务</p><p>查询用户基础信息</p></td><td colspan="1"><p><strong>数据库：SQL Service</strong></p><p><strong>库名：Activity</strong></p><p>OrderCashBackOwner</p><p>（返现助力发起记录表）</p></td><td colspan="1"><p><strong>数据库：SQL Service</strong></p><p><strong>库名：Activity</strong></p><p>OrderCashBackShare</p><p>(返现助力帮忙助力记录表)</p></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">4</td><td colspan="1">订单返现</td><td colspan="1">优惠活动组</td><td colspan="1">返现</td><td colspan="1"><p>1、助力满时 发送MQ消息（notification.OrderCashBack.SupportComplete）消费者 进行验证和返现</p><p>2、订阅 订单状态流转MQ消息（#.OrderTrackingLog.#）订单状态已完成时进行验证和返现</p></td><td colspan="1"><p>幂等校验返现</p></td><td colspan="1"><p>PayClient C端统一支付服务</p><p>返现</p><p>PushApiClient 推送服务</p><p>返现成功消息推送</p><p>金融支付服务</p></td><td colspan="1"><p><strong>数据库：SQL Service</strong></p><p><strong>库名：Activity</strong></p><p>OrderCashBackOwner</p><p>（返现助力发起记录表）</p></td><td colspan="1"><p><strong>数据库：SQL Service</strong></p><p><strong>库名：Activity</strong></p><p>OrderCashBackOwner</p><p>（返现助力发起记录表）</p><p><strong>库名：Activity</strong></p><p>WxSendRedBagLog</p><p>(支付记录表)</p></td><td colspan="1"><p>名称：</p><p>notification.OrderCashBack.SupportComplete</p><p>字段：订单号，是否完成</p></td><td colspan="1"><p>1、完成助力时调用返现服务。</p><p>2、订单状态完成时调用返现服务。</p></td></tr><tr><td colspan="1">5</td><td colspan="1">订单返现</td><td colspan="1">优惠活动组</td><td colspan="1">取消助力</td><td colspan="1">订阅 订单状态流转MQ消息（#.OrderTrackingLog.#）订单状态取消时，作废返现申请</td><td colspan="1">关联取消订单，强制作废返现申请</td><td colspan="1"><p>PushApiClient 推送服务</p><p>助力失败消息推送</p></td><td colspan="1"></td><td colspan="1"><p><strong>数据库：SQL Service</strong></p><p><strong>库名：Activity</strong></p><p>OrderCashBackOwner</p><p>（返现助力发起记录表）</p></td><td colspan="1"></td><td colspan="1">订单状态取消时，调用返现服务进行返现申请作废</td></tr></tbody></table>

### 2.1.6 洗美活动

<table><colgroup><col> <col> <col> <col> <col> <col> <col> <col> <col> <col> <col></colgroup><tbody><tr><td colspan="11"><strong>洗美活动-平台活动创建/更新流程</strong></td></tr><tr><th>顺序编号</th><th>所经系统（比较大的不准确的概念）</th><th colspan="1">系统所属团队</th><th>所经服务（明确准确的概念）</th><th colspan="1">服务如何触发运行</th><th>完成了哪些功能/能力</th><th colspan="1"><p>调用了哪些服务</p><p>对方完成什么主要功能</p></th><th colspan="1"><p>读了哪些数据库/表/关键字段</p></th><th colspan="1">写了哪些数据库/表/关键字段</th><th colspan="1"><p>对外Push了哪些消息及消息内容体概述</p></th><th colspan="1"><p>下游消费者有哪些服务</p><p>消费者完成什么主要功能</p></th></tr><tr><td colspan="1">1</td><td colspan="1">平台活动服务</td><td colspan="1"></td><td colspan="1">平台活动服务</td><td colspan="1">RPC调用</td><td colspan="1">创建平台活动，处理补贴配置</td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td>2</td><td><p>洗美活动</p></td><td colspan="1"><p>洗美活动组</p></td><td>洗美优惠活动服务</td><td colspan="1"><p>RPC调用</p></td><td>洗美活动创建，更新</td><td colspan="1"><p>平台活动创建返回创建结果</p></td><td colspan="1"><p>beauty_activity</p><p>beauty_activity_detail</p></td><td colspan="1"></td><td colspan="1">发送刷新缓存消息</td><td colspan="1">消费消息刷新活动缓存</td></tr><tr><td colspan="1">3</td><td colspan="1">缓存刷新服务</td><td colspan="1">洗美活动组</td><td colspan="1">洗美活动缓存刷新MQ消费者</td><td colspan="1">RabbitMQ消息</td><td colspan="1">消费消息调用接口刷新缓存</td><td colspan="1">调用洗美主服务，活动缓存刷新</td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">4</td><td colspan="1">洗美主服务</td><td colspan="1">洗美活动组</td><td colspan="1">洗美活动缓存刷新服务</td><td colspan="1">RPC调用</td><td colspan="1">洗美活动缓存刷新</td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr></tbody></table>

<table><colgroup><col> <col> <col> <col> <col> <col> <col> <col> <col> <col> <col></colgroup><tbody><tr><td colspan="11"><strong>洗美活动-平台活动报名流程</strong></td></tr><tr><th>顺序编号</th><th>所经系统（比较大的不准确的概念）</th><th>系统所属团队</th><th>所经服务（明确准确的概念）</th><th>服务如何触发运行</th><th>完成了哪些功能/能力</th><th><p>调用了哪些服务</p><p>对方完成什么主要功能</p></th><th><p>读了哪些数据库/表/关键字段</p></th><th>写了哪些数据库/表/关键字段</th><th><p>对外Push了哪些消息及消息内容体概述</p></th><th><p>下游消费者有哪些服务</p><p>消费者完成什么主要功能</p></th></tr><tr><td>1</td><td><p>洗美优惠活动服务</p></td><td><p>洗美活动组</p></td><td>洗美优惠活动服务</td><td><p>RPC调用</p></td><td>平台活动报名</td><td><p>活动报名，返回报名结果</p></td><td><p>beauty_activity</p><p>beauty_activity_detail</p></td><td></td><td></td><td></td></tr><tr><td>2</td><td>缓存刷新服务</td><td>洗美活动组</td><td>洗美活动缓存刷新MQ消费者</td><td>RabbitMQ消息</td><td>消费消息调用接口刷新缓存</td><td>调用洗美主服务，活动缓存刷新</td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>洗美主服务</td><td>洗美活动组</td><td>洗美活动缓存刷新服务</td><td>RPC调用</td><td>洗美活动缓存刷新</td><td>活动缓存刷新</td><td></td><td></td><td></td><td></td></tr></tbody></table>

<table><colgroup><col> <col> <col> <col> <col> <col> <col> <col> <col> <col> <col></colgroup><tbody><tr><td colspan="11"><strong>洗美活动-门店活动创建/更新流程</strong></td></tr><tr><th>顺序编号</th><th>所经系统（比较大的不准确的概念）</th><th>系统所属团队</th><th>所经服务（明确准确的概念）</th><th>服务如何触发运行</th><th>完成了哪些功能/能力</th><th><p>调用了哪些服务</p><p>对方完成什么主要功能</p></th><th><p>读了哪些数据库/表/关键字段</p></th><th>写了哪些数据库/表/关键字段</th><th><p>对外Push了哪些消息及消息内容体概述</p></th><th><p>下游消费者有哪些服务</p><p>消费者完成什么主要功能</p></th></tr><tr><td>1</td><td><p>洗美优惠活动服务</p></td><td><p>洗美活动组</p></td><td>洗美优惠活动服务</td><td><p>RPC调用</p></td><td>门店活动创建，更新</td><td><p>活动报名，返回报名结果</p></td><td><p>beauty_activity</p><p>beauty_activity_detail</p></td><td></td><td></td><td></td></tr><tr><td>2</td><td>缓存刷新服务</td><td>洗美活动组</td><td>洗美活动缓存刷新MQ消费者</td><td>RabbitMQ消息</td><td>消费消息调用接口刷新缓存</td><td>调用洗美主服务，活动缓存刷新</td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>洗美主服务</td><td>洗美活动组</td><td>洗美活动缓存刷新服务</td><td>RPC调用</td><td>洗美活动缓存刷新</td><td>活动缓存刷新</td><td></td><td></td><td></td><td></td></tr></tbody></table>

<table><colgroup><col> <col> <col> <col> <col> <col> <col> <col> <col> <col> <col></colgroup><tbody><tr><td colspan="11"><strong>洗美活动-下单流程</strong></td></tr><tr><th>顺序编号</th><th>所经系统（比较大的不准确的概念）</th><th colspan="1">系统所属团队</th><th>所经服务（明确准确的概念）</th><th colspan="1">服务如何触发运行</th><th>完成了哪些功能/能力</th><th colspan="1"><p>调用了哪些服务</p><p>对方完成什么主要功能</p></th><th colspan="1"><p>读了哪些数据库/表/关键字段</p></th><th colspan="1">写了哪些数据库/表/关键字段</th><th colspan="1"><p>对外Push了哪些消息及消息内容体概述</p></th><th colspan="1"><p>下游消费者有哪些服务</p><p>消费者完成什么主要功能</p></th></tr><tr><td>1</td><td><p>洗美主服务</p></td><td colspan="1"><p>洗美活动组</p></td><td>洗美优惠活动服务</td><td colspan="1"><p>RPC调用</p></td><td>限购验证，更新下单记录</td><td colspan="1"><p>平台服务，平台活动状态验证</p><p>订单服务，创建订单</p></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">2</td><td colspan="1">平台活动</td><td colspan="1">门店组</td><td colspan="1">平台活动服务</td><td colspan="1">RPC调用</td><td colspan="1">平台活动状态验证</td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">3</td><td colspan="1">订单服务</td><td colspan="1">订单组</td><td colspan="1">订单服务</td><td colspan="1">RPC调用</td><td colspan="1">创建订单</td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr></tbody></table>

<table><colgroup><col> <col> <col> <col> <col> <col> <col> <col> <col> <col> <col></colgroup><tbody><tr><td colspan="11"><strong>不在经典流程中的服务列表</strong></td></tr><tr><th>顺序编号</th><th>所经系统（比较大的不准确的概念）</th><th colspan="1">系统所属团队</th><th>所经服务（明确准确的概念）</th><th colspan="1">服务如何触发运行</th><th>完成了哪些功能/能力</th><th colspan="1"><p>调用了哪些服务</p><p>对方完成什么主要功能</p></th><th colspan="1"><p>读了哪些数据库/表/关键字段</p></th><th colspan="1">写了哪些数据库/表/关键字段</th><th colspan="1"><p>对外Push了哪些消息及消息内容体概述</p></th><th colspan="1"><p>下游消费者有哪些服务</p><p>消费者完成什么主要功能</p></th></tr><tr><td>1</td><td>xx系统</td><td colspan="1">xx组</td><td>xx服务</td><td colspan="1"><p>RPC调用/MQ消息/定时任务</p><p>如是RPC，是哪个接口，那个服务调用它</p><p>如是MQ消息，是哪个消息，生产者是那个服务</p><p>如是定时任务，间隔多长时间</p></td><td>完成了xx功能，关键细节描述清楚</td><td colspan="1"><p>1，xxx服务，获取xx信息</p><p>2，yyy服务，操作xxx</p></td><td colspan="1"><p>xxDB/xx表，主要字段：订单id，用户id</p></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">2</td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">3</td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr></tbody></table>

## 2.2、现有逻辑架构图

### 2.2.1 打折

![](../attachments/打折逻辑架构图_34b91b27.jpg)

### 2.2.2 优惠券

![](../attachments/image2020-2-14_17-45-35_8439d1e9.png)

### 2.2.3 拼团

![](../attachments/拼团架构图_922a46f3.jpg)

### 2.2.4 赠品

![](../attachments/赠品架构图_00149a86.jpg)

### 2.2.5 订单返现助力

![](../attachments/订单返现逻辑架构图_623d8dcc.jpg)

### 2.2.6 洗美活动

![](../attachments/image2019-11-13_16-11-45_a120510e.png)

## 2.3、现有状态机

### 2.3.1 打折

![](../attachments/打折核心流程状态机_3ef6bbbd.jpg)

### 2.3.2 优惠券

![](../attachments/image2020-2-14_10-24-29_4addb2fd.png)

### 2.3.3 拼团

![](../attachments/拼团状态机_6fb9511c.jpg)

### 2.3.4 订单返现助力

![](../attachments/订单返现核心流程状态机_4d9e40af.jpg)

## 2.4、现有数据ER图

### 2.4.1 打折

![](../attachments/打折活动数据ER图_3592cb32.jpg)

### 2.4.2 优惠券

![](../attachments/image2020-2-14_10-1-3_baf2078c.png)

### 2.4.3 拼团

![](../attachments/企业微信截图_20200214142812_e3926a14.png)

### 2.4.4 赠品

![](../attachments/企业微信截图_20200213231640_340a5b70.png)

### 2.4.5 订单返现助力

![](../attachments/订单返现助力ER图_58dca927.jpg)

### 2.4.6 洗美活动

![](../attachments/image2020-2-14_18-33-7_4d9099be.png)

## 2.5、典型业务流程时序图

### 2.5.1 打折

![](../attachments/打折核心流程时序图_1ab5031e.jpg)

### 2.5.2 优惠券

![](../attachments/image2020-3-5_20-55-39_44927b82.png)

### 2.5.3 拼团

![](../attachments/拼团流程时序图_4bf8a5cd.jpg)

### 2.5.4 赠品

![](../attachments/赠品流程时序图_1cdb95fc.jpg)

### 2.5.5 订单返现助力

![](../attachments/返现助力核心时序图_9d34fb04.jpg)

### 2.5.6 洗美活动

**1）平台活动时序图**

![](../attachments/image2019-11-13_14-21-55_4906cdde.png)

**2）门店活动时序图**

![](../attachments/image2019-11-13_14-56-21_96880b42.png)

**3）洗美产品和标签查询**

![](../attachments/image2019-11-13_14-12-29_c0a5aa33.png)

**4）下单流程时序图**

![](../attachments/image2019-11-13_14-6-38_e92252df.png)

## 三、领域统一的路径

暂不需要新系统的详细设计，但是对统一路径，应该有大的概貌

<table><colgroup><col> <col> <col> <col> <col> <col> <col> <col></colgroup><thead><tr><th><p>序号</p></th><th colspan="1"><p>项目名称</p></th><th><p>项目的里程碑，解决什么问题</p></th><th><p>启动时间（大概）</p></th><th colspan="1"><p>结束时间（大概）</p></th><th colspan="1"><p>涉及外部团队</p></th><th colspan="1"><p>耗费人力资源（大概）</p></th><th colspan="1"><p>项目方案概述</p></th></tr></thead><tbody><tr><td>1</td><td colspan="1">优惠券重构</td><td><p>重新设计优惠券基础模型，增强扩展性</p><p>梳理统一优惠券的核心流程，收拢对外API</p></td><td>2020.04</td><td colspan="1">2020-Q3</td><td colspan="1"><p>商品</p><p>交易</p><p>结算</p><p>上游各业务线使用方</p></td><td colspan="1">100PD+</td><td colspan="1">先设计核心基础模型，再基于基础模型设计核心服务接口，然后进行灰度数据迁移，最后推动上游逐步迁移新的服务接口</td></tr><tr><td>2</td><td colspan="1">优惠立减开发</td><td><p>设计新的立减基础促销形式</p><p>支持基于立减二次包装的一些优惠促销形式</p></td><td>2020.03月初</td><td colspan="1">2020-Q2</td><td colspan="1"><p>商品</p><p>交易</p><p>结算</p><p>上游各业务线使用方</p></td><td colspan="1">50PD+</td><td colspan="1"><p>先设计立减基础模型及服务，支持线下门店立减促销</p><p>再逐步支持基于立减二次的优惠促销形式的迁移</p></td></tr><tr><td>3</td><td colspan="1">赠品重构</td><td><p>设计新的统一支持购后返赠系统</p><p>迁移现有赠品系统</p></td><td>2020.04</td><td colspan="1">2020-Q2</td><td colspan="1"><p>商品</p><p>交易</p><p>结算</p><p>上游各业务线使用方</p></td><td colspan="1">30PD+</td><td colspan="1"><p>借着赠品老系统的重构，设计新的返赠系统基础模型及服务，支付现有赠品系统的无缝迁移</p><p>逐步支持其他返赠类的促销形式</p></td></tr><tr><td>4</td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr></tbody></table>