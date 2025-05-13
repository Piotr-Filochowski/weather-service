import twilio.rest
import os

from dotenv import load_dotenv

load_dotenv()
client = twilio.rest.Client(
    os.getenv('TWILIO_ACCOUNT_SID'),
    os.getenv('TWILIO_AUTH_TOKEN'),
    )

TWILIO_MESSAGING_SERVICE_ID = os.getenv('TWILIO_MESSAGING_SERVICE_ID')

def send_sms(text: str):
    message = client.messages.create(
        messaging_service_sid=TWILIO_MESSAGING_SERVICE_ID,
        body=text,
        to=os.getenv('RECIPIENT_PHONE_NUMBER')
    )
    print(f'Message sent. SID: {message.sid}')