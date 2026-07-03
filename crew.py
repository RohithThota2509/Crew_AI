import os
from dotenv import load_dotenv
from crewai import Crew, Process
from tasks import research_task, write_task
from agents import researcher, writer

load_dotenv()

def run_crew():
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        verbose=True
    )
    
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: Please ensure OPENAI_API_KEY is configured in your environment or .env file.")
    else:
        run_crew()