from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, Field


class MessageContentText(BaseModel):
    """Text content block"""

    type: Literal["text"]
    text: str


class MessageContentImage(BaseModel):
    """Image content block"""

    type: Literal["image"]
    source: Dict[str, str]  # Contains type, media_type, data (base64)


class MessageContentDocument(BaseModel):
    """Document content block (PDF)"""

    type: Literal["document"]
    source: Dict[str, str]  # Contains type, media_type, data (base64)


class MessageContentToolUse(BaseModel):
    """Tool use content block"""

    type: Literal["tool_use"]
    id: str
    name: str
    input: Dict[str, Any]


class MessageContentToolResult(BaseModel):
    """Tool result content block"""

    type: Literal["tool_result"]
    tool_use_id: str
    content: Union[str, List[Dict[str, Any]]]
    is_error: Optional[bool] = False


# Union type for all content types
MessageContent = Union[
    MessageContentText,
    MessageContentImage,
    MessageContentDocument,
    MessageContentToolUse,
    MessageContentToolResult,
    str,  # Simple string content
]


class MessageSchema(BaseModel):
    """Individual message in the conversation"""

    role: Literal["user", "assistant"]
    content: Union[str, List[MessageContent]]


class ToolInputSchema(BaseModel):
    """Schema for tool input parameters"""

    type: Literal["object"]
    properties: Dict[str, Any]
    required: Optional[List[str]] = None


class ToolSchema(BaseModel):
    """Tool definition"""

    name: str
    description: str
    input_schema: ToolInputSchema


class AnthropicChatDataSchema(BaseModel):
    """Chat Data Schema for Anthropic Messages API"""

    messages: List[MessageSchema]
    model: str = Field(
        default="claude-sonnet-4-20250514", description="Model identifier"
    )
    max_tokens: int = Field(
        default=1024, ge=1, le=8192, description="Maximum tokens to generate"
    )
    system: Optional[Union[str, List[Dict[str, str]]]] = Field(
        default=None, description="System prompt"
    )
    temperature: Optional[float] = Field(
        default=1.0, ge=0.0, le=1.0, description="Sampling temperature"
    )
    tools: Optional[List[ToolSchema]] = Field(
        default=None, description="Available tools for the model"
    )
    tool_choice: Optional[
        Union[
            Literal["auto", "any"],
            Dict[str, str],  # {"type": "tool", "name": "tool_name"}
        ]
    ] = None
    top_p: Optional[float] = Field(default=None, ge=0.0, le=1.0)
    top_k: Optional[int] = Field(default=None, ge=0)
    stop_sequences: Optional[List[str]] = None
    stream: Optional[bool] = False
    metadata: Optional[Dict[str, Any]] = None


class ResponseContentBlock(BaseModel):
    """Response content block"""

    type: str
    text: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    input: Optional[Dict[str, Any]] = None


class CacheCreation(BaseModel):
    """Cache creation information"""

    ephemeral_5m_input_tokens: int = 0
    ephemeral_1h_input_tokens: int = 0


class Usage(BaseModel):
    """Token usage information"""

    input_tokens: int
    output_tokens: int
    cache_creation_input_tokens: Optional[int] = 0
    cache_read_input_tokens: Optional[int] = 0
    cache_creation: Optional[CacheCreation] = None
    service_tier: Optional[str] = None


class MessageResponseSchema(BaseModel):
    """Response from Anthropic Messages API"""

    id: str
    type: Literal["message"]
    role: Literal["assistant"]
    content: List[ResponseContentBlock]
    model: str
    stop_reason: Optional[str] = None
    stop_sequence: Optional[str] = None
    usage: Usage
