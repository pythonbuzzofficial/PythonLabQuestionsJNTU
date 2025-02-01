"""
Write a function called primes that is given a number n and returns a list of the first n
primes. Let the default value of n be 100.
"""

def primes(n = 100):
        
    prime_list = []

    start = 2

    while len(prime_list)<n:
        is_prime = True
        for i in range(2,int(start**0.5)+1):  
            if start%i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(start)
            
        start+=1
    return prime_list          
        
print(primes(100000))


# n = 10

# prime_list=[2,3,5,7,11,13,17,19,23,29]

# start= 2,3,4,5,6,7,8,9,10,11,12,1,3,14,15,16,17,18.........................29

# 30 = 5

# 2,15
# 3,10
# 5,6

# 541 = 23


    

        
        
        
        
        
        
       
        
        
        
    
    
   
