 
# Print the calendar of a given month 

def is_leap_year(year):
    return (year%100!=0 and year%4==0) or year%400==0

def days_in_month(month , year):
    if month==2:
        return 28+int(is_leap_year(year))        
    elif (month<8 and month%2!=0) or (month>=8 and month%2==0):
        return 31
    else:
        return 30
    
def date_value(day ,month, year):
    value=0
    y=year-1
    # total days elapsed till the end of previous year
    value = y * 365 + y//4  - y//100 + y//400

    # add total days passed till previous month of this year
    m=1
    while m<month:
        #print(f'Adding {days_in_month(m,year)} for {m}/{year}')
        value+= days_in_month(m,year)
        m+=1

    #add days of this month
    value+=day
    return value

def date_to_week_day(date,month,year):
    ref_date = date_value(1,1,2006)
    input_date= date_value(date,month,year)
    diff= (input_date-ref_date) % 7
    return diff

def week_day_name(index):
    week_name = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
    return week_name[index]

def print_dates(start_date, month, year):
    while(start_date<=days_in_month(month, year)):
        print(start_date, end='\t')
        start_date+=7
    print('\n')
    
def calendar(month, year):
    day_for_first_date = date_to_week_day(1, month, year)
    for i in range(7):
        print(week_day_name(i), end='\t')
        if(i<day_for_first_date):
            print('', end='\t')
            x = 7-day_for_first_date + i + 1
            print_dates(x, month, year)
            
        else:
            x = i - day_for_first_date + 1
            print_dates(x, month, year)
            

calendar(9, 2023)



