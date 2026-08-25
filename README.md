# 供应链专家

[简体中文](README.md) | [English](README_EN.md)

一个可解释的采购 Agent。当前从工程与IT集成采购中的设备分类与标准化开始：将非标准设备名称进行规范化，输出系统分类、细化分类、编码、置信度、判断依据和候选冲突，并把新设备交给人工审核，而不是静默强制分类。

## 项目边界

本仓库公开的是通用分类框架、基础规则、审计数据结构和Agent Skill示例，不包含任何企业真实采购清单、供应商、报价、合同、会话日志、账号配置或人工确认知识库。

```text
设备名称/规格/备注 → 标准化 → 规则候选 → 可解释分类建议 → Gate-1人工确认 → 企业私有知识库
```

## 快速开始

```bash
python -m pip install -e .
procurement-classify --name "24口千兆交换机" --spec "24GE+4SFP"
```

不安装时可以运行：

```bash
PYTHONPATH=src python -m procurement_classifier.cli --name "网络硬盘录像机" --spec "32路 8盘位"
```

规则结果默认需要人工审核。只有使用者在自己的私有环境中明确导入的人工确认历史，才可以作为稳定复用依据。

## 内容

- `src/procurement_classifier/`：通用分类与审计核心。
- `skills/procurement-device-classification/`：Agent Skill。
- `schemas/ai-classification-audit.schema.json`：24字段AI运行审计结构。
- `examples/`：完全虚构的演示记录。
- `tests/`：分类、人工审核和审计哈希测试。
- `docs/SECURITY_AND_DATA.md`：隐私和发布边界。

## 准确率声明

本项目不承诺对未知设备自动达到固定准确率。准确率必须在使用方独立、人工确认且未参与规则开发的测试集上测量。新设备、候选冲突或信息不足时应进入人工审核。

## 发布前隐私检查

```bash
python scripts/privacy_scan.py
PYTHONPATH=src python -m unittest discover -s tests -v
```

隐私扫描通过只是发布的必要条件，仍需人工复核完整Git提交清单。

## 许可证

代码使用 Apache License 2.0。示例数据为虚构数据，仅用于演示。使用者必须自行确认业务数据来源、授权、隐私和合规要求。
