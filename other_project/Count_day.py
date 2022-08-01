'''
calculate number of days from date of birth to present
'''

import calendar, time

print('-'*20)
year = str(input('Input Year: '))
month = str(input('Input Month: '))
date = str(input('Input Date: '))
print('-'*20)

if int(month) > 12 or int(date) > 31:
    print('Invalid timestamp, please check again!')
    print('-'*20)
else:
    time_at_then = calendar.timegm(time.strptime(f'{year}-{month}-{date}', '%Y-%m-%d'))
    current_time = int(time.time())
    if time_at_then > current_time:
        print('Invalid timestamp, please check again!')
        print('-'*20)
    else:
        print(f'The person have lived: {int((current_time-time_at_then)/86400):,} days')  # /86400 chuyển từ s sang ngày
        print('-'*20)