# функция принимает путь к файлу и возвращает список продаж
def read_sales_data(file_path):
    # открытие и чтение файла
    file= open(file_path, encoding="utf-8")
    onstring = file.read().split("\n")
    sales_data = {}
    list_f = list()
    # преобразование строк в списки
    for i in range(len(onstring)):
        list_f.append(onstring[i].split(','))
    # список ключей
    dict_keys = ['product_name', 'quantity', 'price', 'date']
    # преобразование списка ключей и данных в словарь
    for i in range(len(list_f)):
        sales_data[i] = dict(zip(dict_keys, list_f[i]))
    return sales_data

# принимает список продаж и возвращает словарь, где ключ - название продукта,
# а значение - общая сумма продаж этого продукта.
def total_sales_per_product(sales_data):
    total_sale = {}
    for i in range(len(sales_data)):
        if sales_data[i]['product_name'] in total_sale:
            total_sale[sales_data[i]['product_name']] += int(sales_data[i]['quantity']) * int(sales_data[i]['price'])
        else:
            total_sale[sales_data[i]['product_name']] = int(sales_data[i]['quantity']) * int(sales_data[i]['price'])
    return total_sale

def sales_over_time(sales_data):
    total_sale_date = {}
    for i in range(len(sales_data)):
        if sales_data[i]['date'] in total_sale_date:
            total_sale_date[sales_data[i]['date']] += int(sales_data[i]['quantity']) * int(sales_data[i]['price'])
        else:
            total_sale_date[sales_data[i]['date']] = int(sales_data[i]['quantity']) * int(sales_data[i]['price'])
    return total_sale_date

sales_data = read_sales_data('sales_data_202410022248.csv')
total_sales = total_sales_per_product(sales_data)
total_sale_date = sales_over_time(sales_data)


print (sales_data)
print (total_sales)
print(total_sale_date)


