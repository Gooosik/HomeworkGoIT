import re

def normalize_phone(phone_number):
    digits = re.findall(r'\d+', phone_number)
    
    normalized_number = ''.join(digits)
    
    if normalized_number.startswith("0"):
        normalized_number = "+38" + normalized_number
    elif normalized_number.startswith("380"):
        normalized_number = "+" + normalized_number
    elif not normalized_number.startswith("+380"):
        normalized_number = "+380" + normalized_number
    
    return normalized_number

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
