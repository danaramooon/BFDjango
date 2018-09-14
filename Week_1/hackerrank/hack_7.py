if __name__ == '__main__':
    n = int(raw_input())
    input_list = map(int, raw_input().split())
    for i in range(n):
        input_list[i] = int(input_list[i])
    t = tuple(input_list)
    print( hash(t))