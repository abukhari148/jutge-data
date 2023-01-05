import os
import re
import requests
import bs4


JUTGED_DATA_DIR = os.path.expanduser(
    os.environ.get("JUTGED_DIR", os.path.join(os.getcwd(), ".config", "jutged"))
)

JUTGED_CONFIG_DIR = os.path.expanduser(
    os.environ.get("JUTGED_CONFIG_DIR", JUTGED_DATA_DIR)
)

URL = "https://jutge.org/problems/{id}/"


class Problem:
    def __init__(self, id: str) -> None:
        self.id = id
        self.public_tests_fname = f"{self.id}_public_tests.json"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        regex = "^P+\d{5}$"
        if isinstance(value, str) and re.match(regex, value):
            self._id = value.upper()
        else:
            raise TypeError("Invalid Problem ID.")

    @property
    def url(self):
        return URL.format(id=self.id)

    @property
    def _soup(self):
        response = requests.get(self.url)
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        return soup

    @property
    def public_tests(self):
        pass # maybe return a dict using function in get or maybe read data from file 