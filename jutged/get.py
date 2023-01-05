from models import Problem

p = Problem("P57548")
soup = p._soup
print(soup.head.title.string.split(" - "))
ps = soup.find_all(class_="horizontal-view")
for p in ps:
    print(list(p.stripped_strings))
