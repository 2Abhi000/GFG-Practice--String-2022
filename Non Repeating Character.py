#Non Repeating Character
s=input("Enter first string: ")
def repe(S):
    a=[]
    d={}
    k=[]
    for i in range(len(S)):
        d[S[i]]=S.count(S[i])
    for i in d:
        if(d[i]==1):
            a.append(i)
    for i in a:
        ind=s.find(i)
        k.append(ind)
    if len(k)!=0:
        return s[k[0]]
    else:
        return '$'
ans=repe(s)
print(ans)








