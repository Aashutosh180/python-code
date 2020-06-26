def fibo(num):
    if(num<=1):
        return num
    else:
        return(fibo(num-1)+fibo(num-2))
numterms=int(input("enter number to get fibonacci sequence: "))
if (numterms<=0):
    print("please enter a positive number:")
else:
   print("Fibonacci sequence:")
   for i in range(numterms):
       print(fibo(i))
