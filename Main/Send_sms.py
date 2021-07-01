from twilio.rest import Client

account_sid = 'ACc8f48e89aceece4f61fdc203d3245c92'
auth_token = '149ce1d699069c8dc3de32b46a991eb2'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="",  # Body to be filled
    from_='+12729991628',
    to='+917981417200'
)
