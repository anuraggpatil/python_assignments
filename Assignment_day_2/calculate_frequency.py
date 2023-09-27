# Create a function to return a frequency distribution of a given sequence of values 

def calculate_frequency(input):
    dict = {}
    for i in input:
        if(i in dict):
            dict[i] += 1
        else: dict.update({i : 1})
    
    print(dict)

calculate_frequency((2,2,9,1,2,2,1,4,9,2,2,3,1))