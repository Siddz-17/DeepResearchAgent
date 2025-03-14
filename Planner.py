from agno.agent import Agent
from agno.models.groq import Groq

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
def QueryTake(query):
    
    des = """This agent systematically breaks down the steps of the query recieved and provides a structured response which contains the 
    steps to be followed if One has to research on the topic.
    Do not include any sub steps after specifying the main steps.
    State only the steps, i.e, the main points to be followed.
    Do not start with statements like: "Here's a structured approach to researching "Aloo Fry":".
    Dive straight to the points.┃
    """
    PlannerAgent = Agent(
        name = "PlannerAgent",
        model = Groq(id="gemma2-9b-it"),
        description = des,
        markdown = False
    )

    PlannerAgent