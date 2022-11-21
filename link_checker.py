from bs4 import BeautifulSoup

link = ["www.google.com", "www.yahoo.com", "www.youtube.com"]
email = "This is a test text string. In this string you will find the algorthm used by www.yahoo.com and www.youtube.co"
spam = False
for i in link:
    if i in email:
        spam = True
    else:
        pass

# if spam is False:
#     print("Safe Email")
# else:
#     print("Spam Email")


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
