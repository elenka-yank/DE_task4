# функция принимает путь к файлу и возвращает список продаж
def read_sales_data(file_path):
    # открытие и чтение файла
    file= open(file_path, encoding="utf-8")
    onstring = file.read().split("\n")[:-1]
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

# принимает список продаж и 
def total_sales_per_product(sales_data):
    #создание списка ключей с названиями продуктов
    products = []
    for i in range(len(sales_data)):
        products.append(sales_data[i]['product_name'])
    # создание списка общей суммы продаж
    total_sale = []
    for i in range(len(sales_data)):
        total_sale.append(int(sales_data[i]['quantity'])*int(sales_data[i]['price']))
    # возврат словаря с продуктами и общей суммой продаж
    pr_total_sale = {}
    pr_total_sale = dict(zip(products, total_sale))
    return pr_total_sale

sales_data = read_sales_data('sales_data_202410022248.csv')
total_sales = total_sales_per_product(sales_data)

print (sales_data)
print (total_sales)
