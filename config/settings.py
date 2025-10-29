# config loader file
import os
from dotenv import load_dotenv

BASE_DIR = os.getenv("PYTHONPATH", os.getcwd())
env_path = os.path.join(BASE_DIR, ".env")

load_dotenv(dotenv_path=env_path)

OPENWEATHER_KEY = os.getenv('OPENWEATHER_API_KEY')
GITHUB_KEY = os.getenv('GITHUB_TOKEN')