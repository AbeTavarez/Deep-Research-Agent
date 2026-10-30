from deepagents import create_deep_agent

from dotenv import load_dotenv

from src.deep_research_agent.prompts import SYSTEM_PROMPT

load_dotenv()


# (LLM) Large Language Model
model = "openai:gpt-5.5"

agent = create_deep_agent(model=model, system_prompt=SYSTEM_PROMPT)



if __name__ == "__main__":
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "What's a micro controller?"}]}
    )

print(response)
