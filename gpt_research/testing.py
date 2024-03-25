from gpt_researcher import GPTResearcher
import asyncio
from dotenv import load_dotenv

load_dotenv()

async def get_report(query: str, report_type: str) -> str:
    researcher = GPTResearcher(query, report_type)
    report = await researcher.run()
    return report

if __name__ == "__main__":
    query = "What specific news and world events impacted the performance of the Toronto Stock Exchange index from 2023 January 1st to 2023 December 31st"
    report_type = "research_report"

    report = asyncio.run(get_report(query, report_type))
    
    print("###################")
    print(report)