import re

filename = "README.md"
patt = '<a.*class="ranking".*></a>'

def write(rank):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    for c in content:
        if re.search(patt, c):
            modify = (c.split(re.split(patt, c)[0])[1]).replace("><",f">{str(rank)}<")
            print(modify)
            break
