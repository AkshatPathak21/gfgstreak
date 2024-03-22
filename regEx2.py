import re
def validate(str):
    pat= r'\w+\W+\d+'
    match = re.search(pat, str)
    if(match):
        return True
    else:
        return False
