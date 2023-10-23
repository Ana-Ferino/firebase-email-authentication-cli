import pyrebase
from config import FirebaseConfig


class Firebase:

    firebase_config = {
        "apiKey": FirebaseConfig.API_KEY,
        "authDomain": FirebaseConfig.AUTH_DOMAIN,
        "projectId": FirebaseConfig.PROJECT_ID,
        "databaseURL": FirebaseConfig.DATABASE_URL,
        "storageBucket": FirebaseConfig.STORAGE_BUCKET,
        "messagingSenderId": FirebaseConfig.MESSAGING_SENDER_ID,
        "appId": FirebaseConfig.APP_ID,
        "measurementId": FirebaseConfig.MEASUREMENT_ID
    }

    def __init__(self) -> None:
        self.firebase = pyrebase.initialize_app(self.firebase_config)
        self.auth = self.firebase.auth()

    def create_user(self, user_mail, password) -> None:
        self.auth.create_user_with_email_and_password(user_mail, password)

    def authenticate_user(self, user_mail: str, password: str) -> bool:
        response = self.auth.sign_in_with_email_and_password(user_mail, password)
        return response.get("idToken") is not None
