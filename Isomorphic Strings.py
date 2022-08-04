#Isomorphic Strings
s=input("Enter first string: ")
s2=input("Enter another string: ")
def isom(s,s2):
    d={}
    d1={}
    a=[]
    b=[]
    for i in range(len(s)):
        d[s[i]]=s.count(s[i])
    for i in range(len(s2)):
        d1[s2[i]]=s2.count(s2[i])
    for i in d:
        a.append(d[i])
    for i in d1:
        b.append(d1[i])
    if(set(a)==set(b)):
        return 1
    else:
        return 0
    
ans=isom(s,s2)
print(ans)
