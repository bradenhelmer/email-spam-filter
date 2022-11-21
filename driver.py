# driver.py
# ~~~~~~~~~
# This puts all the components of the spam filter together
import link_checker
import unsub_checker
import hash_checker

from os.path import exists
import eml_parser
import json
import datetime

def json_serial(obj):
  if isinstance(obj, datetime.datetime):
      serial = obj.isoformat()
      return serial


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

    # Getting raw email bytes
    raw_email = bytes()
    with open(email_to_check, "rb") as email:
        raw_email = email.read()
    
    # eml parsing
    parser = eml_parser.EmlParser()
    parsed_email = parser.decode_email_bytes(raw_email)

    json_representation = json.dumps(parsed_email, default=json_serial)
    
    #TODO run spam checks through the JSON representation of the email

if __name__ == "__main__":
    main()
