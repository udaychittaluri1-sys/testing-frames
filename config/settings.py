import os

BASE_URL = os.getenv("BASE_URL", "https://react-frontend-api-testing.vercel.app")

BROWSER = os.getenv("BROWSER", "chrome")
GRID_URL = os.getenv("GRID_URL", "")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

IMPLICIT_WAIT = 5
EXPLICIT_WAIT = 20
PAGE_LOAD_TIMEOUT = 30