altitude_1=int(input("enter current altitude"))
if(altitude_1<=1000):
    print("pilot can land plain safely")
elif(altitude_1>1000 and altitude_1<5000):
    print("bring down the plain to 1000 ft for safe landing")
elif(altitude_1>=5000):
    print("turn around plain and attemt later")
