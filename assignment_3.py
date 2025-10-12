import re

def normalize_phone(num):
    # Substitute all non-numberic elements with empty string
    num = re.sub(r'\D', '', num)

    # Check if number starts with 0, then add +38, otherwise, add +
    if num.startswith('0'):
        return '+38' + num
    return '+' + num
    

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

correct_numbers = [
    '+380671234567', 
    '+380952345678', 
    '+380441234567', 
    '+380501234567', 
    '+380501233234', 
    '+380503451234', 
    '+380508889900', 
    '+380501112222', 
    '+380501112211']
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(sanitized_numbers)
print([sanitized_numbers[i] == correct_numbers[i] for i in range(len(raw_numbers))])