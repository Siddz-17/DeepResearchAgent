from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model = Groq(id="qwen-2.5-32b"),
    description='You are assistant to help me with my research',
    tools=[DuckDuckGoTools()],
    markdown = True
    )
