import os
import imaplib
from imap_tools import
import email
from email.header import decode_header
import webbrowser
from app import db





def clean(text):
    return("".join(c if c.isalnum() else "_" for c in text))

# def check_message_number():
#     return(int(db.get("message_number")))
#
# def set_message_number(number):
#     return(db.set("message_number", number))
#
# def compare_messages():
#     messages = int(inbox[1].pop())
#     current_messages = check_message_number()
#     if messages > current_messages:
#         N = messages - current_messages
#         return (N)
#     else:
#         #do stuff if not
#         return(messages)
def setup_mailbox(username, password, server):
    mailbox = MailBox(server)
    #logs in
    mailbox.login(username, password, initial_folder='sms')
    return(mailbox)


def check_message_number():
    number = db.get("text_message_number")
    if number != None:
        return("text_message_number not set")
    else:
        return(int(number))

def set_message_number(n):
    if db.set("text_message_number", n) == True:
        return(True)
    else:
        return(False)

def set_hash(reply, number, timedate, message_number):
    if db.hset("text_message:".format(str(message_number)), {"number": number, "reply": reply, "timedate": timedate }) == True:
        return(True)
    else:
        return(False)

def check_for_messages(imap):
    inbox = imap.select("sms")
    message_number_current = int(db.get("text_message_number"))
    messages_in_inbox = int(inbox[1][0])
    if messages_in_inbox != message_number_current:
        update = get_messages(messages_in_inbox, message_number_current, imap)
    else:
        return(None)




def get_messages(messages, N, imap):
    flag = True
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
                    print(phone, datetime, reply)
                    if db.hset("text_message:".format(str(i)), {"phone": phone, "reply": reply, "datetime": datetime, "full": body }) != True:
                        return(False)
                    else:
                        pass







#imap = imaplib.IMAP4_SSL(server)
#logs in
#imap.login(username, password)
#selects inbox
#inbox = imap.select("INBOX")
# checks number messages
# popping result out of list and casting to int to get number
# imap = setup_login(username,password,server)

#N = compare_messages()
#inbox = imap.select("INBOX")

#messages = int(inbox[1].pop())

#if N is not int:
#    print("done")
#else:
#    get_messages(messages, N)
