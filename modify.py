import re

filename = "README.md"
patt = '<a.*class="ranking".*></a>'

def write(rank):
    with open(filename) as f:
        content = f.readlines()
    content = [x for x in content] 
    replaced = ""
    for c in content:
        if re.search(patt, c):
            splitToModify = (c.split(re.split(patt, c)[0])[1])
            modify = splitToModify.replace("><",f">{str(rank)}<")
            replaced += c.split(splitToModify)[0] + modify + c.split(splitToModify)[1]
        else:
            replaced += c
    with open(filename, "w") as f:
        f.write(replaced)
