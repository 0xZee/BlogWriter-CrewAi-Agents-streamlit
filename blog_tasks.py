from datetime import datetime
from crewai import Task
#DuckDuckGoSearchRunTool DuckDuckGoSearchResults DuckDuckGoSearchRun
from langchain_groq import ChatGroq
from blog_agents import BlogAgents




# TASKS
class BlogTasks():

    # Task: Location
    def editor_task(self, topic, agent):
        return Task(
            description=f"""This task involves collect 10 articles about {topic}
            Compile them into 10 rich articles. 
            Use recent_search tool and proceed with results you got.
            """,
            expected_output ="""
            In markdown format with sections and bullets : A rich blog post with the 10 articles, including URL sources.
            Use emojies in accordance in the beginings of the sections's titles.
            """,
            agent=agent,
            #output_file='blog_report_task_editor.md',
        )

    # Task: Location
    def writer_task(self, topic, agent, context):    
        return Task(
            description=f"""
            Develop a rich paragraphe about {topic} as an introduction.
            The, Compile the 10 articles from editor_agent in a long blog post with introduction and sections about {topic}.
            """,
            expected_output="""
            A rich structured blog post in markdown format.
            Use emojies in accordance in the beginings of the sections's titles.
            """,
            agent=agent,
            context=[context],
            #output_file='blog_report_task_writer.md',
        )

    # tip section
    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $1000 and grant you any wish you want!"

#
