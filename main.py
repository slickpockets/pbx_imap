import os
import imaplib
import email
from email.header import decode_header
import webbrowser
import redis

####configs
for line in open('.env'):
    var = line.strip().split('=')
    if len(var) == 2:
        os.environ[var[0]] = var[1]

username = os.environ['USERNAME']
password = os.environ['PASSWORD']
server = os.environ['SERVER']
redis_pass= os.environ['REDISPASS']
redis_server = os.environ['REDISURL']
redis_port = os.environ['REDISPORT']
redis_db = os.environ['REDISDB']

db = redis.Redis(
    host=redis_server,
    port=redis_port,
    password=redis_pass
)


##main

def clean(text):
    return("".join(c if c.isalnum() else "_" for c in text))

def check_message_number():
    return(int(db.get("message_number")))

def set_message_number(number):
    return(db.set("message_number", number))

def compare_messages():
    messages = int(inbox[1].pop())
    current_messages = check_message_number()
    if messages > current_messages:
        N = messages - current_messages
        return (N)
    else:
        #do stuff if not
        return(messages)




def get_messages(messages, N):
    for i in range(messages, messages-N, -1):
    # fetch the email message by ID
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
             if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                content_type = msg.get_content_type()
                body = msg.get_payload(decode=True).decode()
                if content_type == "text/plain":
                    # print only text email parts
                    body = body.splitlines()
                    phone = body[0][-14:-2]
                    datetime = body[0][0:19]
                    reply = body[1]

imap = imaplib.IMAP4_SSL(server)
#logs in
imap.login(username, password)
#selects inbox
inbox = imap.select("INBOX")
# checks number messages
# popping result out of list and casting to int to get number
N = compare_messages()
inbox = imap.select("INBOX")

messages = int(inbox[1].pop())

if N is not int:
    print("done")
else:
    get_messages(messages, N)
