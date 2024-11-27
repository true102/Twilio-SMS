import key
from twilio.rest import Client

account_sid = key.account_sid
account_token = key.auth_token

client = Client(account_sid,account_token)

try: 
    message = client.messages.create(
        from_=key.twilio_number,
        body = "your message",  # Message content
        to=key.my_phone_number
    )

    print(f"Message sent successfully! SID: {message.sid}")
except Exception as e:
    print(f"Failed to send message: {e}")