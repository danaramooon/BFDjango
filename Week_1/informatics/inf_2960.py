if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if(a == b):
    	print("YES")
    if(a != b):
    	if(a == 1 or b == 1):
	   		print("NO")
    	else:
    		print("YES")