from dotenv import load_dotenv
import os

def load_env(dotenv_path=None):
    """Loads environment variables from .env file."""
    load_dotenv(dotenv_path=dotenv_path)

def get_key(key, default=None):
    """Retrieves the value of a given environment variable key."""
    return os.getenv(key, default)