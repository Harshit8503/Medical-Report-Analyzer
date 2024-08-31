from crewai import Task
from tools import pdf_tool
from agents import report_analyzer,web_searcher,recommender

#analyzer task 
 
analyzer_task=Task(
    description=(
       "Take all the content from the pdf"
       "Get all detailed information from this blood report"
       "Summarize the whole report"
    )
    expected_output="A summarization of whole report containing all the health data from the pdf making sure that it is easy to read"
    tools=[pdf_tool],
    agent=report_analyzer,
) 
searcher_task=Task(
    description=(
       "On the basis of report search for "
    )
    expected_output="A summarization of whole report containing all the health data from the pdf making sure that it is easy to read"
    tools=[pdf_tool],
    agent=,
) 
