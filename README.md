<p align="center">
  <img src="assets/hero.svg" alt="Supply Chain Expert" width="100%" />
</p>

<p align="center">
  <a href="README.md">简体中文</a>&nbsp;&nbsp;·&nbsp;&nbsp;<a href="README_EN.md">English</a>
</p>

<h3 align="center">让采购成为一条连续、清晰、可积累的智能工作流。</h3>

<p align="center">
  <strong>Hermes Agent 原生采购 Profile</strong><br/>
  从需求清单到供应商评价，一个 Agent 贯穿项目始终。<br/>
  AI 处理复杂信息，人掌握关键决定。
</p>

<br/>

## 从清单，到结果

<p align="center">
  <img src="assets/workflow.svg" alt="完整智能采购流程" width="100%" />
</p>

供应链专家将十个采购环节组织成同一条项目主线。每次处理都会留下阶段、依据、状态与交接；四个质量 Gate 让确认自然发生在最重要的位置。

<table>
  <tr>
    <td width="25%"><strong>Gate 01</strong><br/><sub>清单与分类</sub></td>
    <td width="25%"><strong>Gate 02</strong><br/><sub>定标与合同</sub></td>
    <td width="25%"><strong>Gate 03</strong><br/><sub>到货与验收</sub></td>
    <td width="25%"><strong>Gate 04</strong><br/><sub>评价与收尾</sub></td>
  </tr>
</table>

## 把时间还给采购员

供应链专家优先压缩清单整理、分类标准化、询价表生成、报价拉齐、过程追踪和项目交接中的重复劳动。采购员仍负责四个 Gate，但不必反复搬运字段、翻找上下文或从零整理比较表。

以 **200 条物料、5 家候选供应商** 的中等规模工程采购为规划样例，在数据模板稳定、人工 Gate 正常执行的前提下：

| 价值指标 | 规划参考区间 |
|---|---:|
| 端到端人工操作时间 | 减少 **25%–45%** |
| 清单整理与分类标准化 | 提速 **1.5–2.5×** |
| 询价准备与报价拉齐 | 提速 **2–3×** |
| 状态汇总与跨人交接 | 提速 **2–4×** |
| 单项目人工工时 | 约节省 **20–30 小时** |

这些数字是容量规划基线，不是对所有项目的效果承诺。真实收益取决于清单质量、供应商数量、历史数据完整度、异常比例和人工复核深度。项目内置可复核的测量口径：以相同范围下的人工基线工时与 Agent 辅助工时对比，并单独记录返工时间和 Gate 审核时间。计算方法与试点验收表见 [`docs/VALUE_MODEL.md`](docs/VALUE_MODEL.md)。

## 一个核心，四种能力

<table>
  <tr>
    <td width="50%">
      <h3>01 · Workflow</h3>
      十阶段采购编排。项目状态连续，任务边界清晰，交接随时可恢复。
    </td>
    <td width="50%">
      <h3>02 · Intelligence</h3>
      设备分类、规格标准化、成本分析、供应商匹配与商务建议进入同一上下文。
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>03 · Control</h3>
      四个 Gate 连接 AI 建议与采购员确认，让每个关键决定都有清晰归属。
    </td>
    <td width="50%">
      <h3>04 · Memory</h3>
      项目事实、确认结果与可复用经验持续回流，形成越来越懂业务的采购知识。
    </td>
  </tr>
</table>

## 部署为 Hermes Agent

```bash
# 1. 安装 Hermes Agent
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# 2. 一键安装完整采购Agent Profile
hermes profile install \
  github.com/Hao-Miracle/supply-chain-expert \
  --alias

# 3. 配置并启动
supply-chain-expert setup
supply-chain-expert chat
```

现在直接和它对话：

```text
创建一个新的工程采购项目，导入需求清单，
并告诉我Gate-1之前还缺哪些信息。
```

安装命令会一次装入专属 Profile、`SOUL.md`、采购全流程 Skill 和设备分类 Skill。模型配置、会话、记忆与凭据保留在使用者自己的 Hermes 环境中。完整部署、更新与消息平台接入见 [`docs/HERMES_DEPLOYMENT.md`](docs/HERMES_DEPLOYMENT.md)。

### 可选：安装确定性业务工具

Python 是 Agent 下层的规则与校验工具，不是产品入口。需要设备分类、询价字段过滤或流程状态校验时安装：

```bash
python -m pip install -e .
```

Hermes 可以调用这些能力，也可以直接在 Python 中集成：

```python
from supply_chain_expert import ProcurementWorkflow

flow = ProcurementWorkflow("DEMO-001", "园区网络升级")

flow.record("requirements", "import", "需求清单已导入")
flow.record(
    "classification_standardization",
    "classify",
    "分类与标准化建议已生成",
)

flow.approve_gate("gate1", reviewer="purchaser")
external_rfq = flow.prepare_external_rfq({
    "item": "24口千兆交换机",
    "quantity": 2,
    "internal_cost": 100,
})
```

## 智能采购的基础能力

| | 能力 | 输出 |
|---:|---|---|
| 01 | 需求与清单 | 结构化条目、缺失信息、项目上下文 |
| 02 | 分类与标准化 | 分类、编码、标准规格、置信度、判断依据 |
| 03 | 成本与市场核验 | 成本分析、价格异常、核验依据 |
| 04 | 供应商与询价 | 候选供应商、询价清单、可比报价 |
| 05 | 议价与定标 | 议价要点、综合分析、定标建议 |
| 06 | 合同与履约 | 合同或订单草稿、物流状态、到货信息 |
| 07 | 验收与回流 | 验收记录、供应商评价、采购知识沉淀 |

市场价格始终以“核验参考”进入流程，并携带规格、品牌、单位、税率、运费、地区、来源与采集日期。对外询价则只保留适合对外共享的信息。

## Agent 组成

<table>
  <tr>
    <td width="50%">
      <a href="skills/supply-chain-expert/SKILL.md"><strong>supply-chain-expert</strong></a><br/>
      <sub>采购全流程、质量 Gate、商业规则与项目交接</sub>
    </td>
    <td width="50%">
      <a href="skills/procurement-device-classification/SKILL.md"><strong>procurement-device-classification</strong></a><br/>
      <sub>可解释的工程采购设备分类与标准化</sub>
    </td>
  </tr>
</table>

| 层 | 作用 |
|---|---|
| Hermes Profile | 隔离模型、工具、会话、技能与记忆 |
| `AGENTS.md` | 每次会话自动加载采购流程和执行规则 |
| Procurement Skill | 驱动十阶段采购工作流与四个Gate |
| Project Memory | 跨会话恢复项目状态、决定、文件与下一步 |
| Python Tools | 执行分类、脱敏、校验等确定性业务动作 |

流程契约位于 [`docs/WORKFLOW.md`](docs/WORKFLOW.md)，价值测量位于 [`docs/VALUE_MODEL.md`](docs/VALUE_MODEL.md)，部署说明位于 [`docs/HERMES_DEPLOYMENT.md`](docs/HERMES_DEPLOYMENT.md)，状态结构位于 [`schemas/procurement-workflow.schema.json`](schemas/procurement-workflow.schema.json)。

## 数据边界

公共仓库由通用代码、公开文档与合成示例构成。企业采购数据、运行配置与组织知识保留在使用者自己的环境中。仓库内置隐私扫描，并为外发询价提供商业字段过滤。

```bash
python scripts/privacy_scan.py
PYTHONPATH=src python -m unittest discover -s tests -v
```

## 开源与企业服务

核心代码继续采用 Apache-2.0，个人与企业均可依许可证自由使用和商用。需要私有化部署、企业分类体系、采购知识库、系统集成、培训、维护或服务级别保障时，可选择[企业商业服务](COMMERCIAL.md)。品牌和官方身份的使用规则见[商标与品牌政策](TRADEMARKS.md)，正式项目可参考[《企业商业服务协议模板》](docs/企业商业服务协议模板.md)磋商签约。

## Build with us

欢迎围绕采购工作流、行业分类、数据结构与 Agent 协作提交 Issue 和 Pull Request。

<p align="center">
  <sub>Apache-2.0 · Built for explainable procurement intelligence.</sub>
</p>
