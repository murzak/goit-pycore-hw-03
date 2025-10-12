from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # Initiate an empty output array
    birthday_users = []

    # Loop through users
    for user in users:

        # Concatenate this or next year with string pattern MM.DD to get 2 possible birthdays
        mmdd = '.'.join(user['birthday'].split('.')[1:])
        this_year = datetime.today().year
        next_year = this_year + 1

        # For each year loop through and calculate difference in days 
        for year in [this_year, next_year]:
            birthday = f'{year}.{mmdd}'
            birthday_dt = datetime.strptime(birthday, '%Y.%m.%d').date()
            days_diff = (birthday_dt - datetime.today().date()).days

            # In case difference between 0 and 7, inclusively. 
            # Return congratulation date as birthday itself in case it happens Monday through Friday, otherwise, move to the next Monday
            if 0 <= days_diff <= 7:
                if 0 <= birthday_dt.weekday() <= 4:
                    birthday_users.append({'name': user['name'], 
                                           'congratulation_date': datetime.strftime(birthday_dt, '%Y.%m.%d')})
                else:
                    birthday_users.append({'name': user['name'], 
                                           'congratulation_date': datetime.strftime(birthday_dt + timedelta(days=7-birthday_dt.weekday()), '%Y.%m.%d')})
    return birthday_users

# users = [
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}
# ]
users = [
    {'name': f'{i}', 'birthday': f'1985.10.{11 + i}'} for i in range(1, 12)
]

print('Users :', users)
print(get_upcoming_birthdays(users))