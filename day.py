days = { 
        0:'Sunday',
        1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday',
        7:'Sunday'
        }

#print(days[13])
day = int(input("Enter day number : "))
print(days.get(day,f'Invalid Input, Input Range(1,7), your input was {day}'))
