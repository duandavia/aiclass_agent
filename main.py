from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_core.memory import ListMemory
from autogen_core.models import ModelFamily
import os
from dotenv import load_dotenv
import asyncio
import output_agent

load_dotenv()

# Define a model client. You can use other model client that implements
# the `ChatCompletionClient` interface.
model_client = OpenAIChatCompletionClient(
    model="deepseek-reasoner",
    base_url="https://api.deepseek.com",
    api_key=os.getenv("Deepseek_API_KEY"),
    model_info={
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "family": ModelFamily.R1,
        "structured_output": True
    }
)

team_memory = ListMemory()

OutputAgent = output_agent.create_output_agent(model_client, team_memory)

team = RoundRobinGroupChat([OutputAgent],max_turns=5)

async def run_team(task, team):
    stream = team.run_stream(task=task)
    await Console(stream=stream)
    await model_client.close()

if __name__ == "__main__":
    eg_task = "分析一下港股恒生指数的走势"
    asyncio.run(run_team(eg_task, team))
