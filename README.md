# AI Receptionist

A reusable, multi-tenant AI receptionist backend designed to handle
after-hours calls, answer basic questions, and eventually manage
appointment scheduling.

## Current Goal

Build a working voice-agent backend capable of:

1. Receiving an incoming phone call
2. Establishing a call session
3. Converting speech to text
4. Generating an AI response
5. Converting the response to speech
6. Maintaining a short conversational context

## Week 1 Goal

A caller can have a 30–60 second natural conversation with the AI receptionist.

## Initial Stack

- Python
- FastAPI
- PostgreSQL / Supabase
- Retell AI
- Gemini / inexpensive LLM
- Redis — only if justified