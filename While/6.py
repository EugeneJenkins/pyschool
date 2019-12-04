def factorial(num):
    product = 1
    i = num
    
    while i > 0: 
       product = product*i
       i-=1
       if i<=0:
           break

    return product 

a=factorial(10)
print (a)