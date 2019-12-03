def LCM(nums): 
   Maxnums=max(nums)
   i=0
   length=len(nums)
   while i<=length:
       if Maxnums%nums[i]==0:
           i=i+1
           if i==length:
               return Maxnums
               break
       if Maxnums%nums[i]!=0:
           Maxnums=Maxnums+1
           i=0

a=LCM([2, 3, 4,5,7])   
print (a)
