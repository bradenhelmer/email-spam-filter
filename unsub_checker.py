# unsub_cheker.py
# ~~~~~~~~~~~~~~~
# Handler for chceking unsubscrip links

from bs4 import BeautifulSoup


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
