import matplotlib.pyplot as plt

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


max_sales_pr = max(total_sales, key=total_sales.get)
max_sales_dt = max(total_sale_date, key=total_sale_date.get)

print (sales_data)
print (total_sales)
print(total_sale_date)

plt.figure(figsize=(12, 7))
plt.plot(total_sales.keys(), total_sales.values(), 'o-r', alpha=0.7, label="products", lw=5, mec='b', mew=2, ms=10)
plt.plot(total_sale_date.keys(), total_sale_date.values(), 'v-.g', label="dates", mec='r', lw=2, mew=2, ms=12)
plt.legend()
plt.grid(True)
plt.title(f"""Наибольшую выручку принес продукт:  {max_sales_pr} 
Наибольшая сумма продаж была  {max_sales_dt}""", loc="left", pad=10)
plt.show()

print (f"Наибольшую выручку принес продукт:  {max_sales_pr}")
print(f"Наибольшая сумма продаж была  {max_sales_dt}")
