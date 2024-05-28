import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")

    receiver = os.getenv("USER_NAME")
    # function to send emails securely
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

