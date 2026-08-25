# Deploy Supply Chain Expert as a Hermes Agent

Supply Chain Expert is a native Hermes Profile Distribution. The repository packages the agent's identity, procurement Skills, workflow rules, and update manifest. Python modules remain an optional deterministic tool layer.

## Install

Install Hermes Agent with its official installer:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Install the complete procurement agent from GitHub:

```bash
hermes profile install \
  github.com/Hao-Miracle/supply-chain-expert \
  --alias
```

Hermes reads `distribution.yaml`, previews the agent, creates an isolated profile, and installs the distribution-owned `SOUL.md` and procurement Skills. User sessions, memories, model settings, and credentials remain user-owned.

## Configure and start

The `--alias` option creates the `supply-chain-expert` command:

```bash
supply-chain-expert setup
supply-chain-expert doctor
supply-chain-expert chat
```

Start with a natural-language request:

```text
创建一个新的工程采购项目，导入需求清单，并告诉我Gate-1之前还缺哪些信息。
```

The agent restores persistent project context, identifies the current procurement stage, loads the relevant Skill, and moves the task toward its next quality Gate.

## What the Profile contains

```text
distribution.yaml
SOUL.md
skills/
  supply-chain-expert/
  procurement-device-classification/
```

- `distribution.yaml` makes the repository installable and updateable as one Hermes agent.
- `SOUL.md` defines procurement identity, operating rhythm, commercial judgment, memory, and data care.
- `supply-chain-expert` drives the ten-stage procurement workflow and four human Gates.
- `procurement-device-classification` provides explainable classification and standardization guidance.

## Update

Pull future agent improvements while preserving user-owned memory and sessions:

```bash
hermes profile update supply-chain-expert
```

Inspect the installed distribution:

```bash
hermes profile info supply-chain-expert
```

## Use in a cloned project workspace

Clone the repository when you also want its Python tools, schemas, tests, and project-local `AGENTS.md`:

```bash
git clone https://github.com/Hao-Miracle/supply-chain-expert.git
cd supply-chain-expert
python -m pip install -e .
```

Create an optional local project handoff file:

```bash
mkdir -p .sce
cp templates/PROJECT_MEMORY.md .sce/PROJECT_MEMORY.md
```

The `.sce/` directory is Git-ignored. When Hermes starts from the repository, `AGENTS.md` directs it to restore and update that project handoff.

## Connect a messaging platform

Configure the gateway through the installed profile alias:

```bash
supply-chain-expert gateway setup
supply-chain-expert gateway run
```

For a background service:

```bash
supply-chain-expert gateway install
supply-chain-expert gateway start
```

The same agent identity, Skills, sessions, memory, and quality Gates then serve the configured messaging channel.

## Verification

```bash
supply-chain-expert skills list
supply-chain-expert doctor
hermes profile info supply-chain-expert
```

In a new chat, ask the agent to state the ten procurement stages, four Gates, market-reference rule, current project stage, and next action.

Official Hermes documentation: https://hermes-agent.nousresearch.com/docs/
