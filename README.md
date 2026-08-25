# 供应链专家

[简体中文](README.md) | [English](README_EN.md)

一个注重隐私、可解释且由采购员最终确认的智能采购 Agent。它覆盖从需求清单到供应商评价与采购数据回流的完整采购闭环，设备分类与标准化只是其中一个环节。

```text
需求清单 → 分类与标准化 → 成本估算 → 供应商匹配 → 询价比价
→ 议价与定标 → 合同或采购订单 → 物流跟踪 → 到货验收
→ 供应商评价与采购数据回流
```

流程设置四个人工质量门禁：Gate-1确认清单与分类，Gate-2确认定标与合同，Gate-3确认到货验收，Gate-4确认评价与项目收尾。AI负责整理、核验和建议，采购员负责最终决定。

## 项目边界

本仓库公开的是通用采购流程编排、业务安全规则、设备分类组件、审计数据结构、虚构示例和Agent Skills，不包含任何企业真实采购清单、供应商、报价、合同、会话日志、账号配置或人工确认知识库。

```text
公开通用框架 + 使用者私有数据与配置 + 人工Gate确认 = 可落地的采购工作流
```

ERP对接、ERP入库、销售订单匹配、销购匹配和业财预转单不属于本项目流程。物流接口和图片OCR验收只提供扩展位置，未验证真实接入前不得称为自动运行。

## 快速开始

```bash
python -m pip install -e .
procurement-classify --name "24口千兆交换机" --spec "24GE+4SFP"
supply-chain-expert --project-id "DEMO-001" --project-name "虚构演示项目"
```

不安装时可以运行：

```bash
PYTHONPATH=src python -m procurement_classifier.cli --name "网络硬盘录像机" --spec "32路 8盘位"
```

分类规则、供应商推荐、定标建议、合同草稿和验收辅助结果默认不能替代人工决定。只有使用者在自己的私有环境中明确确认的历史，才可以作为稳定复用依据。

## 关键安全规则

- 对外询价文件自动排除内部成本价、目标价和其他供应商报价。
- 市场价数据库仅供核验参考，不直接决定成本价、目标价、成交价或供应商。
- 市场参考价必须核对规格、品牌、单位、税率、运费、地区、来源和采集日期；信息不全时标记“待人工核验”。
- 新分类建议必须经过Gate-1，定标和合同必须经过Gate-2，验收必须经过Gate-3，评价与数据回流必须经过Gate-4。

## 内容

- `src/supply_chain_expert/`：完整采购流程编排、Gate与安全策略。
- `src/procurement_classifier/`：设备分类与审计组件。
- `skills/supply-chain-expert/`：采购全流程Agent Skill。
- `skills/procurement-device-classification/`：设备分类子Skill。
- `docs/WORKFLOW.md`：流程、Gate和能力边界。
- `schemas/ai-classification-audit.schema.json`：24字段AI运行审计结构。
- `schemas/procurement-workflow.schema.json`：完整采购流程快照结构。
- `examples/`：完全虚构的演示记录。
- `tests/`：分类、人工审核和审计哈希测试。
- `docs/SECURITY_AND_DATA.md`：隐私和发布边界。

## 准确率声明

本项目不承诺对未知设备自动达到固定准确率，也不把流程完整等同于真实集成已经上线。分类准确率必须在使用方独立、人工确认且未参与规则开发的测试集上测量。新设备、候选冲突或信息不足时应进入人工审核。

## 发布前隐私检查

```bash
python scripts/privacy_scan.py
PYTHONPATH=src python -m unittest discover -s tests -v
```

隐私扫描通过只是发布的必要条件，仍需人工复核完整Git提交清单。

## 许可证

代码使用 Apache License 2.0。示例数据为虚构数据，仅用于演示。使用者必须自行确认业务数据来源、授权、隐私和合规要求。
