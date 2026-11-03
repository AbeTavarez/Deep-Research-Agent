from deepagents import create_deep_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

from dotenv import load_dotenv
import asyncio

from deep_research_agent.prompts import SYSTEM_PROMPT
from deep_research_agent.tools import web_search

load_dotenv()


async def main():
    # (LLM) Large Language Model
    model = "openai:gpt-5.5"
    
    mcp_client = MultiServerMCPClient({
        "fire_crawler": {
            "transport": "http",
            "url": "https://mcp.firecrawl.dev/v2/mcp"
        }
    })
    
    mcp_tools = await mcp_client.get_tools()
    
    print(f"\nFireCrawler: {len(mcp_tools)} tools")
    
    for tool in mcp_tools:
        print(f"Name: {tool.name}")
        print(f"\ndescription: {tool.description}")

    agent = create_deep_agent(
            model=model, 
            system_prompt=SYSTEM_PROMPT,
            tools=[web_search, *mcp_tools]
        )

    response = agent.invoke(
        {"messages": [{"role": "user", "content": "What's a micro controller?"}]}
    )

    print(response)

if __name__ == "__main__":
    asyncio.run(main())
