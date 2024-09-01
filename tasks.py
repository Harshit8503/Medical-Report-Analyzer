from crewai import Task
from tools import search_tool
from agents import report_analyzer,web_searcher,recommender

#analyzer task 
 
analyzer_task=Task(
    description=(
       "Take all the content from the paragraph {text}"
       "Get all detailed information from this blood report"
       "Summarize the whole report"
    ),
    expected_output="A summarization of whole report containing all the health data making sure that it is easy to read",
    tools=[],
    agent=report_analyzer,
    async_execution=False,
) 
searcher_task=Task(
    description=(
       "On the basis of report ,search for relevant health articles and provide their links"
    ),
    expected_output="Generate search queries related to the identified health concerns and retrieve articles that are relevant to the person’s health needs.Relevant links related to the blood reports of about 5-6 articles on web ",
    tools=[search_tool],
    async_execution=False,
    agent=web_searcher,
) 
recommender_task=Task(
    description=(
       "Search the links and summarize all the relevant articles to provide health recommendations based on the report"
    ),
    expected_output="A 2-3 page summary of the articles and health recommendations based on the report with relevant article links",
    tools=[search_tool],
    async_execution=False,
    agent=recommender,
) 
