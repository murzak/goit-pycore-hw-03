from datetime import datetime

def get_days_from_today(date_str):
    try:
        # Parse the date string with the expected format 'YYYY-MM-DD'
        date_dt = datetime.strptime(date_str, '%Y-%m-%d')

        # Get today's date (without time part)
        today_dt = datetime.today()

        # Return statement as difference between today and input date
        return (today_dt - date_dt).days

    except ValueError as e:
        print(f"Wrong input format for '{date_str}'. Please use 'YYYY-MM-DD'.")
        return None

print(get_days_from_today('2025-10-13'))
print(get_days_from_today('202510.13')) 
