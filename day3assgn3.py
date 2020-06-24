for num in range (100000,702648265):
    sum = 0  
    temp = num  
  
    while temp > 0:  
       digit = temp % 10  
       sum += digit ** 6 
       temp //= 10  
  
    if num == sum:  
       print(num,"is an Armstrong number")
       break
