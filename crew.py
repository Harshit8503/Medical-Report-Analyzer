from crewai import Crew,Process
from tasks import analyzer_task,recommender_task,searcher_task
from agents import report_analyzer,web_searcher,recommender
import os
crew=Crew(
    agents=[report_analyzer,web_searcher,recommender],
    tasks=[analyzer_task,searcher_task,recommender_task],
    process=Process.sequential,
)

result=crew.kickoff(inputs={'text':os.getenv("report")})
print(result)