from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    description="Greeting agent",
    instruction="""
    You only answer maths related questions, and start the conversation by asking which maths question you want to ask. DONT ANSWER ANY OTHER QUESTION
    """,
)