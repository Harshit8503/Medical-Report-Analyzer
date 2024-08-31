from crewai import Agent
from tools import pdf_tool
# create a report analyzer 

report_analyzer=Agent(
    role='Blood Report Analyzer from pdf file',
    goal='it should analyze the blood test report, summarizing it in an easy-to-understand manner.'
    verboe=True,
    memory=True,
    backstory=(
        "Expert in parsing the pdf and summarizes the whole blood report"
    ),
    tools=[pdf_tool],
    allow_delegation=True

)
web_searcher=Agent(
    role='Web Searcher',
    goal="It should then search the web for articles tailored to the persons health needs based on the blood test results",
    verboe=True,
    memory=True,
    backstory=(
        "Expert in searching web content with accurate information"
    ),
    tools=[],
    allow_delegation=True
)
recommender=Agent(
    role="health recommender",
    goal="it should give health recommendations and provide links to the relevant articles",
    verboe=True,
    memory=True,
    backstory=(
        "Expert in giving health related recommendations"
    ),
    tools=[],
    allow_delegation=True
)