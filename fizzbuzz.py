
for i in range(1 , 16):
    c=0
    if i % 3 == 0:
        c=1;
    if i % 5 == 0:
        c=c+2;
        
    if(c==1):
        print("Fizz")
    elif(c==2):
        print("Buzz")
    elif(c==3):
        print("FizzBuzz")
    else:
        print(i)
