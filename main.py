from salary import hourly_salary

exit_ = 'q'
exit_msg = f'[{exit_}] to quit]'

while True:
    position = input('Type down position: ')
    if position == exit_:
        break

    hours = input(f'Actual hours{exit_msg}: ')
    if hours == exit_:
        break

    try:
        hours = float(hours)
    except ValueError:
        print('VAlue is not a number or decimal point is not a dot.')
        continue
    
    try:
        salary, tax = hourly_salary(position, hours)
    except Exception as error:
        print(error)
    else:
        print(f'After tax salary: {salary}')
        print(f'tax: {tax}')

