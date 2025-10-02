from twilio.rest import Client
from datetime import datetime, timedelta
import time

acc_sid = "ACa1134aa0889e5634de0b76b60cc7b6ab"
auth_token = "d16963abdcfe4e6e9faa5579cfe8c9d3"

client = Client(acc_sid, auth_token)

def sendMsg(recepient_No, msg_body):
    try:
        msg = client.messages.create(
            from_ = 'whatsapp:+14155238886',
            body = msg_body,
            to = f"whatsapp:{recepient_No}"
        )
        print(f"Message sent successfully, Msg SID: {msg.sid}")
    except Exception as e:
        print("Error occured: ",e)

# 919834001393
# 919403672573
sendMsg("+919834001393", "hello how are you")