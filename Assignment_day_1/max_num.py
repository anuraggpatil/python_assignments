n = int(input('Enter a number: '))
x = 0
max = -100

while x<n:
    temp = int(input(f'Enter input {x+1}'))
    if(x==0):
        max = temp
    elif(temp>max):
        max = temp
    x+=1

print(max, 'is the maximum number')