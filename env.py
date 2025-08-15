import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "22657083")
API_HASH = os.getenv("API_HASH", "d6186691704bd901bdab275ceaab88f3")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8371449862:AAEpx9I6SkNb64sIYwl-8euG6rVnTeV2iF0")
SUDOERS = list(map(int, os.getenv("SUDOERS", "8195241636").split()))
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ahad0181888:ahad0181888@cluster0.f9casz0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP_ID = os.getenv("LOG_GROUP_ID", "-1002750713715")
MUST_JOIN = os.getenv("MUST_JOIN", "DEVELOPEDBYIVAN")
DISABLED = os.getenv("DISABLED", "").split()

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")

if not MONGO_URL:
    print("MONGO_URL environment variable Is Empty Bot")

# Convert the LOG_GROUP_ID variable to an integer if it is not None
if LOG_GROUP_ID:
    LOG_GROUP_ID = int(LOG_GROUP_ID)
