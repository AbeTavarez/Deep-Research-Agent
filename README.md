# Deep Research Agent 

## Get started

```bash
# Start project
uv init --package deep-research-agent
cd deep-research-agent/
source .venv/Scripts/activate # Windows
source .venv/bin/activate # Mac/Linux
uv add deepagents python-dotenv

# Add your provider
uv add langchain-openai
# See full list of providers:
# https://docs.langchain.com/oss/python/integrations/providers/all_providers

# Run Agent
uv run agent.py

# Adding Tracing and Studio
uv add "langgraph-cli[inmem]"
langgraph dev
```