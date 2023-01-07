import os
import re
import requests
import bs4
from get import get_public_tests, get_title

JUTGED_DATA_DIR = os.path.expanduser(
    os.environ.get("JUTGED_DIR", os.path.join(os.getcwd(), ".config", "jutged"))
)

JUTGED_CONFIG_DIR = os.path.expanduser(
    os.environ.get("JUTGED_CONFIG_DIR", JUTGED_DATA_DIR)
)

URL = "https://jutge.org/problems/{id}/"


class Problem:
    def __init__(self, id: str) -> None:
        self._id = id

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id={self.id}, title="{self.title}")'

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str):
        regex = "^[pP]+\d{5}$"
        if (
            isinstance(value, str)  # maybe this is not needed
            and re.match(regex, value)
            and len(self._soup.head.title.string.split(" - ")) == 3
        ):
            self.id = value.upper()
        else:
            raise AttributeError("Problem ID is invalid!")

    @property
    def fname(self) -> str:
        return f"{self.id}.json"

    @property
    def url(self) -> str:
        return URL.format(id=self.id)

    @property
    def title(self) -> str:
        return get_title(self._soup)

    @property
    def _soup(self) -> str:
        response = requests.get(self.url)
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        return soup

    @property
    def public_tests(self) -> dict:
        return get_public_tests(self._soup)
