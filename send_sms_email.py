import os
from twilio.rest import Client
from smtplib import SMTP
from email.message import EmailMessage

# for sending SMS
TWILLIO_ACCOUNT_SID = os.environ["TWILLIO_SID"]
TWILLIO_AUTH_TOKEN = os.environ["TWILLIO_AUTH_TOKEN"]
TWILLIO_PHONE_NUMBER = os.environ["TWILLIO_PHONE_NUMBER"]
MY_PHONE_NUMBER = os.environ["MY_PHONE_NUMBER"]
# for sending mail
SENDER_MAIL = os.environ.get('SENDER_MAIL')
PASSWORD = os.environ.get('PASSWORD')
RECEIVER_MAIL = os.environ['RECEIVER_MAIL']


def send_message(message_to_send):
    client = Client(TWILLIO_ACCOUNT_SID, TWILLIO_AUTH_TOKEN)
    client.messages.create(body=message_to_send,
                           from_=TWILLIO_PHONE_NUMBER,
                           to=MY_PHONE_NUMBER
                           )
    print("message sent successfully")

def send_mail(STOCK_NAME, message_to_send):

    # for sending emails with emoji
    message = EmailMessage()
    message["Subject"] = f"{STOCK_NAME} {message_to_send[:1]}"
    message["From"] = SENDER_MAIL
    message["To"] = RECEIVER_MAIL
    message.set_content(message_to_send[2:])

    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_MAIL, password=PASSWORD)
        connection.send_message(message)
        print(f"{STOCK_NAME} mail sent successfully")
