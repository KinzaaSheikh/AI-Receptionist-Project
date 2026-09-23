from retell import Retell

from app.config import RETELL_API_KEY


client = Retell(api_key=RETELL_API_KEY)


def create_receptionist():

    llm = client.llm.create(
        start_speaker="agent",
        begin_message=(
            "Thanks for calling. "
            "How can I help you today?"
        ),
        general_prompt="""
You are an after-hours receptionist.

Your responsibilities:

- Answer basic questions about the business.
- Collect the caller's name.
- Collect their callback number when needed.
- Understand why they are calling.
- Help with scheduling when appropriate.
- Be polite, concise, and conversational.
- Ask one question at a time.
- Never invent information.
- If you do not know something, say that the office will follow up.
""".strip(),
    )

    print(f"Created Retell LLM: {llm.llm_id}")

    agent = client.agent.create(
        agent_name="After Hours Receptionist",
        response_engine={
            "type": "retell-llm",
            "llm_id": llm.llm_id,
        },
        voice_id="retell-Willa",
        language="en-US",
    )

    print(f"Created agent: {agent.agent_id}")
    print(f"Version: {agent.version}")


if __name__ == "__main__":
    create_receptionist()