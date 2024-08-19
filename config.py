import os
from dotenv import load_dotenv

load_dotenv()

MAX_MESSAGES_BEFORE_DELETION = 5
UPSTAGE_API_KEY = os.getenv("UPSTAGE_API_KEY")
