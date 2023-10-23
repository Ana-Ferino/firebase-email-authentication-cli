import os
from dotenv import load_dotenv

load_dotenv()


class FirebaseConfig:

    API_KEY = os.getenv("api_key")
    AUTH_DOMAIN = os.getenv("auth_domain")
    PROJECT_ID = os.getenv("project_id")
    DATABASE_URL = os.getenv("database_url")
    STORAGE_BUCKET = os.getenv("storage_bucket")
    MESSAGING_SENDER_ID = os.getenv("messaging_sender_id")
    APP_ID = os.getenv("app_id")
    MEASUREMENT_ID = os.getenv("measurement_id")


class EmailSender:

    EMAIL = os.getenv("email")
    PASSWORD = os.getenv("password")