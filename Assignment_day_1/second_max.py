n = int(input('Enter a number: '))
x = 0
max = -100
secondLargest = max

while x<n:
    temp = int(input('Enter input '))
    if(x==1):
        if(temp<=max):
            secondLargest = temp

    if(temp>max):
        secondLargest = max
        max = temp
    x+=1

print(max, 'is the largest number and', secondLargest, 'is the second largest')