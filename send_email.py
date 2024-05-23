import smtplib
import ssl


def send_email():
    host = "smtp.gmail.com"
    port = 465

    username = "email@example.com"
    password =

    receiver = "email@example.com"

    # function to send emails securely
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


send_email()
