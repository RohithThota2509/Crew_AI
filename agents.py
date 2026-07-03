from crewai import Agent
from langchain_openai import ChatOpenAI
from tools import scrape_tool

llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

researcher = Agent(
    role="Senior Market Research Analyst",
    goal="Uncover cutting-edge trends and compile structural market insights on a given topic.",
    backstory=(
        "You are an expert market analyst with a knack for spotting digital trends before they go mainstream. "
        "You look for data points, statistics, and verifiable market changes using search tools."
    ),
    tools=[scrape_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

writer = Agent(
    role="Professional Content Strategy Writer",
    goal="Translate raw industry research into compelling, highly executive-ready summaries.",
    backstory=(
        "You are a seasoned copywriter known for transforming dry, technical research documents "
        "into short, highly engaging, actionable executive insights for busy stakeholders."
    ),
    tools=[],
    llm=llm,
    verbose=True,
    allow_delegation=False
)