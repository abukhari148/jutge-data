import os
import re
import requests
import bs4
import errno
import json
import io

JUTGED_DATA_DIR = os.path.expanduser(
    os.environ.get("JUTGED_DIR", os.path.join("~", ".config", "jutged"))
)
JUTGED_CONFIG_DIR = os.path.expanduser(
    os.environ.get("JUTGED_CONFIG_DIR", JUTGED_DATA_DIR)
)  # make changes here maybe?
URL = "https://jutge.org/problems/{id}/"

class Problem:
    def __init__(self, id: str) -> None:
        self.id = id
        self.public_tests_fname = f"{self.id}_public_tests.json"  # TODO: json or txt?

    # TODO: validate problem ID -> do something if it doesnt exist

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,value):
        if isinstance(self._id, str):
            self._id = value.upper()
        else:
            raise TypeError("Invalid Problem")

    @property
    def url(self):
        return URL.format(id=self.id)

    @property
    def _soup(self):
        response = requests.get(self.url)
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        return soup
