if __name__ == '__main__':
    import math
    a = int(input())
    b = int(input())
    for i in range(a,b+1):
    	n = math.sqrt(i)
    	if(i//n == n):
    		print(i)