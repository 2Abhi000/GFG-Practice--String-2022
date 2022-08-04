#Check if string is rotated by two places
s=input("Enter first string: ")
s2=input("Enter another string: ")
def rotatech(s,s2,d):
    Lfirst = s[0 : d]
    Lsecond = s[d :]
    Rfirst = s[0 : len(s)-d]
    Rsecond = s[len(s)-d : ]
    f=Lsecond + Lfirst
    f1=Rsecond + Rfirst
    if(s2==f or s2==f1):
        return 1
    else:
        return 0

x=rotatech(s,s2,2)
if(x):
    print('1')
else:
    print('0')






