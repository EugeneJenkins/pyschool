def sqApprox(num):
    i = 0
    minsq = int(pow(num,0.5))      
    maxsq = int(pow(num,0.5))+1        

    while i<=maxsq :      
          if i*i==num:
             minsq=i
             return(minsq,minsq)
#             break

          if i*i<=num and i >=minsq: 
             minsq = i
          if i*i>=num and i <=maxsq: 
             maxsq = i

          i+=1                   
    return (minsq, maxsq) 

a=sqApprox(4)
print (a)
