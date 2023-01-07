def get_public_tests(soup):
    parsed_cases = dict()
    cases = soup.find_all(class_="horizontal-view")
    for i, case in enumerate(cases):
        case = list(case.stripped_strings)
        parsed_cases[i] = {"input": case[1], "output": case[3]}
    return parsed_cases


def get_title(soup):
    title = soup.head.title.string.split(" - ")[2]
    return title
