import smtplib

HOST = "sandbox.smtp.mailtrap.io"
PORT = 2525

USERNAME = "64642348d580a0"
PASSWORD = "958c36d650487c"

server = smtplib.SMTP(
    HOST,
    PORT
)

server.set_debuglevel(1)

server.ehlo()

server.starttls()

server.ehlo()

server.login(
    USERNAME,
    PASSWORD
)

print(
    "MAILTRAP SUCCESS"
)

server.quit()