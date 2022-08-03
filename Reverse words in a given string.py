#Reverse words in a given string
s=input("Enter string: ")
a=s.split('.')
k=[]
for i in a[::-1]:
    k.append(i)
    
x=".".join(k)
print(x)
