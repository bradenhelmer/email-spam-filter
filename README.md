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
            links = [link.rstrip() for link in links]
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
![bad_hash](https://user-images.githubusercontent.com/77756408/203658946-85a64033-e383-4dd8-9205-ccc01892172b.jpeg)
The hash for this email is c5bb32205c7c618ae35c72c6711dcecb30a7ef88a3115c0d82663d9954f94404, which is in the spam_hashes.txt file
![Screenshot_2022-11-23_17-50-33](https://user-images.githubusercontent.com/77756408/203659180-fe39fbc9-3484-41f6-9ee8-b6836b896f09.png)
### Blacklisted link / No unsubscribe link
![BIDEN](https://user-images.githubusercontent.com/77756408/203661308-9a502f14-d3c0-421d-ba4a-10dc35c53e45.jpeg)
The href for this link is https://usa.gov which is in the blacklisted_links.txt file
![Screenshot_2022-11-23_18-12-05](https://user-images.githubusercontent.com/77756408/203661660-1ee5bec0-05bf-44b9-bcce-4efc336557b4.jpg)
