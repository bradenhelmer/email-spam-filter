# hash_checker.py
# ~~~~~~~~~~~~~~~
# Function to check hashes against blacklisted emails

class hashCheck:
    def __init__(self, hash=""):
        self.hash = hash

    def hashCheck(self):
        file = open('spam_hashes.txt', 'r')
        Lines = file.readlines()
        if self.hash in Lines:
            return True
        return False
