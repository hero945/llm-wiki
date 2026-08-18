---
title: "04-领域边界（promo） - 研发部"
author:
  - "[[李力5]]"
created: 2026-06-30
description:
tags:
  - "tuhu"
---
[转至元数据结尾](#page-metadata-end) [转至元数据起始](#page-metadata-start)

## 1 本领域提供的接口

<table><colgroup><col> <col> <col> <col> <col> <col></colgroup><tbody><tr><td rowspan="2"><strong>服务</strong></td><td colspan="5"><strong>领域提供的接口</strong></td></tr><tr><th><strong>对外提供接口</strong></th><th colspan="1"><strong>接口参数与结果 （ <em>参数后续可完善</em> ）</strong></th><th colspan="1"><strong>接口提供的功能</strong></th><th><strong>向外发出消息topic</strong></th><th colspan="1"><strong>消息体内容</strong></th></tr><tr><td rowspan="2">优惠领取服务</td><td>领取/发放单种优惠</td><td colspan="1"></td><td colspan="1">单个用户或多个用户领取指定优惠（一般是券）</td><td rowspan="2">优惠领取消息（XX人领取了XX优惠）</td><td rowspan="2"></td></tr><tr><td><p>批量领取/发放多种优惠</p></td><td colspan="1"></td><td colspan="1">单个用户或多个用户批量领取多个优惠（一般是个券包）</td></tr><tr><td rowspan="5">优惠查询服务</td><td>批量查询可用优惠活动列表</td><td colspan="1"></td><td colspan="1"><p>批量查询多个（商品、门店、服务等）可用的优惠活动信息</p><p>一般用于列表页、搜索页、活动页查询优惠活动（标签、有效期、优惠价格等）信息</p></td><td></td><td colspan="1"></td></tr><tr><td colspan="1">查询可用优惠活动列表</td><td colspan="1"></td><td colspan="1"><p>查询但个（商品、门店、服务等）可用的优惠活动信息</p><p>一般用于详情页查询优惠活动详细信息</p></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">查询可用优惠活动组合列表</td><td colspan="1"></td><td colspan="1"><p>查询（单个、多个）商品的可用优惠活动组合</p><p>一般用于提单页</p></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">查询优惠活动明细</td><td colspan="1"></td><td colspan="1">查询某个优惠活动的明细（优惠价格、有效期、适用条件等）信息</td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">批量查询优惠活动明细</td><td colspan="1"></td><td colspan="1">批量查询多个优惠活动的明细（优惠价格、有效期、适用条件等）信息</td><td colspan="1"></td><td colspan="1"></td></tr><tr><td rowspan="2">优惠校验服务</td><td colspan="1">校验单笔优惠</td><td colspan="1"></td><td colspan="1">校验用户下单购买的（单个、多个）（商品、门店、服务等）是否可使用某一个优惠活动</td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">批量校验多笔优惠</td><td colspan="1"></td><td colspan="1">批量校验用户下单购买的（单个、多个）（商品、门店、服务等）是否可使用指定的多个优惠活动</td><td colspan="1"></td><td colspan="1"></td></tr><tr><td rowspan="2">优惠锁定服务</td><td colspan="1">预锁定优惠</td><td colspan="1"></td><td colspan="1"><p>用户下单优惠校验成功后预先锁定（单个、多个）优惠的库存及资格</p><p>适用于部分需严格控制库存&资格的场景</p></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">取消锁定优惠</td><td colspan="1"></td><td colspan="1">回滚之前预锁定（单个、多个）优惠的库存及资格</td><td colspan="1"></td><td colspan="1"></td></tr><tr><td rowspan="6">优惠核销服务</td><td colspan="1">核销单笔优惠</td><td colspan="1"></td><td colspan="1"><p>核销用户下单过程中指定的某个优惠活动</p><p>通常会核销（库存、资格、预算等）</p></td><td rowspan="3">优惠核销消息（XX人下单购买了XX商品使用了XX优惠）</td><td rowspan="3"></td></tr><tr><td colspan="1">批量核销多笔优惠</td><td colspan="1"></td><td colspan="1"><p>批量核销用户下单过程中指定的多个优惠活动</p></td></tr><tr><td colspan="1">批量校验并核销多笔优惠</td><td colspan="1"></td><td colspan="1">批量校验并核销用户下单过程中指定的多个优惠活动</td></tr><tr><td colspan="1">回退单笔优惠</td><td colspan="1"></td><td colspan="1"><p>回退用户下单过程中指定的某个优惠活动</p><p>通常会回退（库存、资格、预算等）</p><p>一般在下单失败或订单退款时触发优惠回退</p></td><td rowspan="3">优惠回退消息（XX人退货之前XX订单的XX商品触发回退了XX优惠）</td><td rowspan="3"></td></tr><tr><td colspan="1">批量回退多笔优惠</td><td colspan="1"></td><td colspan="1">批量回退用户下单过程中指定的多个优惠活动</td></tr><tr><td colspan="1">部分回退单笔优惠</td><td colspan="1"></td><td colspan="1"><p>回退用户下单过程中指定某个优惠活动的部分优惠</p><p>通常会基于规则决定是否回退（库存、资格、预算等）</p><p>一般是下单多个商品后要求退单其中某1个或几个商品时触发优惠部分回退</p></td></tr><tr><td colspan="1">优惠活动状态广播</td><td colspan="1">-----</td><td colspan="1"></td><td colspan="1">-----</td><td colspan="1">优惠活动状态变更消息（XX优惠活动状态由XX变更到XX）</td><td colspan="1"></td></tr></tbody></table>

## 2 依赖外部领域接口

<table><colgroup><col> <col> <col> <col> <col></colgroup><tbody><tr><td rowspan="2"><strong>领域</strong></td><td colspan="4"><strong>领域依赖的</strong></td></tr><tr><th><strong>调用外部接口</strong></th><th><strong>是否得到满足</strong></th><th><strong>监听外部消息</strong></th><th><strong>是否得到满足</strong></th></tr><tr><td rowspan="2">商品领域</td><td>查询商品基础信息（品牌、品类等）</td><td>√</td><td>商品上下架消息</td><td>√</td></tr><tr><td>批量查询商品基础信息</td><td>√</td><td></td><td></td></tr><tr><td>库存领域</td><td colspan="1">查询商品的可售卖库存</td><td colspan="1">√</td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1"></td><td colspan="1">查询商品在特定仓库的可售卖库存</td><td colspan="1">√</td><td colspan="1"></td><td colspan="1"></td></tr><tr><td rowspan="2">价格领域</td><td>查询商品价格</td><td>√</td><td>商品基础价格变更消息</td><td>√</td></tr><tr><td colspan="1">批量查询商品价格</td><td colspan="1">√</td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">用户领域</td><td colspan="1">查询用户基础信息</td><td colspan="1">√</td><td colspan="1"></td><td colspan="1"></td></tr><tr><td rowspan="4">门店领域</td><td colspan="1">查询门店基础信息</td><td colspan="1">√</td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">批量查询门店基础信息</td><td colspan="1">√</td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">查询门店可售商品信息</td><td colspan="1">√</td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">查询某个商品是否在某个门店可售</td><td colspan="1">√</td><td colspan="1"></td><td colspan="1"></td></tr><tr><td rowspan="2">适配领域</td><td colspan="1">查询商品适配信息</td><td colspan="1">√</td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">批量查询商品适配信息</td><td colspan="1">√</td><td colspan="1"></td><td colspan="1"></td></tr><tr><td>交易领域</td><td colspan="1">-----</td><td colspan="1"></td><td colspan="1">订单状态变更消息</td><td colspan="1">√</td></tr><tr><td rowspan="2">其他领域</td><td colspan="1">查询员工账号相关信息</td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr><tr><td colspan="1">查询组织架构相关信息</td><td colspan="1"></td><td colspan="1">组织架构变更消息</td><td colspan="1"></td></tr><tr><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td><td colspan="1"></td></tr></tbody></table>

## 3 与其他领域模糊待决的边界

| 其他领域 | 优惠域 |
| --- | --- |
| **商品域** | 商品的优惠标签（ 11-赠 13-券 14-促 15-折 23-秒杀 25-拼团 27-预售）展示（已明确）  [商品标签梳理](https://wiki.tuhu.cn/pages/viewpage.action?pageId=36903520) |
| **价格域** | 商品定价涉及优惠部分的边界划分（待讨论） |
| **库存域** | —— |
| **交易域** | —— |
| **结算域** | —— |
| **企业客户域** | —— |
| **门店信息** | —— |
| **金融支付域** | —— |
| **金融账户域** | —— |
| **会员域** | 会员域所使用的优惠需沉淀到优惠领域（已明确） |
| **车型适配域** | —— |
| **积分域** | —— |