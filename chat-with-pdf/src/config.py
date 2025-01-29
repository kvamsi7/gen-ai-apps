import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
HF_TOKEN = os.getenv('HF_TOKEN')
