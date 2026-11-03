# Deep Research Agent 

## Get started

```bash
# Start project
git clone https://github.com/AbeTavarez/Deep-Research-Agent.git
cd Deep-Research-Agent/

uv sync

source .venv/Scripts/activate # Windows
source .venv/bin/activate # Mac/Linux

cp .env.example .env
#! -> Add your API keys to your .env file <-

# Choose your provider!
# I'm using OpenAI, if you want to use the same provider just add your API key. 
# -> If you want to use a different provider or a FREE:
# See full list of providers:
# https://docs.langchain.com/oss/python/integrations/providers/all_providers

# Run Agent
langgraph dev
```