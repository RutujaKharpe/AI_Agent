# 📄 agents.py
import os
from crewai import Agent, Task, LLM

# ✅ Gemini LLM setup (Free API key)
os.environ["GOOGLE_API_KEY"] = "AIzaSyDNy5YDgsBa5PiojMnDlRAxr5M_bBJ1Wfo"
llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.environ["GOOGLE_API_KEY"]
)

# ✅ Agents
parser_agent = Agent(
    role="Parser Agent",
    goal="Extract tasks from user input",
    backstory="Expert in parsing messy input into structured tasks.",
    llm=llm,
    verbose=True
)

categorizer_agent = Agent(
    role="Categorizer Agent",
    goal="Tag each task with Work, Personal, or Urgent",
    backstory="Skilled at understanding task context.",
    llm=llm,
    verbose=True
)

prioritizer_agent = Agent(
    role="Prioritizer Agent",
    goal="Assign High, Medium, or Low priority to tasks",
    backstory="Knows how to rank tasks by urgency and importance.",
    llm=llm,
    verbose=True
)

# ✅ Task generators
def get_parser_task(agent, user_input):
    return Task(
        description=f"Extract a list of clean tasks from: '{user_input}'",
        expected_output="['task1', 'task2', ...]",
        agent=agent
    )

def get_categorizer_task(agent, task_list):
    return Task(
        description=f"Categorize tasks as Work, Personal, or Urgent: {task_list}",
        expected_output="[{{'task': '...', 'tags': ['...']}}]",
        agent=agent
    )

def get_prioritizer_task(agent, categorized_tasks):
    return Task(
        description=f"Assign priority (High, Medium, Low) to: {categorized_tasks}",
        expected_output="[{{'task': '...', 'tags': [...], 'priority': '...'}}]",
        agent=agent
    )
