from crewai import Agent
from tools import search_tool
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI


llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

# create a report analyzer 
# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
report_analyzer=Agent(
    role='Blood Report Analyzer ',
    goal='it should analyze the blood test report {text}, summarizing it in an easy-to-understand manner and also analyze related heath concerns.',
    verboe=True,
    memory=True,
    backstory=(
        "Expert in summarizing the whole blood report,identifying any parameter which should be low or high"
    ),
    tools=[],
    llm=llm,
    allow_delegation=True,

)
web_searcher=Agent(
    role='Web Searcher',
    goal="It should then search the web for articles tailored to the persons health needs based on the blood test results and provide links",
    verboe=True,
    memory=True,
    backstory=(
        "Expert in searching web content with relevant and accurate information"
    ),
    tools=[search_tool],
    llm=llm,
    allow_delegation=True,
)
recommender=Agent(
    role="health recommender",
    goal="it should give health recommendations based on the provided links to the relevant articles",
    verboe=True,
    memory=True,
    backstory=(
        "Expert in giving health related recommendations from each link"
    ),
    tools=[search_tool],
    llm=llm,
    allow_delegation=False,

)