min = int(input('Enter the lower bound of range: '))
max = int(input('Enter the upper bound of range: '))

for i in range(min, max):
    
    isPrime = True
    if(i<2): continue
    for j in range (2, i):        
        if(i%j == 0):
            isPrime = False
            
        j+=1
    
    if(isPrime):
        print(i)