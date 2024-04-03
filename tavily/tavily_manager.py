from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

class Tavily:
    def __init__(self):
        self.tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    
    def search(self, query: str, search_depth: str = "advanced", max_results: int = 5) -> list[dict[str, str]]:
        """
        Perform search.
        
        :param query: The query.
        :param search_depth: You detailed you want to search. If using advanced, they will use reranking to improve results quality.
        :param max_results: How many results you want.
        """
        response = self.tavily.search(query=query, search_depth=search_depth, include_raw_content=True, max_results=max_results)
        return [{"title": web_content["title"], "url": web_content["url"], "content": web_content["content"]} for web_content in response["results"]]
    
    def search_url(self, query: str, search_depth: str = "advanced", max_results: int = 30) -> list[str]:
        """
        Perform search and return urls.
        
        :param query: The query to search for.
        :param search_depth: You detailed you want to search. If using advanced, they will use reranking to improve results quality.
        :param max_results: How many results you want.
        """
        response = self.tavily.search(query=query, search_depth=search_depth, include_raw_content=True, max_results=max_results)
        return [web_content["url"] for web_content in response["results"]]
    
    def ask(self, query: str) -> str:
        """
        Ask a question and get the answer.
        
        :param query: Your question.
        :return: The answer.
        """
        return self.tavily.qna_search(query)
    
tavily = Tavily()
print(tavily.search_url("What is the weather today?"))