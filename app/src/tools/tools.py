from langchain_core.tools import tool
from langchain.agents import Tool
import json
import os

# ---------- Load JSON Once ----------
file_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../static/processed_docs_full_content.json")
)

try:
    with open(file_path, "r", encoding="utf-8") as f:
        docs = json.load(f)
except Exception as e:
    raise Exception(f"Failed to load knowledge base: {e}")

# ---------- Helper ----------
def get_doc_content(filename: str) -> str:
    for doc in docs:
        if doc["document"] == filename:
            return doc["content"]
    return ""

# ---------- TOOL 1 ----------
@tool
def search_database(query: str) -> str:
    """for greeting messages"""
    return f"Hi, iam HOI Bot. how can i help you?"

# ---------- TOOL 2 ----------
@tool
def uber_mich_info(query: str) -> str:
    """Answers questions about Ester, her personal journey, and the philosophy behind 'Home of Inspiration' from the document 'Über mich'."""
    content = get_doc_content("20250515_HoI Text_Über mich.docx")
    return content[:8000] if content else "Leider habe ich dazu keine Informationen."

# ---------- TOOL 3 ----------
@tool
def webpage_philosophy(query: str) -> str:
    """Provides insights from the main webpage text including vision, rental philosophy, and emotional tone of the place."""
    content = get_doc_content("20250515_HoI_Webpage Text.docx")
    return content[:8000]  if content else "Leider habe ich dazu keine Informationen."

# ---------- TOOL 4 ----------
@tool
def angebotsdetails(query: str) -> str:
    """Returns details about the offerings like Leermondzyklus and Herzraum, including structure, pricing, and spiritual context."""
    content = get_doc_content("20250526_Angebotsdetails.docx")
    return content[:8000]  if content else "Leider habe ich dazu keine Informationen."

# ---------- TOOL 5 ----------
@tool
def herzraum_hintergrund(query: str) -> str:
    """Explains Ester's deeper work, vision, values, target audience, and principles from the Herzraum background document."""
    content = get_doc_content("20250526_Herzraum_Angebotsstruktur und Hintergrund.docx")
    return content[:8000]  if content else "Leider habe ich dazu keine Informationen."

# ---------- TOOL 6 ----------
@tool
def mietinfo_retreathaus(query: str) -> str:
    """Provides practical and emotional details about the house for booking, retreat hosting, location, facilities, and philosophy."""
    content = get_doc_content("Website alt Texte.docx")
    return content[:8000]  if content else "Leider habe ich dazu keine Informationen."

# ---------- REGISTER TOOLS ----------
tools = [
    Tool(
        name="DatabaseSearch",
        func=search_database,
        description="Useful for greeting questions and behave naturly"
    ),
    Tool(
        name="UberMichInfo",
        func=uber_mich_info,
        description="Questions about Ester, her journey, and core inspiration. not for greeting"
    ),
    Tool(
        name="WebpagePhilosophy",
        func=webpage_philosophy,
        description="Details from the website about house philosophy and purpose. not for greeting"
    ),
    Tool(
        name="AngebotsDetails",
        func=angebotsdetails,
        description="Information on Leermondzyklus and Heart Circle (Inner Circle). not for greeting"
    ),
    Tool(
        name="HerzraumHintergrund",
        func=herzraum_hintergrund,
        description="Context, audience, and vision behind Ester’s work. not for greeting"
    ),
    Tool(
        name="MietinfoRetreathaus",
        func=mietinfo_retreathaus,
        description="Booking and retreat house information, structure, logistics. not for greeting"
    ),
]
