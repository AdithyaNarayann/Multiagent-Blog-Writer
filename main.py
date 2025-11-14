from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

api_key = os.getenv("API_KEY")
os.environ["GOOGLE_API_KEY"] = api_key

from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LoopAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import AgentTool, FunctionTool, google_search
from google.genai import types

retry_config=types.HttpRetryOptions(
    attempts=5,  
    exp_base=7,  
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)

outline_agent = Agent(
    name="OutlineAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction="""Create a blog outline for the given topic with:
    1. A catchy headline
    2. An introduction hook
    3. 3-5 main sections with 2-3 bullet points for each
    4. A concluding thought""",
    output_key="blog_outline",  
)


writer_agent = Agent(
    name="WriterAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction="""Following this outline strictly: {blog_outline}
    Write a brief, 200 to 300-word blog post with an engaging and informative tone.""",
    output_key="blog_draft", 
)

editor_agent = Agent(
    name="EditorAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction="""Edit this draft: {blog_draft}
    Your task is to polish the text by fixing any grammatical errors, improving the flow and sentence structure, and enhancing overall clarity.""",
    output_key="final_blog", 
)

root_agent = SequentialAgent(
    name="BlogPipeline",
    sub_agents=[outline_agent, writer_agent, editor_agent],
)

runner = InMemoryRunner(agent=root_agent, app_name="AutoBlogWriter")

async def main():
    while True:
        prompt = input("Enter a blog topic (or 'exit' to quit): ")
        if prompt.lower() == 'exit':
            break   
        else:
            response = await runner.run_debug(prompt)
            
asyncio.run(main())

