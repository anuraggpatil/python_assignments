# rewrite histogram function to add following customizatoins
    # cuztomizatoin should be passed as parameters
    # we can change the design of the bar which defaults to '==='
    # we may want to hide the exact frequency value (default show)
    # we may want to align the frequency values (default false)


def plot_histogram(dict, design = '===', hide_freq = False, align_freq = False):
    largest = 0 
    for freq in dict.values():
        if freq> largest: largest = freq
    
    design = design + ' '
    for key,freqeuncy in dict.items():
        print(f'{key} | ', end=' ')

        align_val = ' '
        if align_freq == True: 
            align_val = ' '*(largest - freqeuncy)*len(design)
        print(design*freqeuncy, end=align_val)

        if hide_freq == False:
            print(f'{freqeuncy}')
        else:
            print()

plot_histogram({2:3,1:6, 9:2,4:3,3:1}, '+++++', hide_freq=False, align_freq= True) 
