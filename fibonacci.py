# FIBONACCI
"""
0 1 1 2 3 5 8 13 21 ... n terms
"""
a=0
b=1
n = int(input("Enter number of terms : "))
print(a)
print(b)

for i in range (0,n-2):
    s=a+b
    print(s)
    a=b 
    b=s
