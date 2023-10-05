"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os
import csv

PASSWORD = os.getenv('FOR_POSTGRES')

#подключаемся к БД
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='180116_Psa'
)

# создаем курсор
cur = conn.cursor()

# записываем данные в таблицы

# filename = 'employees_data.csv'
# path = f'../homework-1/north_data/{filename}'
# with open(path) as f:
#     data_file = csv.DictReader(f)
#     for line in data_file:
#         cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', (line['employee_id'],
#                                                                               line['first_name'],
#                                                                               line['last_name'],
#                                                                               line['title'],
#                                                                               line['birth_date'],
#                                                                               line['notes']))
#cur.execute('SELECT * FROM employees')
# conn.commit()

# filename = 'customers_data.csv'
# path = f'../homework-1/north_data/{filename}'
# with open(path) as f:
#     data_file = csv.DictReader(f)
#     for line in data_file:
#         cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', (line['customer_id'],
#                                                                               line['company_name'],
#                                                                               line['contact_name']))
# conn.commit()

# filename = 'orders_data.csv'
# path = f'../homework-1/north_data/{filename}'
# with open(path) as f:
#     data_file = csv.DictReader(f)
#     for line in data_file:
#         cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', (line['order_id'],
#                                                                               line['customer_id'],
#                                                                               line['employee_id'],
#                                                                        line['order_date'],
#                                                                        line['ship_city']))
# conn.commit()

#проверяем записи в таблице
cur.execute("SELECT *FROM orders")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
