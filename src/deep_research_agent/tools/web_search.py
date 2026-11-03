from langchain.tools import tool 
from langchain_tavily import TavilySearch 

@tool
def web_search(query: str) -> dict:
    """Search the web for current information or external evidence.

    Use a focused search query. Returns source titles, URLs,
    and content snippets for evaluating and citing findings.
    """
    search = TavilySearch(
        max_results=3,
        topic="general",
        search_depth="basic",
        include_answer=False,
        include_raw_content=False
    )
    
    return search.invoke({"query": query})