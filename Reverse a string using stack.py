#Reverse a string using stack
s=input("Enter first string: ")

def revstack(s):
    a=[]
    for i in range(len(s)):
        a.append(s[i])
    return a[::-1]

ans=revstack(s)
for i in ans:
    print(i,end='')
