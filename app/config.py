import os

from dotenv import load_dotenv

load_dotenv()

APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
APP_PORT = int(os.getenv("APP_PORT", "8005"))

DATABASE_URL = os.getenv("DATABASE_URL", "")
PAYMENT_SERVICE_URL = os.getenv("PAYMENT_SERVICE_URL", "")
INVENTORY_SERVICE_URL = os.getenv("INVENTORY_SERVICE_URL", "")
ORDER_SERVICE_URL = os.getenv("ORDER_SERVICE_URL", "")
