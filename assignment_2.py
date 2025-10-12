import random as rd

def get_numbers_ticket(min, max, quantity):

    # Generate an empty placeholder for unique lottery numbers
    lottery_numbers = []

    # Check for faulty conditions and return []
    if min < 1 or max > 1000 or not (quantity >= min and quantity <= max):
        return []
    
    # In case of type of any parameter being different from INT it should return a message
    elif type(min) != int or type(max) != int or type(quantity) != int:
        return "One of input parameters should've been of INT type. Please check again"
    
    # Enter an infinite loop 
    while True:

        # Generate a random value in between min and max values, inclusively
        val = rd.randint(min, max+1)

        # If val value is not in placeholder lottery_number, we append this element to lottery_numbers
        if val not in lottery_numbers:  
            lottery_numbers.append(val)

            # Once reached allowed quantity limit, return sorted lottery_numbers array 
            if len(lottery_numbers) == quantity:
                return sorted(lottery_numbers)
            
print(get_numbers_ticket(1.1, 49, 6))
print(get_numbers_ticket(0, 49, 6))
print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 500, 10))
                