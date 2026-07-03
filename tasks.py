from crewai import Task
from agents import researcher, writer

research_task = Task(
    description=(
        "Read and extract key insights from the following industry webpage: "
        "'https://en.wikipedia.org/wiki/Multi-agent_system'. "
        "Identify the top 3 core structural concepts and explain why they matter."
    ),
    expected_output="A detailed bullet-point intelligence report containing the core architectural takeaways.",
    agent=researcher
)

write_task = Task(
    description=(
        "Review the market analysis provided by the research team. "
        "Synthesize the findings into a clear, compelling 3-paragraph executive briefing. "
        "Ensure it highlights practical action items and uses an engaging tone."
    ),
    expected_output="A beautifully formatted 3-paragraph market brief markdown document.",
    agent=writer,
    output_file="market_briefing.md"
)