"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os
import csv

PASSWORD = os.getenv('FOR_POSTGRES')

def write_data(table_name):
    filename = table_name + '_data.csv'
    #print(filename)
    #try:
    path = f'../homework-1/north_data/{filename}'
    with open(path) as f:
        data_file = csv.DictReader(f)
        for line in data_file:
            cur = conn.cursor()  #создаем курсор на каждую запись таблицы
            if table_name == 'employees':
                cur.execute('INSERT INTO employees(employee_id, first_name, last_name, title, birth_date, notes) '
                            'VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING',
                            (line['employee_id'], line['first_name'], line['last_name'], line['title'],
                             line['birth_date'], line['notes']))
            elif table_name == 'customers':
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s) ON CONFLICT DO NOTHING', (line['customer_id'],
                                                                              line['company_name'],
                                                                              line['contact_name']))
            elif table_name == 'orders':
                cur.execute('INSERT INTO orders(order_id, customer_id, employee_id, order_date, ship_city)'
                            ' VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING', (line['order_id'],
                                                                                   line['customer_id'],
                                                                                   line['employee_id'],
                                                                                   line['order_date'],
                                                                                   line['ship_city']))
    # except psycopg2.errors.UniqueViolation:
    #     print(f'запись с таким ключом уже есть в таблице {table_name}')
    # except psycopg2.errors.InFailedSqlTransaction:
    #     print('текущая транзакция прервана, команды до конца блока транзакции игнорируются')
    # else:
            cur.close()
            conn.commit()

#подключаемся к БД
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password=PASSWORD
)

# создаем курсор
# cur = conn.cursor()

# записываем данные в таблицы
table_name = 'employees'
write_data(table_name)
table_name = 'customers'
write_data(table_name)
table_name = 'orders'
write_data(table_name)

# создаем курсор
# cur = conn.cursor()

# # проверяем записи в таблице employees
# cur.execute("SELECT *FROM employees")
# rows = cur.fetchall()
# for row in rows:
#     print(row)
# # проверяем записи в таблице customers
# cur.execute("SELECT *FROM customers")
# rows = cur.fetchall()
# for row in rows:
#     print(row)
# # проверяем записи в таблице orders
# cur.execute("SELECT *FROM orders")
# rows = cur.fetchall()
# for row in rows:
#     print(row)


conn.close()
