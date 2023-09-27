# create a sum function to sum a given set of variable values
# create an average functon to average a given set of variable values
# the average function should reuse the sum() function to sum all the items
    # average is sum()/total items

def sum(*values):
    result = 0
    for value in values:
        result += value
    return result

def average(*values):
    return sum(*values)/len(values)

print(average(1, 2, 3, 4))