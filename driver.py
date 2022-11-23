# driver.py
# ~~~~~~~~~
# This puts all the components of the spam filter together
# import link_checker
from hash_checker import HashCheck
from link_checker import LinkChecker
from unsub_checker import UnsubChecker

from email import parser

from eml_parser import EmlParser
from os import remove
from os.path import exists
from bs4 import BeautifulSoup

from aspose.email import MailMessage, SaveOptions


def main():
    file_exists = False
    email_to_check = str()

    # Asking user which email to check
    while not file_exists:
        email_to_check = input("Enter eml file name for spam check: ")
        file_exists = exists(email_to_check)
        if file_exists:
            file_exists = True
            print("Checking email for spam...")
        else:
            print("Sorry! That file doesn't exist, try again.")

    # Using eml-parser to get hash
    p = EmlParser()
    email_hash = p.decode_email_bytes(open(email_to_check, "rb").read())["body"][0][
        "hash"
    ]

    # Using aspose.email to convert eml to html for parsing
    eml = MailMessage.load(email_to_check)
    options = SaveOptions.default_html
    eml.save("email_to_parse.html", options)

    # Parsing HTML with BeautifulSoup
    soup = BeautifulSoup(open("email_to_parse.html"), "html.parser")
    remove("email_to_parse.html")

    # Removving

    hc = HashCheck(email_hash)
    usc = UnsubChecker(soup)
    lc = LinkChecker(soup)
    spam_hash = hc.hash_check()
    spam_unsubscribe = usc.unsub_check()
    spam_blacklisted = lc.link_check()
    spam = spam_hash or spam_unsubscribe or spam_blacklisted

    print(f"Does the email carry a known spam hash: {spam_hash}")
    print(f"Does the email carry a known black-listed link: {spam_blacklisted}")
    print(f"Does the email not have an unsubscribe button: {spam_unsubscribe}")

    # Adding hash to spam_hashes.txt if not before
    if not spam_hash and (spam_blacklisted or spam_unsubscribe):
        hc.add_hash()

    print("Email is Spam!") if spam else print("Email is not Spam!")


if __name__ == "__main__":
    main()
