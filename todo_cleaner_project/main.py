from crewai import Crew
from agents import (
    parser_agent, categorizer_agent, prioritizer_agent,
    get_parser_task, get_categorizer_task, get_prioritizer_task
)
import json

def extract_output(output):
    # CrewOutput object — convert to string
    if hasattr(output, "result") and isinstance(output.result, str):
        return output.result
    return str(output)

def run_pipeline(user_input):
    # Step 1: Parse tasks
    parser_task = get_parser_task(parser_agent, user_input)
    crew1 = Crew(agents=[parser_agent], tasks=[parser_task], verbose=True)
    parsed_result = extract_output(crew1.kickoff())

    # Step 2: Categorize tasks
    categorizer_task = get_categorizer_task(categorizer_agent, parsed_result)
    crew2 = Crew(agents=[categorizer_agent], tasks=[categorizer_task], verbose=True)
    categorized_result = extract_output(crew2.kickoff())

    # Step 3: Prioritize tasks
    prioritizer_task = get_prioritizer_task(prioritizer_agent, categorized_result)
    crew3 = Crew(agents=[prioritizer_agent], tasks=[prioritizer_task], verbose=True)
    prioritized_result = extract_output(crew3.kickoff())

    # Try parsing the string into a list of dicts if it's valid
    try:
        result_data = eval(prioritized_result)
        return json.dumps(result_data, indent=2)
    except:
        return json.dumps({"result": prioritized_result}, indent=2)
