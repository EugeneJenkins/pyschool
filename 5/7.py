def primeNumbers(num):
    prime=[]
    
    if num==1:
        return prime
    j=2
    
    while j <=num:
        i=2
        if j==2:
            prime.append(2)
        while i<j:        
            if j%i==0:
                break
            else:
                i=i+1
                if i==j:
                    prime.append(j)
        j=j+1
           
    return prime
  
a=primeNumbers(60)
print (a)