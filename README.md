# Crew_AI
# Collaborative Multi-Agent System with CrewAI

A modular, production-grade Python application utilizing CrewAI to orchestrate a team of independent AI agents collaborating sequentially to solve research and content generation tasks.

## 📁 Repository Map
* `main.py`: The entry point script configuring variables and executing the pipeline.
* `agents.py`: Structural architecture defining agent identities, models, and constraints.
* `tasks.py`: Positional logic outlining concrete steps, deliverables, and hand-offs.
* `tools.py`: External tool integrations.

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.10 to 3.13 installed in your environment.

### 2. Installation
```bash
git clone <your-github-repo-url>
cd my-crewai-project
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
