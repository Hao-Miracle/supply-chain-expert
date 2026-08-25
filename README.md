<div align="center">
  <img src="assets/hero.svg" alt="供应链专家" width="100%" />
</div>

<div align="center">

[简体中文](README.md) · [English](README_EN.md)

[![Python](https://img.shields.io/badge/Python-3.10%2B-2563EB?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache--2.0-22C55E?style=flat-square)](LICENSE)
![Tests](https://img.shields.io/badge/Tests-8%20passing-22C55E?style=flat-square)
![Privacy](https://img.shields.io/badge/Data-Synthetic%20only-7C3AED?style=flat-square)
![Human in the loop](https://img.shields.io/badge/Decision-Human%20in%20the%20loop-F59E0B?style=flat-square)

**把采购流程交给 Agent，把关键决定留给人。**

面向工程与 IT 集成项目的可解释智能采购框架。

</div>

## 为什么是供应链专家？

采购不是一次分类，也不是一次比价。它是一条跨越清单、价格、供应商、合同、物流和验收的连续决策链。

供应链专家把这条链装进一个可审计的 Agent 工作流：AI负责整理、核验和建议；采购员通过四个 Gate 掌握最终决定。每一步都有阶段、依据、状态和交接，不因会话中断而失去项目上下文。

## 一条完整的采购闭环

```mermaid
flowchart LR
    A[需求清单] --> B[分类与标准化]
    B --> G1{{Gate-1}}
    G1 --> C[成本估算]
    C --> D[供应商匹配]
    D --> E[询价比价]
    E --> F[议价与定标]
    F --> G2{{Gate-2}}
    G2 --> G[合同或订单]
    G --> H[物流跟踪]
    H --> I[到货验收]
    I --> G3{{Gate-3}}
    G3 --> J[供应商评价与数据回流]
    J --> G4{{Gate-4}}
```

| Gate | 采购员确认什么 | AI不能替你做什么 |
|---|---|---|
| Gate-1 | 品名、分类、规格、数量、询价清单 | 把分类建议当成确认结果 |
| Gate-2 | 供应商、价格、税率、交期、合同或订单 | 自动定标或签署合同 |
| Gate-3 | 型号、数量、外观、验收异常 | 自动判定最终验收通过 |
| Gate-4 | 供应商评价、成交事实、未完成事项 | 自动关闭项目或写入确认知识库 |

## 它已经提供什么？

| 能力 | 公开版状态 | 说明 |
|---|---:|---|
| 10阶段采购流程编排 | ✅ 可运行 | 阶段不可静默跳过或倒退 |
| 四个人工质量门禁 | ✅ 可运行 | Gate不能提前批准，必须记录审核人 |
| 设备分类与标准化 | ✅ 参考实现 | 输出分类、编码、置信度、依据和冲突候选 |
| 对外询价脱敏 | ✅ 可运行 | 递归移除内部成本、目标价和竞品报价 |
| 市场价核验策略 | ✅ 可运行 | 永远标记为核验参考，不拥有定价权 |
| 成本、供应商、比价、合同 | 🧩 流程接口 | 接入企业私有数据源后运行 |
| 物流接口、图片OCR验收 | 🧪 待验证扩展 | 未接入真实服务前不宣称自动化 |

> ERP对接、ERP入库、销售订单匹配、销购匹配和业财预转单不属于本项目。

## 60秒运行

```bash
git clone https://github.com/Hao-Miracle/supply-chain-expert.git
cd supply-chain-expert
python -m pip install -e .
```

启动一个不含真实业务数据的流程：

```bash
supply-chain-expert \
  --project-id "DEMO-001" \
  --project-name "虚构演示项目"
```

单独体验设备分类组件：

```bash
procurement-classify \
  --name "24口千兆交换机" \
  --spec "24GE+4SFP"
```

## 像这样控制采购流程

```python
from supply_chain_expert import ProcurementWorkflow

flow = ProcurementWorkflow("DEMO-001", "虚构演示项目")

flow.record("requirements", "import", "需求清单已导入")
flow.record(
    "classification_standardization",
    "classify",
    "分类与标准化建议已生成",
)

# 关键步骤必须由采购员确认
flow.approve_gate("gate1", reviewer="purchaser")

# 对外询价前递归移除内部商业字段
external_rfq = flow.prepare_external_rfq({
    "item": "演示设备",
    "quantity": 2,
    "internal_cost": 100,
    "target_price": 120,
})
```

`external_rfq` 只保留可以对外发送的字段。未经Gate-1确认，询价文件无法生成。

## 市场价：只核验，不定价

任何外部价格进入流程时，都必须核对：

`型号规格` · `品牌` · `单位` · `税率` · `运费` · `地区` · `来源` · `采集日期`

信息缺失或已过期时，结果会标记为“待人工核验”。市场价不能直接成为成本价、目标价、成交价或自动定标依据。

## 为 Agent 而生

仓库同时提供两个可复用 Skill：

- [`supply-chain-expert`](skills/supply-chain-expert/SKILL.md)：采购全流程、Gate、商业安全和交接规则。
- [`procurement-device-classification`](skills/procurement-device-classification/SKILL.md)：设备分类与标准化子能力。

完整流程约定见 [`docs/WORKFLOW.md`](docs/WORKFLOW.md)，流程数据结构见 [`schemas/procurement-workflow.schema.json`](schemas/procurement-workflow.schema.json)。

## 隐私不是附加功能

这个仓库只包含通用代码、公开文档和完全虚构的演示数据，不包含：

- 真实采购清单、供应商、客户、报价、成本和合同；
- 联系方式、银行信息、身份信息或账号凭据；
- Agent Profile、环境变量、会话、日志、记忆或运行数据库；
- 企业人工校准知识库和数据知识产权存证材料。

发布前检查：

```bash
python scripts/privacy_scan.py
PYTHONPATH=src python -m unittest discover -s tests -v
```

自动扫描是必要条件，完整Git提交仍需人工复核。安全边界详见 [`docs/SECURITY_AND_DATA.md`](docs/SECURITY_AND_DATA.md)。

## 项目结构

```text
src/supply_chain_expert/        完整流程、Gate和安全策略
src/procurement_classifier/     可解释设备分类组件
skills/                         Agent Skills
schemas/                        流程与AI审计数据结构
examples/                       完全虚构的演示数据
tests/                          流程、安全和分类测试
```

## 参与项目

欢迎提交 Issue 和 Pull Request。请只使用虚构或已经合法公开的数据；不要在问题、截图、测试样例或提交记录中粘贴真实报价、合同、联系人或账号信息。

## License

[Apache License 2.0](LICENSE)
