from src.firebase import Firebase
from src.send_email import Email
from config import EmailSender
import random


def user_credentials_input():
    user_email = input("Enter your email: ")
    while True:
        password = input("Enter your password with at least 8 characters: ")
        if len(password) >= 8:
            break
        print("Password must have at least 8 characters.")
    return user_email, password


def display_menu():
    print("\nWelcome our register! Please choose an option. \n")
    options = [
        "(1) Register email",
        "(2) Authenticate email"
    ]
    print("\n".join(options))
    user_choice = int(input(": "))
    return user_choice


def send_an_email_with_token(mail_to: str):
    token = ''.join([str(random.randint(0, 9)) for _ in range(6)])

    subject = "Verify your email!"
    body = f"""
    Hello,

    Insert this token where it is being requested to verify your email address:

    {token}

    If you didn't ask to verify this address, you can ignore this email.

    Thanks!
    """

    mail = Email(mail_from=EmailSender.EMAIL, 
                 app_password=EmailSender.PASSWORD,
                 mail_subject=subject,
                 body=body,
                 mail_to=mail_to)
    mail.send_email()

    return token


def execute_two_step_authentication():
    while True:
        firebase = Firebase()
        option = display_menu()

        if option == 1:
            user_email, password = user_credentials_input()
            firebase.create_user(user_email, password)
            print("Registration completed successfully!")

        elif option == 2:
            user_email, password = user_credentials_input()
            try:
                user_credentials_authenticated = firebase.authenticate_user(user_email, password)

                if user_credentials_authenticated:
                    token_sent = send_an_email_with_token(user_email)
                    user_input_token = input(f"Please enter the token sent to email {user_email} here: ")

                    if token_sent == user_input_token:
                        print("Authenticated user!")
                        break
                    else:
                        print("Invalid token, please try again.")
                else:
                    print("Unauthenticated user, please try again.")
            except Exception:
                print("\n ATTENTION! Check the sent credentials and try again.")

        display_menu()


if __name__ == '__main__':
    execute_two_step_authentication()