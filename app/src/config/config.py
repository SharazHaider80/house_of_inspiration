# Configuration settings
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Get the environment variable for the OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")