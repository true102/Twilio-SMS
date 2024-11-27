# Twilio-SMS
Twilio SMS Sender Script

**Overview**

This Python script leverages the Twilio API to send SMS messages to a designated recipient. It's a simple and efficient solution for automating text-based notifications, reminders, or alerts.

**Features**

- Secure Credential Management: The script reads sensitive data like account_sid, auth_token, and phone numbers from a separate key.py file, ensuring that sensitive information is not exposed directly in the script.
- Twilio Integration: It uses the Twilio SDK (twilio.rest.Client) to connect to Twilio's messaging service.
- Error Handling: Includes basic error handling to ensure smooth execution and provide meaningful feedback in case of issues.

**How It Works**

1- Import Twilio SDK and Credentials:
The script imports Twilio's Client class and credentials stored in a key.py file.
2- Initialize the Twilio Client:
The Client object is instantiated using the account_sid and auth_token.
3- Send SMS:
A message is created and sent using Twilio's messages.create() method, specifying the sender, recipient, and message body.
4- Output the Message SID:
On successful execution, the script prints the unique SID of the sent message for tracking purposes.
5- Error Handling:
If any issues occur (e.g., invalid credentials or network errors), they are caught and displayed in the console.

**Code Structure**

The script follows a modular structure:

key.py: Stores sensitive data like Twilio credentials and phone numbers.
sms_sender.py: Contains the main script to send SMS messages.

**Prerequisites**

pip install twilio
