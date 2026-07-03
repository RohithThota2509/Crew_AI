from dotenv import load_dotenv
from crewai_tools import ScrapeWebsiteTool

load_dotenv()
scrape_tool = ScrapeWebsiteTool()