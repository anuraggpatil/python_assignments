# Create a Historgram for a given frequency table 

def plot_histogram(dict):
    for key in dict:
        print(f'{key} | ', end=' ')
        print('=='*dict[key], end='')
        print(f' {dict[key]}')

plot_histogram({2:6,1:3, 9:2,4:3,3:1}) 