import pandas as pd
import smtplib
from email.mime.text import MIMEText

HOST = "sandbox.smtp.mailtrap.io"
PORT = 2525

USERNAME = "64642348d580a0"

PASSWORD = "958c36d650487c"

df = pd.read_csv(
    "outputs/phase2_outreach.csv"
)

server = smtplib.SMTP(
    HOST,
    PORT
)

server.starttls()

server.login(
    USERNAME,
    PASSWORD
)

count = 0

for _, row in df.head(5).iterrows():

    body = f"""
Telecom Payment Alert

Customer ID: {row['customer_id']}

Predicted Bill: {row['predicted_bill']}

Bill Drop: {row['bill_drop']}

Recommended Offer: {row['offer']}
"""

    msg = MIMEText(body)

    msg["Subject"] = (
        "Telecom Customer Alert"
    )

    msg["From"] = (
        "telecom@project.com"
    )

    msg["To"] = (
        "customer@test.com"
    )

    server.send_message(
        msg
    )

    count += 1

server.quit()

print(
    f"{count} alerts sent successfully"
)