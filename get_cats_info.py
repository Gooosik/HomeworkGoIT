def get_cats_info(path):
    try:
         
        with open(path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file]
        print("Вміст файлу: ", lines)
    
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")
        return
    
    cat_info = []

    for line in lines:
            try:
                line = line.strip()
                if line:
                     cat_id, name, age = line.split(',')
                     cat_info.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                     })


            except ValueError:
                 print(f"Пропущено некоректний рядок: {line}")

    print(cat_info)
    return cat_info


get_cats_info("Two__work/path/to/salary_file.txt")