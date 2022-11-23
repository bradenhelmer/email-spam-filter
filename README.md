# Project Report
CSC 424 Class Project<br>
Group Members: Braden Helmer | Trent Salas | Matt Bryan

# Overview
This filter was built using various python libraries:
-  BeautifulSoup4: Used to parse html files and look for certain elements.
-  eml_parser: Used to parse .eml files to get hash information of an email.
-  aspose.email: Used to convert .eml files into .html files for BeautifulSoup to use.

The spam filter consists of 4 python files:
1. [hash_checker.py](https://github.com/bradenhelmer/email-spam-filter/blob/main/hash_checker.py)
2. [unsub_checker.py](https://github.com/bradenhelmer/email-spam-filter/blob/main/unsub_checker.py)
3. [link_checker.py](https://github.com/bradenhelmer/email-spam-filter/blob/main/link_checker.py)
4. [driver.py](https://github.com/bradenhelmer/email-spam-filter/blob/main/driver.py)

## hash_checker.py
This class is passed a hash value and checks against the file spam_hashes.txt to see if the hash has been blacklisted. If an email is determined spam and the hash is not in the list, HashCheck.add_hash() will be called to add it to the list.
```python
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
```
## unsub_checker.py
This class is passed a BeautifulSoup4 object and searches for all of the email's html `<a>` tags. All the words of all the tags are then parsed and compared to see if the word 'unsubscribe' is found.
```python
class UnsubChecker:
    def __init__(self, soup: BeautifulSoup) -> None:
        self.soup = soup
        self.link_tags = self.soup.find_all("a")

    def unsub_check(self) -> bool:
        words = []
        for tag in self.link_tags:
            words += tag.text.split(" ")
        for word in words:
            if word.lower().replace("-", "") == "unsubscribe":
                return False
        return True
```
## link_checker.py
This class is passed a BeautifulSoup4 object and uses this to find all the `href` attributes of the email's html `<a>` tags. These href addresses are then compared against the links in blacklisted_links.txt.
```python
class LinkChecker:
    def __init__(self, soup: BeautifulSoup) -> None:
        self.soup = soup
        self.link_tags = self.soup.find_all("a", href=True)

    def link_check(self) -> bool:
        with open("blacklisted_links.txt") as file:
            links = file.readlines()
            for tag in self.link_tags:
                if tag["href"] in links:
                    return True
        return False
```
## driver.py
This is the main execution of the program, bringing the above 3 classes together. This is the process:
1. The user is prompted for the name of an .eml file.
2. An EmlParser object is created and decodes the byte representation of the .eml file to find the URI hash.
3. A MailMessage object is used to convert the .eml file into a .html file.
4. BeautifulSoup object is instantiated with the newly created html file.
5. Above checker objects are instantiated and checks are completed.
6. If any checks are true: print "Email is Spam!" else "Email is not Spam!"

# Examples
### Blacklisted hash. 
### Blacklisted link.
### No unsubscribe link.
### Normal Email.



