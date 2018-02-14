#load the module twilio.rest, but only fetch client class into the current namespace
from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "AC53ce1286f11e0c2ddc4833db0efc43ad"
# Your Auth Token from twilio.com/console
auth_token  = "ce2797abbeed3c1817c619ce53540a9e"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+16136175373", #my number 
    from_="+18738002697", #twilio number 
    body="Hello my name is Nouran Nouh!")

print(message.sid)