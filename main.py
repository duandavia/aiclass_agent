from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv

load_dotenv()

# Define a model client. You can use other model client that implements
# the `ChatCompletionClient` interface.
model_client = OpenAIChatCompletionClient(
    model="deepseek-reasoner",
    base_url="https://api.deepseek.com",
    api_key=os.getenv("Deepseek_API_KEY"),
)