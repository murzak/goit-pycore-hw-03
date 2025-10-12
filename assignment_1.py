from datetime import datetime

def get_days_from_today(date):

    # Get date of string type to string of datetime with pattern of 'YYYY-MM-DD'
    date_dt = datetime.strptime(date, '%Y-%m-%d')

    # Get today's date in datetime format
    today_dt = datetime.today()

    # Calculate difference in between today's date and given date and get number of days in between
    return (today_dt - date_dt).days

print(get_days_from_today('2025-10-13'))
