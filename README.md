# Job Search Agent 🤖

An AI-powered job search agent designed and built by **Biruk Tensae**.

## What It Does
This is an intelligent AI agent that helps users navigate their job search. It can:
- Recommend jobs based on your skills and background
- Help write and improve resumes and cover letters
- Prepare you for interviews with targeted advice
- Provide career guidance and actionable next steps

## How It Works
The agent is powered by Claude (Anthropic) and maintains conversation memory, meaning it remembers context throughout your session and gives increasingly personalized advice the more you share.

## Tech Stack
- **Backend**: Python, FastAPI, Anthropic Claude API
- **Frontend**: React
- **AI**: Claude claude-sonnet-4-5 via Anthropic API

## Running Locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install anthropic fastapi uvicorn
export ANTHROPIC_API_KEY=your_key_here
uvicorn main:app --reload
```

## About
This agent was designed and built by Biruk Tensae as a portfolio project demonstrating hands-on experience with AI agent development, API integration, and full-stack development.
