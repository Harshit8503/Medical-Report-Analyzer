## Medical Report Analyzer ##

Firstly decided to create three agents:-
Analyzer : analyzer is responsible to take the report file and summarize its context in a easy to understand manner.
Web_Searcher: This agent is responsible to search the web for relevant health concerns article after the analysis of the blood report.It needs to search down the queries to find the right articles and provide suitable links.
Recommender: It uses the queries or links and give the health recommendations related to the concerns after analysis of the report.It gives a more detailed summary of all the recommendations and provide links of the articles used to carry our the search.

Tool used to undertake this project:- Google Serpent(used for fast searching)
LLM used: Google gemini

After creating the work pipeline with Crew then simply model is commanded to proceed after giving the desired input file.

# Steps to Run the code
1. Need to create an python(3.11) environment.
2. Need to install libraries from requirements.txt
3. Create a Google API key
4. Create a Serpent Google API key
5. Declare them in a .env file
6. Run the crew.py file 