import requests
from schemas import *


def test():
    url = "http://localhost:8000/api/v1/chats"

    chat_data = AnthropicChatDataSchema(
        messages=[MessageSchema(role="user", content="Hello, how are you?")]
    )

    headers = {"Content-Type": "application/json"}

    response = requests.post(
        url, json=chat_data.model_dump(exclude_none=True), headers=headers
    )
    print(response.text)


if __name__ == "__main__":
    test()
