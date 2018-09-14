def count_substring(str, sub_string):
    cnt = 0
    i = 0
    while i<len(str):
        if (str.find(sub_string,i)>=0):
            i=str.find(sub_string,i)+1
            cnt+=1
        else: 
            break
    return(cnt)