from deepagents import create_deep_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

from dotenv import load_dotenv

from deep_research_agent.prompts import SYSTEM_PROMPT
from deep_research_agent.tools import web_search

load_dotenv()


async def build_agent():
    # (LLM) Large Language Model ---
    model = "openai:gpt-5.5"
    
    # MCP ---
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

    return create_deep_agent(
            model=model, 
            system_prompt=SYSTEM_PROMPT,
            tools=[web_search, *mcp_tools]
        )