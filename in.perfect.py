def perfect_number():
    i=1
    while i<=500:
        j=1
        sum=0
        while   j<i:
            if i%j==0:
                sum=sum+j
            j=j+1
        if sum==i:
            print( i,"perfect no")    
        else:
            print("not perfect")
        i=i+1  
perfect_number()  
      
