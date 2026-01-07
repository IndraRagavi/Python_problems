def isalnumm(s):
    return True if re.search('[a-zA-Z0-9]',s) else False

def isalphh(s):
    return True if re.search('[a-zA-Z]',s) else False

def isdigitt(s):
    return True if re.search('[0-9]',s) else False

def islowerr(s):
    return True if re.search('[a-z]',s) else False

def isupperr(s):
    return True if re.search('[A-Z]',s) else False


if __name__ == '__main__':
    import re
    s = input()
    alpnum = isalnumm(s)
    print(alpnum)
    alp = isalphh(s)
    print(alp)
    dig = isdigitt(s)
    print(dig)
    low = islowerr(s)
    print(low)
    upp = isupperr(s)
    print(upp)

eg: qA2 - this will result as True in all case since we have used search; output would be different if match is used
#search - finds the regex in the whole string
#match - find the regex from the starting of the string