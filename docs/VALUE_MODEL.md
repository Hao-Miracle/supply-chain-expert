# Value measurement / 价值测量

This document turns “saves time” into a result that a procurement team can verify. The ranges shown in the README are planning baselines for pilot design, not guaranteed outcomes or results from a completed third-party benchmark.

本文把“节省时间”变成采购团队可以核验的结果。README 中的区间用于设计试点容量，不代表效果承诺，也不冒充已经完成的第三方评测。

## 中文

### 测量边界

选择一个有代表性的工程采购项目，固定清单条数、供应商数量和交付物范围。分别记录传统人工方式与 Agent 辅助方式在下列环节的实际用时：

1. 需求清单整理与缺失项补全
2. 设备分类与规格标准化
3. 成本资料整理与市场参考核验
4. 供应商筛选与询价文件准备
5. 报价清洗、拉齐与比价分析
6. 议价、定标材料和合同或订单草稿准备
7. 物流状态汇总、验收记录与供应商评价
8. 项目状态汇总和跨人交接

Gate 审核时间、异常返工时间和等待供应商回复的时间必须分开记录。等待时间不计入 Agent 带来的人工节省。

### 核心公式

```text
人工工时节省率 = (人工基线工时 - Agent辅助工时) / 人工基线工时 × 100%
效率提升倍数 = 人工基线工时 / Agent辅助工时
净节省工时 = 人工基线工时 - Agent辅助工时 - 新增返工工时
净人工成本节省 = 净节省工时 × 团队综合小时成本 - Agent新增使用成本
```

综合小时成本可使用企业自己的全成本口径，包括工资、社保、管理分摊等；公开案例不应披露个人薪酬。

### README 规划样例

假设一个项目包含 200 条物料和 5 家候选供应商，传统方式需要 45–70 人工小时，Agent 辅助后需要 25–40 人工小时，则单项目计划节省约 20–30 小时，对应约 25%–45% 的端到端人工操作时间下降。该样例只用于试点排期，正式对外引用前必须替换为真实计时结果。

### 试点验收表

| 指标 | 人工基线 | Agent辅助 | 差值 | 证据 |
|---|---:|---:|---:|---|
| 清单与分类工时 |  |  |  | 时间记录、输出版本 |
| 询价与比价工时 |  |  |  | 询价表、报价比较表 |
| 商务材料准备工时 |  |  |  | 定标材料、合同草稿 |
| 履约与交接工时 |  |  |  | 状态记录、交接记录 |
| Gate审核工时 |  |  |  | Gate确认记录 |
| 异常返工工时 |  |  |  | 纠错记录 |
| 分类准确率 |  |  |  | 独立人工标注测试集 |
| 对外字段泄露数 |  |  |  | 外发文件检查结果 |

效率不能以牺牲质量为代价。设备分类准确率应在独立、人工确认的冻结测试集上测量；所有关键决定继续由采购员通过对应 Gate。

## English

### Measurement boundary

Choose a representative engineering-procurement project and freeze its line-item count, supplier count, and deliverables. Measure actual labor time for both the manual baseline and the agent-assisted workflow across requirements, classification, cost preparation, sourcing, RFQ, quote comparison, commercial documents, delivery, acceptance, evaluation, reporting, and handoff.

Track Gate review, exception rework, and supplier waiting time separately. Waiting time is not counted as labor saved by the agent.

### Core formulas

```text
Labor reduction = (manual baseline hours - agent-assisted hours) / manual baseline hours × 100%
Speed multiplier = manual baseline hours / agent-assisted hours
Net hours saved = manual baseline hours - agent-assisted hours - additional rework hours
Net labor-cost saving = net hours saved × blended hourly cost - incremental agent cost
```

Use the organization's own fully loaded hourly-cost method. Public evidence should not disclose individual compensation.

### Planning example

For 200 line items and 5 candidate suppliers, a manual baseline of 45–70 hours and an agent-assisted range of 25–40 hours yields a planning estimate of roughly 20–30 hours saved per project, or a 25%–45% reduction in manual touch time. Replace this estimate with measured pilot results before presenting it as achieved performance.

Quality remains a constraint, not a trade-off. Measure classification accuracy on an independently reviewed frozen test set, and keep accountable purchaser approval at every applicable Gate.
