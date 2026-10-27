from deepagents import create_deep_agent

from dotenv import load_dotenv

load_dotenv()


# (LLM) Large Language Model
model = "openai:gpt-5.5"

agent = create_deep_agent(
    model=model
)

response = agent.invoke({
    "messages": [
        {"role": "user", "content": "What's a micro controller?"}
    ]
})

print(response)