
"""
Comprehensive manual type stubs for LangChain patterns.
Generated automatically for better IDE support.
"""

from typing import Any, Dict, List, Optional, Sequence, Union, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage, ToolMessage
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import BaseTool


class AgentState(TypedDict):
    """Agent state for LangChain agents."""
    messages: Sequence[BaseMessage]
    user_id: Optional[str]
    session_id: Optional[str]


class InputAgentState(TypedDict):
    """Input state schema for agent invocation."""
    messages: Sequence[Union[BaseMessage, Dict[str, Any]]]


# Agent creation and invocation
def create_agent(
    model: str,
    tools: Sequence[BaseTool],
    system_prompt: Optional[str] = None,
    max_tokens: Optional[int] = None,
    temperature: Optional[float] = None,
    **kwargs: Any
) -> Any:
    """Create a LangChain agent."""
    ...


def invoke_agent(
    input: Union[Dict[str, Any], InputAgentState],
    config: Optional[RunnableConfig] = None
) -> Dict[str, Any]:
    """Invoke a LangChain agent."""
    ...


# Message creation functions
def HumanMessage(
    content: Union[str, List[Dict[str, Any]]],
    **kwargs: Any
) -> Any:
    """Create a human message."""
    ...


def AIMessage(
    content: Union[str, List[Dict[str, Any]]],
    tool_calls: Optional[List[Dict[str, Any]]] = None,
    **kwargs: Any
) -> Any:
    """Create an AI message."""
    ...


def SystemMessage(
    content: Union[str, List[Dict[str, Any]]],
    **kwargs: Any
) -> Any:
    """Create a system message."""
    ...


def ToolMessage(
    content: Union[str, List[Dict[str, Any]]],
    tool_call_id: str,
    **kwargs: Any
) -> Any:
    """Create a tool message."""
    ...


# Tool-related types
class ToolCall(TypedDict):
    """Tool call structure."""
    name: str
    args: Dict[str, Any]
    id: str


def tool(func: Any) -> BaseTool:
    """Decorator to create a tool from a function."""
    ...


# Configuration types
class RunnableConfig(TypedDict, total=False):
    """Configuration for runnable objects."""
    configurable: Optional[Dict[str, Any]]
    recursion_limit: Optional[int]
    tags: Optional[List[str]]
    metadata: Optional[Dict[str, Any]]


# Common patterns for agent responses
class AgentResponse(TypedDict):
    """Standard agent response structure."""
    messages: Sequence[BaseMessage]
    output: Optional[str]
    tool_calls: Optional[List[ToolCall]]


# Helper functions
def bind_tools(
    model: Any,
    tools: Sequence[BaseTool]
) -> Any:
    """Bind tools to a model."""
    ...


def get_state(
    agent: Any,
    config: Optional[RunnableConfig] = None
) -> Any:
    """Get the current state of an agent."""
    ...


# Type aliases for better readability
MessageList = Sequence[BaseMessage]
ToolList = Sequence[BaseTool]
ConfigDict = Dict[str, Any]
