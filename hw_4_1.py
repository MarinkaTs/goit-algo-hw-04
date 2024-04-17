def total_salary(path):
    total_salary = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділення рядка на ім'я та зарплату
                name, salary = line.strip().split(',')
                
                # Додавання зарплати до загальної суми та інкремент кількості розробників
                total_salary += int(salary)
                count += 1

        # Обрахунок середньої зарплати
        average_salary = total_salary / count if count > 0 else 0

        return total_salary, average_salary

    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Помилка: {e}")
        return 0, 0

# Приклад використання:
total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")