from typing import Any
from langchain_anthropic import ChatAnthropic

# Claude Code system prompt - required for OAuth credentials
CLAUDE_CODE_SYSTEM_PROMPT = "You are Claude Code, Anthropic's official CLI for Claude."


class ChatAnthropicOauth(ChatAnthropic):
    """
    ChatAnthropic with OAuth token authentication support.

    Identical to ChatAnthropic in all ways except:
    1. Uses OAuth token (auth_token) instead of API key
    2. Automatically includes required OAuth beta headers
    3. Always prepends Claude Code system prompt as first block

    Use this as a drop-in replacement for ChatAnthropic when using OAuth credentials.
    """

    def __init__(
        self,
        *,
        auth_token: str,
        model: str = "claude-sonnet-4-5-20250929",
        **kwargs,
    ):
        """
        Initialize ChatAnthropic with OAuth token authentication.

        Args:
            auth_token: OAuth token for authentication (replaces api_key)
            model: Model name (default: claude-sonnet-4-5-20250929)
            **kwargs: All other arguments identical to ChatAnthropic
                     (max_tokens, temperature, streaming, timeout, model_kwargs, etc.)

        Examples:
            # Basic usage (identical to ChatAnthropic)
            chat = ChatAnthropicOauth(auth_token="token")
            response = chat.invoke([HumanMessage(content="Hello")])

            # With custom parameters (identical to ChatAnthropic)
            chat = ChatAnthropicOauth(
                auth_token="token",
                model="claude-sonnet-4-5-20250929",
                max_tokens=4096,
                temperature=0.7,
                streaming=True
            )

            # With LangChain agents (identical to ChatAnthropic)
            from langchain.agents import create_tool_calling_agent
            agent = create_tool_calling_agent(
                llm=ChatAnthropicOauth(auth_token="token"),
                tools=[tool1, tool2],
                prompt=prompt
            )

            # Add custom system prompts (as additional blocks after Claude Code)
            chat = ChatAnthropicOauth(
                auth_token="token",
                model_kwargs={"system": "You are an expert in Python."}
            )
        """
        # Set up OAuth-specific beta headers
        betas = "oauth-2025-04-20,claude-code-20250219,interleaved-thinking-2025-05-14,fine-grained-tool-streaming-2025-05-14"

        # Merge with any provided default headers
        default_headers = kwargs.pop("default_headers", {})
        default_headers.update(
            {
                "anthropic-beta": betas,
                "anthropic-version": "2023-06-01",
            }
        )

        # Handle system prompt: Claude Code is ALWAYS first block
        model_kwargs = kwargs.pop("model_kwargs", {})
        additional_system = model_kwargs.pop("system", None)

        # Build system blocks with Claude Code as first block
        system_blocks = [{"type": "text", "text": CLAUDE_CODE_SYSTEM_PROMPT}]

        # Add any additional system blocks
        if additional_system:
            if isinstance(additional_system, str):
                system_blocks.append({"type": "text", "text": additional_system})
            elif isinstance(additional_system, list):
                system_blocks.extend(additional_system)

        # Use single string if only Claude Code, otherwise use block list
        final_system = (
            CLAUDE_CODE_SYSTEM_PROMPT if len(system_blocks) == 1 else system_blocks
        )
        model_kwargs["system"] = final_system

        # Initialize parent class (use placeholder api_key, will be overridden)
        super().__init__(
            api_key="placeholder",
            model=model,
            default_headers=default_headers,
            model_kwargs=model_kwargs,
            **kwargs,
        )

        # Store OAuth token after initialization to avoid Pydantic validation issues
        object.__setattr__(self, "_oauth_token", auth_token)

    @property
    def _client_params(self) -> dict[str, Any]:
        """Override client params to use OAuth token instead of api_key"""
        params = dict(super()._client_params)

        # Remove api_key if present and add auth_token instead
        if "api_key" in params:
            del params["api_key"]

        # Add OAuth token
        params["auth_token"] = self._oauth_token

        return params

    def bind(self, **kwargs: Any) -> Any:
        """
        Override bind to handle system prompts as additional blocks.

        When create_agent or other LangChain components call .bind(system=...),
        we need to add it as a second block after Claude Code, not replace it.
        """
        # Extract system prompt from bind kwargs
        bound_system = kwargs.pop("system", None)

        if bound_system:
            # Get current system from model_kwargs
            current_system = self.model_kwargs.get("system")

            # Build new system with Claude Code first, then bound system
            if (
                isinstance(current_system, str)
                and current_system == CLAUDE_CODE_SYSTEM_PROMPT
            ):
                # Currently just Claude Code, add bound system as second block
                new_system = [
                    {"type": "text", "text": CLAUDE_CODE_SYSTEM_PROMPT},
                    {"type": "text", "text": bound_system},
                ]
            elif isinstance(current_system, list):
                # Already have multiple blocks, add to the end
                new_system = current_system + [{"type": "text", "text": bound_system}]
            else:
                # Fallback: just use what we have
                new_system = current_system

            # Update kwargs with new system
            kwargs["system"] = new_system

        # Call parent bind with modified kwargs
        return super().bind(**kwargs)
