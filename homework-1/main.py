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
    password=PASSWORD
)

# создаем курсор
cur = conn.cursor()

# записываем данные в таблицы
try:
    filename = 'employees_data.csv'
    path = f'../homework-1/north_data/{filename}'
    with open(path) as f:
        data_file = csv.DictReader(f)
        for line in data_file:
            cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', (line['employee_id'],
                                                                                  line['first_name'],
                                                                               line['last_name'],
                                                                               line['title'],
                                                                               line['birth_date'],
                                                                               line['notes']))
except psycopg2.errors.UniqueViolation:
    print('запись с таким ключом уже есть в таблице employees')
else:
    conn.commit()

finally:
    try:
        filename = 'customers_data.csv'
        path = f'../homework-1/north_data/{filename}'
        with open(path) as f:
            data_file = csv.DictReader(f)
            for line in data_file:
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', (line['customer_id'],
                                                                                 line['company_name'],
                                                                                 line['contact_name']))
    except psycopg2.errors.InFailedSqlTransaction:
        print('запись с таким ключом уже есть в таблице customers')
    else:
        conn.commit()
    finally:
        try:
            filename = 'orders_data.csv'
            path = f'../homework-1/north_data/{filename}'
            with open(path) as f:
                data_file = csv.DictReader(f)
                for line in data_file:
                    cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', (line['order_id'],
                                                                              line['customer_id'],
                                                                              line['employee_id'],
                                                                       line['order_date'],
                                                                       line['ship_city']))
        except psycopg2.errors.InFailedSqlTransaction:
            print('запись с таким ключом уже есть в таблице orders')
        else:
            conn.commit()
        finally:
            cur.close()

# # создаем курсор
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


