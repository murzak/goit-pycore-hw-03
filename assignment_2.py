import random as rd

def get_numbers_ticket(min, max, quantity):

    # Check for faulty conditions and return []
    if  min < 1 or max > 1000 or min > max or quantity > (max - min + 1) or quantity < 1:
        return []
    
    # Otherwise, return the outcome
    lottery_numbers = rd.sample(range(min, max + 1), quantity)
    
    return sorted(lottery_numbers)

print(get_numbers_ticket(0, 49, 6))
print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(10, 5, 2))
print(get_numbers_ticket(10, 15, 10))
print(get_numbers_ticket(1, 1001, 5))
                