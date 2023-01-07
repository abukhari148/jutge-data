def get_public_tests(soup):
    parsed_cases = dict()
    if soup.find("horizontal-view"):
        cases = soup.find_all(class_="horizontal-view")
        for i, case in enumerate(cases):
            case = list(case.stripped_strings)
            parsed_cases[i] = {"input": case[1], "output": case[3]}
    else:
        #FIXME: adapt special cases such as P96275,P12509 
        cases = soup.find_all("li", class_="list-group-item")
        for i, case in enumerate(cases):
            case = list(case.stripped_strings)
            if not 'Input/Output':
                parsed_cases[i] = {"input": case[1], "output": case[3]}
    return parsed_cases


def get_title(soup):
    title = soup.head.title.string.split(" - ")[2]
    return title
