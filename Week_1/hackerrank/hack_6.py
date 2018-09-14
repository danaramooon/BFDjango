if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
def swap_case(s):
    str = ""
    for i in s:
        if(i.isupper()):
            str += i.lower()
        else:
            str += i.upper()
    return str
