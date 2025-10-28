from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_core.memory import ListMemory
from autogen_core.models import ModelFamily
import os
from dotenv import load_dotenv
import asyncio
import output_agent
import search_agent
import plotting_agent
import report_agent

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
# 创建团队记忆体，用于保持上下文
team_memory = ListMemory()
#创建各个智能体
OutputAgent = output_agent.create_output_agent(model_client, team_memory)
SearchAgent = search_agent.create_search_agent(model_client, team_memory)
PlottingAgent = plotting_agent.create_plotting_agent(model_client, team_memory)
ReportAgent = report_agent.create_report_agent(model_client, team_memory)
# 创建团队 - 按照README要求的顺序：搜索智能体、制图智能体、评论智能体、输出智能体
agent_team = RoundRobinGroupChat([SearchAgent, PlottingAgent, ReportAgent, OutputAgent], max_turns=6)
# 异步运行团队
async def test_team():
    eg_task = "分析一下港股恒生指数的走势"
    stream = agent_team.run_stream(task=eg_task)
    await Console(stream=stream)
    await model_client.close()

if __name__ == "__main__":
    asyncio.run(test_team())
