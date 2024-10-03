def read_sales_data(file_path):
    file= open(file_path, encoding="utf-8")
    onstring = file.read().split("\n")[:-1]
    dict_f = {}
    list_f = list()
    # преобразование строк в списки
    for i in range(len(onstring)):
        list_f.append(onstring[i].split(','))
    # список ключей
    dict_keys = ['product_name', 'quantity', 'price', 'date']
    # преобразование списка ключей и данных в словарь
    for i in range(len(list_f)):
        dict_f[i] = dict(zip(dict_keys, list_f[i]))
    return dict_f
sales = read_sales_data('sales_data_202410022248.csv')
print (sales)
