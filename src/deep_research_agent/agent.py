from pathlib import Path
from deepagents import create_deep_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from deepagents.backends import FilesystemBackend
from dotenv import load_dotenv

from deep_research_agent.prompts import SYSTEM_PROMPT
from deep_research_agent.tools import web_search

load_dotenv()

# Constants ===
PROJECT_ROOT = Path(__file__).resolve().parents[2]
WORKSPACE_DIR = PROJECT_ROOT / "workspace"
WORKSPACE_DIR.mkdir(exist_ok=True)


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
            tools=[web_search, *mcp_tools],
            backend=FilesystemBackend(
                root_dir=str(WORKSPACE_DIR),
                virtual_mode=True
            )
        )