from parse import parse


def get_public_tests(soup):
    parsed_cases = dict()
    if soup.find("horizontal-view"):
        cases = soup.find_all(class_="horizontal-view")
        for i, case in enumerate(cases):
            case = list(case.stripped_strings)
            parsed_cases[i] = {"input": case[1], "output": case[3]}
    else:
        # FIXME: adapt special cases such as P96275,P12509 -> solved but revise later
        cases = soup.find_all("li", class_="list-group-item")
        cases = [
            c
            for case in cases
            for c in list(case.stripped_strings)
            if c != "Input/Output"
        ]
        for i, case in enumerate(cases):
            r = parse("{:w}({input:g}) → {output:g}", case)
            parsed_cases[i] = {"input": r["input"], "output": r["output"]}
    return parsed_cases


def get_title(soup):
    title = soup.head.title.string.split(" - ")[2]
    return title
