# hash_checker.py
# ~~~~~~~~~~~~~~~
# Function to check hashes against blacklisted emails


def hash_checker(hash_to_check: str) -> bool:
    with open("spam_hashes.txt") as hashes:
        stripped = [line.rstrip() for lines in hashes.readlines()]
        return hash_to_check in stripped
