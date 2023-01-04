import os
import re

JUTGED_DATA_DIR = os.path.expanduser(
    os.environ.get("JUTGED_DIR", os.path.join("~", ".config", "jutged"))
)
JUTGED_CONFIG_DIR = os.path.expanduser(
    os.environ.get("JUTGED_CONFIG_DIR", JUTGED_DATA_DIR)
)  # make changes here maybe?
URL = "https://jutge.org/problems/{id}/"


class User:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if not re.match(regex, value):
            raise ValueError("Invalid email address")
        self._email = value

    # TODO: find a way to cache and store user email and password

    # TODO: add a method to login

    # TODO: add a method to retrieve user stats


class Problem:
    def __init__(self, id) -> None:
        self.id = id
        self.public_tests_fname = f"{self.id}_public_tests.json" # TODO: json or txt?

    # TODO: validate problem ID -> do something if it doesnt exist

    @property
    def url(self):
        return URL.format(id=self.id)
