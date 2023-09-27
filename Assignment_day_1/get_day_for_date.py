
def checkLeapYear(year):
    if(year%100 == 0):
        if(year%400 == 0):
            return True
    elif(year%4 == 0):
        return True
    
    return False

def week_day_name(index):
    week_name = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
    return week_name[index]

def date_value(day, month, year):
    value = 0
    y = year-1

    # total days elasped till a given date 
    value = y * 365 + y//4 - y//100 + y//400  #we use // to get integer result



def get_day_for_date():

    date = input('Enter a date in format dd/mm/yyyy: ')

    refDateDay = 1
    refDateMonth = 1
    refDateYear = 2006

    inputDateDay = int(date[:2])
    inputDateMonth = int(date[3:5])
    inputDateYear = int(date[-4:])

    # print(inputDateDay, inputDateMonth, inputDateYear)

    isLeapYear = checkLeapYear(inputDateYear)


    if(inputDateMonth%2 == 0):
        diffInDays = (int((inputDateMonth/2)-1)*30) + (int(inputDateMonth/2)*31)
    elif(inputDateMonth%2 !=0):
        diffInDays = (int(inputDateMonth/2)*30) + (int(inputDateMonth/2)*31)

    if(isLeapYear):
        diffInDays = diffInDays - 1
    else:
        diffInDays = diffInDays - 2

    if(inputDateMonth > 8):
        diffInDays = diffInDays + 1

    diffInDays = diffInDays + (inputDateDay - refDateDay) 

    print(diffInDays)

    

