# Complete the solve function below.
def solve(s):
    s1 = s.split(" ")
    a = [i.capitalize() for i in s1]       
    return ' '.join(a)