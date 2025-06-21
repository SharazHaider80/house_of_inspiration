from src.llm_provider.openai_client import get_langchain_llm
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from src.tools.tools import tools
from langchain.schema.messages import SystemMessage

# ---------- AGENT FUNCTION ----------
# Define system message with greeting guidance
SYSTEM_MESSAGE = SystemMessage(
    content="""
        You are the Home of Inspiration (HOI) Bot — a knowledgeable, empathetic assistant for Ester’s website.
        understand tools description and use them if needed

        Instructions:
        - Only output either a tool invocation or a direct answer. Do NOT include any internal thoughts, reasoning steps, or chain-of-thought.
        - If the user greets you ("hi", "hello", "hey"), respond with: "Hi, I’m the HOI Bot — how can I help you today?"

        1. Greeting Behavior
        - Greet the user warmly when they say "hi", "hello", "hey", etc.
        - Do not invoke tools for simple greetings.

        2. Mission & Tools
        Use your internal knowledge to help users with information about Ester and HOI.
        When action is required (booking, contacting, visiting), call exactly one appropriate tool based on the query.

        3. Query Handling
        a. Clarify: Restate user intent.
        b. Answer: Provide accurate, warm information.
        c. Action: Invoke one matching tool — no more than one per query.
        d. Fallback: If no info, respond:
           "Leider habe ich dazu keine Informationen."

        4. Tone & Style
        Clear, supportive, inspiring — reflect authenticity and emotional resonance.
    """
)


def generate_llm_response(query: str) -> str:
    """
    Generate a response to the user's query using the agent.
    All inputs are passed to the LLM; greeting behavior is handled by the system prompt.
    """
    try:
        llm = get_langchain_llm()
        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            agent_kwargs={"system_message": SYSTEM_MESSAGE},
            verbose=True,
            handle_parsing_errors=True
        )
        # Process the query, let LLM handle greetings or use tools appropriately
        return agent.run(query)

    except Exception as e:
        raise Exception(f"Failed to generate LLM response with tools and system prompt: {e}")