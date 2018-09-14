if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range (n):
    	x = int(input())
    	a.append(x)
    for i in range (0,n):
    	if(a[i] % 2 == 0):
    		print(a[i])