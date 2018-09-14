if __name__ == '__main__':
    year = int(input())
    leap = "NO"
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                  leap = "YES"
        else: leap = "YES"
    print(leap)
    
    
       
