from os import getenv

# API_URL = getenv("API_URL", "https://api.testbook.com/api/v2/tests/{test_id}")

API_ID = int(getenv("API_ID", "27775431"))
API_HASH = getenv("API_HASH", "b70bb1d45a1d05236671d4cc615e40f9")
BOT_TOKEN = getenv("BOT_TOKEN", "")
COOKIES = getenv("AUTH_CODE", "")
OWNER_ID = getenv("OWNER_ID", "6414266397") # if want to make accessible in channel put channel id in owner id field