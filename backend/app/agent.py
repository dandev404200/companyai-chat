import json
from typing import Any, TypedDict

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
)
from langchain_core.runnables import RunnableConfig

load_dotenv()


class InputAgentState(TypedDict):
    """Input agent state"""

    messages: list[dict[str, Any]]


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_agent(
    model="claude-haiku-4-5-20251001",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)


def run_agent_with_messages(
    messages: list[BaseMessage], config: RunnableConfig | None = None
) -> dict:
    """
    Run agent with LangChain message objects.

    Args:
        messages: List of LangChain message objects
        config: Optional configuration for threading, recursion limits, etc.

    Returns:
        Dictionary containing all messages including the agent's response
    """
    return agent.invoke({"messages": messages}, config=config)


result = run_agent_with_messages(
    messages=[
        HumanMessage(content="What is the weather in San Francisco?"),
        AIMessage(content="It's always sunny in San Francisco!"),
    ]
)
print(json.dumps(result, indent=2))
