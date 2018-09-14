if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = (a*b) % 109
    if(c < 0):
        print(c + 109)
    else:
        print(c)