def total_salary(path):
    try:
         
        with open(path, 'r') as file:
            lines = [line.strip() for line in file]
        print("Вміст файлу: ", lines)
    
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")
        return

    salary_list = []
    
    for salary in lines:
            try:

                name, salary = salary.split(",")
                salary_list.append(float(salary))

            except ValueError:
                 print(f"Пропущено некоректний рядок: {salary}")

    total = sum(salary_list)
    salary_number = len(salary_list)
    average = total / salary_number

    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

total_salary("Two__work/path/to/salary_file.txt")