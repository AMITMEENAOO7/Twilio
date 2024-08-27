from twilio.rest import Client
import config

# Your Twilio account credentials
account_sid = config.YourAccountSID
auth_token = config.YourAuthToken
client = Client(account_sid, auth_token)

# URL to handle call instructions
twiml_url = "http://demo.twilio.com/docs/voice.xml"  # Replace this with your TwiML URL

call = client.calls.create(
    url=twiml_url,  # The URL for Twilio to get call instructions
    to="+919166314168",  # The recipient's phone number
    from_="+12568278248",  # Your Twilio phone number
    record=True,  # Enable call recording
    recording_channels='dual',  # Record both sides of the conversation
    transcribe=True,  # Enable transcription
    transcribe_callback="https://your-callback-url.com/transcription"  # Your URL to receive transcriptions
)

print(call.sid)
