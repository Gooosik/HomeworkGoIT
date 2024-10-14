import random

def get_numbers_ticket(min, max, quantity):

    lottery_nums_list = random.sample(range(min, max + 1), quantity)

    result = sorted(lottery_nums_list)

    return result

print("Ваші лотерейні числа:", get_numbers_ticket(1, 49, 6))