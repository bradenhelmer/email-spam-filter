# email_fetcher.py
# ~~~~~~~~~~~~~~~~
# This file fetches all the emails from the user for checking
import email
from imaplib import IMAP4_SSL

DUMMY_EMAIL_ADDRESS = "csc424projectdummy@gmail.com"
# This is an app specific password for IMAP access, it differs from the actual Google account password.
PASSWORD = "mpuietxubasitdja"
IMAP_ADDRESS = "imap.gmail.com"

def get_body(message):
    if message.is_multipart():
        return (
            get_body(message.get_payload(0))
            if message.is_multipart()
            else message.get_payload(None, True)
        )


def search(key, value, con):
    # value is the email address we are searching emails from
    data = con.search(None, key, '"{}"'.format(value))
    return data


def get_emails(result_bytes, con):
    print(result_bytes)
    messages = []
    for num in result_bytes[1][0].split():
        data = con.fetch(num, "(INSERT PARSE OPTION HERE)")
        messages.append(data)
    return messages


def login_and_retrieve():
    con = IMAP4_SSL(IMAP_ADDRESS)
    con.login(DUMMY_EMAIL_ADDRESS, PASSWORD)
    con.select("Inbox")
    return get_emails(search("FROM", "INSERT_EMAIL_ADDRESS_HERE", con), con)


def main():
    emails = login_and_retrieve()
    for email in emails:
        print(email)


if __name__ == "__main__":
    main()
