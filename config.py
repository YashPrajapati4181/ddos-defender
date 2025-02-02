import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

class Config:
    IPINFO_API_KEY = os.getenv("IPINFO_API_KEY", "")
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REQUEST_LIMIT = 100  # Max requests per minute
    BLOCK_DURATION = 3600  # Block IP for 1 hour (in seconds)
