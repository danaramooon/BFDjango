if __name__ == '__main__':
    n = int(input())
    sum = 0
    a = []
    for i in range (n):
        x = int(input())
        a.append(x)
    for i in a:
        if(i == 0):
            sum += 1
    print(sum)
