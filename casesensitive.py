def isSubSequence(string1, string2, m, n): 
    if m == 0:    return True
    if n == 0:    return False
    if string1[m-1] == string2[n-1]: 
        return isSubSequence(string1, string2, m-1, n-1) 
    return isSubSequence(string1, string2, m, n-1) 
string1,string2 = input().split()
m = len(string1) 
n = len(string2) 
if isSubSequence(string1, string2, m, n): 
    print ("yes")
else: 
    print ("no")
