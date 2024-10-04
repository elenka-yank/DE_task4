file= open('sales_data_202410022248.csv', encoding="utf-8")
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


products=[]
for i in range(len(sales_data)):
    products.append(sales_data[i]['product_name'])

total_sale = {}
for i in range(len(sales_data)):
    if sales_data[i]['product_name'] in total_sale:
        total_sale[sales_data[i]['product_name']] += int(sales_data[i]['quantity'])*int(sales_data[i]['price'])
    else:
        total_sale[sales_data[i]['product_name']] = int(sales_data[i]['quantity'])*int(sales_data[i]['price'])
       #total_sale.append(int(sales_data[i]['quantity'])*int(sales_data[i]['price']))


all_pr = {}
print(total_sale)
'''for i in range(0, len(products)):
    all_pr[products[i]] = total_sale[i]
'''
#print (list_f)
print(sales_data)
print(products)
print(total_sale)
print(all_pr)