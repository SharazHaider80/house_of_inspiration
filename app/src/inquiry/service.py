from src.llm_provider.openai_client import get_langchain_llm
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_core.tools import tool
from src.llm_provider.openai_client import get_langchain_llm
from src.tools.tools import tools
from langchain.schema.messages import SystemMessage
from langchain.memory import ConversationBufferMemory

# ---------- AGENT FUNCTION ----------
# Define system message
SYSTEM_MESSAGE = SystemMessage(
    content="""
You are a knowledgeable and empathetic assistant for the Home of Inspiration/HOI website.

Your purpose is to help users:
- Understand who Ester is and what she stands for
- Learn about the vision behind the Home of Inspiration
- Discover the energy and intention behind the space
- Get practical guidance on how to engage with or use the space

Use the provided internal knowledge (such as "Über mich" and other page content) to answer questions clearly, helpfully, and with warmth.

For each user query:
- Explain *what* they’re asking about using accurate and relevant content
- If appropriate, guide them on *how* they can take action (e.g., book, contact, visit, reflect)
- If the question goes beyond the available information, respond with:
  “Leider habe ich dazu keine Informationen.”

Keep your tone clear, supportive, and inspiring — aligned with Ester’s values of authenticity, clarity, and emotional resonance.

"""
)

# Initialize memory for chat history
memory = ConversationBufferMemory(
    memory_key="chat_history",  # key under which the history is stored
    return_messages=True       # return list of messages objects
)

def generate_llm_response(query: str) -> str:
   
    try:
        llm = get_langchain_llm()

        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            agent_kwargs={
                "system_message": SYSTEM_MESSAGE
            },
            memory=memory,
            verbose=True,
            handle_parsing_errors=True
        )

        # Run the agent with the new query; memory updates automatically
        response = agent.run(query)

        return response

    except Exception as e:
        raise Exception(f"Failed to generate LLM response with tools and system prompt: {e}")


def get_chat_history() -> list:
    """
    Retrieve the current conversation history.

    Returns:
        list: List of message objects representing the chat history.
    """
    # memory.chat_memory.messages is list of BaseMessage
    return memory.load_memory_variables({}).get("chat_history", [])
