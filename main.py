from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import anthropic
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

conversation_history = []

class Message(BaseModel):
    message: str

@app.post("/chat")
def chat(msg: Message):
    conversation_history.append({
        "role": "user",
        "content": msg.message
    })

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1000,
        system="""You are a helpful job search agent. You help users with:
        - Finding jobs that match their skills
        - Writing resumes and cover letters
        - Interview preparation
        - Career advice
        Be specific, actionable, and encouraging.""",
        messages=conversation_history
    )

    reply = response.content[0].text

    conversation_history.append({
        "role": "assistant",
        "content": reply
    })

    return {"reply": reply}
