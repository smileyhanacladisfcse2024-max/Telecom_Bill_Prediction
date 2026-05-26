import smtplib

email = "YOUR_OUTLOOK_EMAIL"
pwd = "YOUR_OUTLOOK_PASSWORD"

server = smtplib.SMTP(
    "smtp.office365.com",
    587
)

server.starttls()

server.login(
    email,
    pwd
)

print(
    "LOGIN SUCCESS"
)

server.quit()