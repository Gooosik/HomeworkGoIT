import random

def get_numbers_ticket(min, max, quantity):

    try:

        lottery_nums_list = random.sample(range(min, max + 1), quantity)

        result = sorted(lottery_nums_list)

        return result
    
    except ValueError:
        return []

print("Ваші лотерейні числа:", get_numbers_ticket(112, 10, 5))
