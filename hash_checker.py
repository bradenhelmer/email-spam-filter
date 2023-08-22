# hash_checker.py
# ~~~~~~~~~~~~~~~
# Handler to check hashes against blacklisted emails

# test comment 

class HashCheck:
    def __init__(self, hash=""):
        self.hash = hash

    def hash_check(self):
        file = open("spam_hashes.txt", "r")
        Lines = file.readlines()
        for line in Lines:
            if self.hash == line.rstrip():
                return True
        return False

    def add_hash(self) -> None:
        with open("spam_hashes.txt", "a") as spam_hashes:
            spam_hashes.write(self.hash)
