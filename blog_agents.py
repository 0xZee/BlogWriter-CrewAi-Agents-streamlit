import streamlit as st
from crewai import Agent
from langchain_groq import ChatGroq
#from blog_tools import DuckSearchTool
from DuckSearchTools import DuckSearchTool
import re


# AGENTS
class BlogAgents():

    def __init__(self, model_name):
        self.model_name = model_name

    def llm(self):
        #self.model_name = model_name
        #llm = ChatGroq(model="gemma2-9b-it", temperature=0.2, api_key=st.secrets['GROQ_API']) # model="llama3-70b-8192" , "gemma2-9b-it" , "mixtral-8x7b-32768"
        llm = ChatGroq(model=self.model_name, temperature=0.2, api_key=st.secrets['GROQ_API'])
        return llm

    # Financial expert
    def editor_agent(self):
        return Agent(
            role="Blog Editor",
            goal="Uncover main information and insights about {topic}",
            #goal="Uncover the last news and trends about {topic}",
            backstory="""You work at famous blog editor.
            Higly skilled in collecting informations and outlookds for {topic}
            """,
            verbose=True,
            memory=True,
            max_iter=4,
            allow_delegation=False,
            tools=[DuckSearchTool.web_search],
            llm = self.llm(),
        )

    # reporter expert
    def writer_agent(self):
        return Agent(
            role="Blog Writer",
            goal="Craft compelling and detailed Blog on {topic} based on a collection of related articles",
            backstory="""You are a renowned Content Writer for {topic}, known for your insightful and engaging articles.
          You transform complex concepts into compelling narratives.""",
            verbose=True,
            memory=True,
            max_iter=5,
            allow_delegation=False,
            #tools=[DuckSearchTool.web_search],
            llm = self.llm()
        )




class StreamToExpander:
    # Print agent process to Streamlit app container 
    # This portion of the code is adapted from @AbubakrChan; thank you!  

    def __init__(self, expander):
        self.expander = expander
        self.buffer = []
        self.colors = ['red', 'green', 'blue', 'orange']  # Define a list of colors
        self.color_index = 0  # Initialize color index

    def write(self, data):
        # Filter out ANSI escape codes using a regular expression
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)

        # Check if the data contains 'task' information
        task_match_object = re.search(r'\"task\"\s*:\s*\"(.*?)\"', cleaned_data, re.IGNORECASE)
        task_match_input = re.search(r'task\s*:\s*([^\n]*)', cleaned_data, re.IGNORECASE)
        task_value = None
        if task_match_object:
            task_value = task_match_object.group(1)
        elif task_match_input:
            task_value = task_match_input.group(1).strip()

        if task_value:
            st.toast(":robot_face: " + task_value)

        # Check if the text contains the specified phrase and apply color
        if "Entering new CrewAgentExecutor chain" in cleaned_data:
            # Apply different color and switch color index
            self.color_index = (self.color_index + 1) % len(self.colors)  # Increment color index and wrap around if necessary

            cleaned_data = cleaned_data.replace("Entering new CrewAgentExecutor chain", f":{self.colors[self.color_index]}[Entering new CrewAgentExecutor chain]")

        if "City Selection Expert" in cleaned_data:
            # Apply different color 
            cleaned_data = cleaned_data.replace("City Selection Expert", f":{self.colors[self.color_index]}[City Selection Expert]")
        if "Local Expert at this city" in cleaned_data:
            cleaned_data = cleaned_data.replace("Local Expert at this city", f":{self.colors[self.color_index]}[Local Expert at this city]")
        if "Amazing Travel Concierge" in cleaned_data:
            cleaned_data = cleaned_data.replace("Amazing Travel Concierge", f":{self.colors[self.color_index]}[Amazing Travel Concierge]")
        if "Finished chain." in cleaned_data:
            cleaned_data = cleaned_data.replace("Finished chain.", f":{self.colors[self.color_index]}[Finished chain.]")

        self.buffer.append(cleaned_data)
        if "\n" in data:
            self.expander.markdown(''.join(self.buffer), unsafe_allow_html=True)
            self.buffer = []
