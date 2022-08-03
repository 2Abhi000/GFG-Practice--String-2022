#Validate an IP Address
ipv4=input("Enter the IP address: ")
k=ipv4.split('.')
p=0
for i in range(len(k)):
    if(len(k)==4 and (int(k[i])>=0) and (int(k[i])<=255)):
        p=1
    else:
        p=0
if(p):
    print(1)
else:
    print(0)

