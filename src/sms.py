# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def send(cliente):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'AC2081ebe3a4f7e41d7f20582aac8ab68b'
    auth_token = 'ef73316473b46af4782c69ec2ba4fc36'
    client = Client(account_sid, auth_token)
    mensaje='Es el  turno para almorzar de: '+cliente
    message = client.messages \
                    .create(
                        body=mensaje,
                        from_='+18304200477',
                        to='+56984876061'
                    )

    print(message.sid)