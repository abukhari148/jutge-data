from exceptions import ProblemError
from pprint import pprint


def get_public_tests(soup):
    # save all title, and test cases here
    problem_info = dict()

    """
    Website always returns 200, even when problem ID is Invalid. 
    Workaround is parsing the title info.
    """
    title = soup.head.title.string.split(" - ")
    if len(title) == 3:
        problem_info["title"] = title[2]
    else:
        raise ProblemError("Invalid Problem ID.")

    # parse public test data
    parsed_cases = dict()
    cases = soup.find_all(class_="horizontal-view")
    for i, case in enumerate(cases):
        case = list(case.stripped_strings)
        parsed_cases[i] = {"input": case[1], "output": case[3]}

    problem_info["public_tests"] = parsed_cases
    return problem_info
