t="hello"
dict1={}
while t != '':
    t=input("Enter item name and price:")
    if(t!=""):
        a=t.split(" ")
        if a[0] not in dict1:
            dict1[a[0]]=int(a[1])
        else:
            dict1[a[0]]=dict1[a[0]]+int(a[1])
a1=dict1.keys()
for i in a1:
    msg=f'{i} {dict1[i]}'
    print(msg)