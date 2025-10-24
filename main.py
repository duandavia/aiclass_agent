from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

# Define a model client. You can use other model client that implements
# the `ChatCompletionClient` interface.
model_client = OpenAIChatCompletionClient(
    model="deepseek-reasoner",
    base_url="https://api.deepseek.com",
    api_key="sk-048d248ce7844f8c9f9c325ace7743ba",
)