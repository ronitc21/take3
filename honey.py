from twilio.rest import Client

account_sid = 'ACdbe0d1e668372d0ce7d4e84eeb90b2e0'
auth_token = 'b75dfa8b5a413e6b3ae5ef88e6ab7d56'
client = Client(account_sid, auth_token)

def send_message():
    message = client.messages.create(
                                    # Do not change from
                                        from_='whatsapp:+14155238886',
                                        body='I love you Dadu Dadi 💕😘💌😍 - From your Favorite Pota, Ronit',
                                        to='whatsapp:+919810132444'
                                    )

    print(message.sid)
