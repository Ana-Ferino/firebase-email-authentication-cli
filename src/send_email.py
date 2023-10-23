import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email():

    def __init__(self, mail_from: str, app_password: str, mail_subject: str, body: str, mail_to: str):

        self.mail_from = mail_from
        self.app_password = app_password
        self.mail_subject = mail_subject
        self.body = body
        self.recipient = mail_to
        self.msg = MIMEMultipart()

    def structure_the_email(self):

        self.msg["From"] = self.mail_from
        self.msg["To"] = self.recipient
        self.msg["Subject"] = self.mail_subject
        self.msg.attach(MIMEText(self.body,"plain"))

    def send_email(self):

        self.structure_the_email()

        try:
            connection = smtplib.SMTP('smtp.gmail.com', 587)
            connection.starttls()
            connection.login(self.mail_from, self.app_password)
            message_type = self.msg.as_string()
            connection.sendmail(self.msg['From'], self.msg['To'], message_type)
            connection.quit()
            print("Email successfully sent!")
        except Exception as e:
            print(f"Something went wrong. Exception: {e}")