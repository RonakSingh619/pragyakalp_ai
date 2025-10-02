from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

# Your Twilio credentials (replace with your own)
ACCOUNT_SID = 'ACa1134aa0889e5634de0b76b60cc7b6ab'  # From Twilio dashboard
AUTH_TOKEN = 'd16963abdcfe4e6e9faa5579cfe8c9d3'    # From Twilio dashboard
TWILIO_PHONE_NUMBER = '+15626207278'  # Your Twilio number (e.g., +12025550123)

# Initialize the Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Phone number to call (replace with the recipient's number)
TO_PHONE_NUMBER = '+919696829722'  # E.164 format (e.g., +12025550123)

# Function to make a call
def make_phone_call(to_number, from_number, message=None, url=None):
    try:
        # Create a call
        call = client.calls.create(
            to=to_number,
            from_=from_number,
            # If using a TwiML URL (e.g., hosted voice instructions)
            url=url if url else 'http://demo.twilio.com/docs/voice.xml',  # Default Twilio demo
            # Alternatively, use TwiML directly for TTS (uncomment below if needed)
            # twiml=VoiceResponse().say(message) if message else None
        )
        print(f"Call initiated! Call SID: {call.sid}")
    except Exception as e:
        print(f"Error making call: {e}")

# Example usage
if __name__ == "__main__":
    # Simple call with default Twilio demo message
    make_phone_call(TO_PHONE_NUMBER, TWILIO_PHONE_NUMBER)

    # Uncomment to use custom text-to-speech message instead of a URL
    # message = "Hello! This is a test call from your Python script."
    # make_phone_call(TO_PHONE_NUMBER, TWILIO_PHONE_NUMBER, message=message)