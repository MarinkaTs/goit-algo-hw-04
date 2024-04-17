def get_cats_info(path):
    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                if len(cat_data) == 3:
                    cat_info = {
                        "id": cat_data[0],
                        "name": cat_data[1],
                        "age": cat_data[2]
                    }
                    cats_list.append(cat_info)

        return cats_list

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []

#Приклад використання функції:
cats_info = get_cats_info("path/to/cats_file.txt")
for cat in cats_info:
   print(cat)