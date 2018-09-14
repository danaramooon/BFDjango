if __name__ == '__main__':
    n = int(input())
    sum = 0
    a = []
    for i in range (n):
        x = int(input())
        a.append(x)
    for i in a:
        sum += i
    print(sum)
