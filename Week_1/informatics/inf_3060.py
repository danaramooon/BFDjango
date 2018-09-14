if __name__ == '__main__':
	n = int(input())
	i = 1
	t = 0
	while(i<=n):
		if(i==n):
			t = 0
			i *= 2
	if(t==0):
		print("NO")
	if(t == 1):
		print("YES")