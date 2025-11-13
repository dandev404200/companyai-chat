import json
import os
from http import HTTPStatus
from typing import Dict, List

import requests
from fastapi import APIRouter
from pydantic import BaseModel
from schemas import *
from starlette.responses import Response

router = APIRouter()


@router.get("/")
async def get_routes():
    return {"message": "/chats is available"}


@router.post(
    "/chats", response_model=MessageResponseSchema, status_code=HTTPStatus.CREATED
)
async def create_chat(chat_data: AnthropicChatDataSchema):
    """Create a new chat"""
    # Here you would typically save the chat to a database
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": os.environ["ANTHROPIC_API_KEYpoop"],
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json",
    }
    response = requests.post(
        url, json=chat_data.model_dump(exclude_none=True), headers=headers
    )
    response.raise_for_status()
    return response.json()
