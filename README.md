# Firebase Two-Step Authentication via Email - Terminal Application

This project implements a two-step authentication system using Firebase and email verification. The application is entirely executed through the terminal.

## Features

- **Email Registration**:
  - Users can register by providing an email and a password with at least 8 characters.
  - The credentials are sent to Firebase for creating a new user account.

- **Email Authentication**:
  - Users can authenticate by providing their email and password created for Firebase.
  - After successful authentication, the user is asked to enter the 6-digit token generated and sent to the email provided.

## How to Run

1. **Firebase Configuration**:
   - Set up the Firebase and get your credentials here: https://firebase.google.com/docs/auth/web/start?hl=pt-br
   - Set up Firebase credentials in the `config.py` file.

2. **Email Configuration**:
   - Set up email sending credentials in the `config.py` file.

3. **Execution**:
   - Run the main script `main.py` through the terminal.

## Dependencies

- Python 3.x
- Python Libraries: pyrebase4 (for interacting with Firebase)

## Setting Up a Virtual Environment (Optional)

If desired, you can set up a virtual environment to install the dependencies:

```bash
# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate  # On Windows: env\Scripts\activate

# Install the dependencies
pip install -r requirements.txt

# Deactivate the virtual environment when no longer in use
deactivate
```