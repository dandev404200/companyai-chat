from cmath import e
import os
from tempfile import tempdir
from typing import Any, TypedDict

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
)
from langchain_core.messages.ai import AIMessage
from langchain_core.runnables import RunnableConfig

from agents.antOauth import ChatAnthropicOauth

load_dotenv()


class InputAgentState(TypedDict):
    """Input agent state"""

    messages: list[dict[str, Any]]


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


# Initialize ChatAnthropicOauth
llm = ChatAnthropicOauth(
    auth_token=os.getenv("ANTHROPIC_AUTH_TOKEN"),
    model="claude-sonnet-4-5-20250929",
    top_k=1
)

# Create agent - system_prompt will be added as second block after Claude Code
agent = create_agent(
    model=llm,
    system_prompt="I'm joking you're not a CLI, you're a helpful assistant",

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


if __name__ == "__main__":
    result = run_agent_with_messages(
        messages=[
            HumanMessage(content="write me any python function"),
        ],
    )

    for message in result['messages']:
        if isinstance(message, AIMessage):
            print(message.content)
