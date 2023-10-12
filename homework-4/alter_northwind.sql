-- Подключиться к БД Northwind и сделать следующие изменения:
-- 1. Добавить ограничение на поле unit_price таблицы products (цена должна быть больше 0)

ALTER TABLE products ADD CONSTRAINT chk_products_unit_price CHECK (unit_price > 0)
--проверим
INSERT INTO products (product_id, product_name, supplier_id, category_id, quantity_per_unit, unit_price, discontinued)
VALUES (78, 'проверка', 8, 1, 'gdfgh', -1, 0)

-- 2. Добавить ограничение, что поле discontinued таблицы products может содержать только значения 0 или 1

ALTER TABLE products ADD CONSTRAINT chk_products_discontinued CHECK (discontinued IN (0, 1))

-- 3. Создать новую таблицу, содержащую все продукты, снятые с продажи (discontinued = 1)

SELECT * INTO old_products FROM products
WHERE discontinued = 1

-- 4. Удалить из products товары, снятые с продажи (discontinued = 1)
-- Для 4-го пункта может потребоваться удаление ограничения, связанного с foreign_key. Подумайте, как это можно решить, чтобы связь с таблицей order_details все же осталась.

--удаляю внешние ключи, по которым таблица products ссылается на другие таблицы
ALTER TABLE products DROP CONSTRAINT fk_products_suppliers;
ALTER TABLE products DROP CONSTRAINT fk_products_categories;

--удаляю внешние ключи, по которым ссылаются на таблицу products
ALTER TABLE order_details DROP CONSTRAINT fk_order_details_products

--удаляю товары, снятые с продажи
DELETE from products WHERE discontinued = 1

--сохраняю на всякий случай записи, которые ссылаются на товары снятые с продажи, из таблицы order_details в old_order_details
SELECT * INTO old_order_details FROM order_details
WHERE product_id IN (1, 2, 5, 9, 17, 24, 28, 29, 42, 53)

--удаляю устаревшие записи, которые ссылаются на товары снятые с продажи, из таблицы order_details
DELETE from order_details WHERE product_id IN (1, 2, 5, 9, 17, 24, 28, 29, 42, 53)

--Восстанавливаем связь FOREIGN KEY из таблицы order_details на products:
ALTER TABLE order_details ADD FOREIGN KEY (product_id) REFERENCES products(product_id)

--Восстанавливаем связь FOREIGN KEY из таблицы products на suppliers:
ALTER TABLE products ADD FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)

--Восстанавливаем связь FOREIGN KEY из таблицы products на categories:
ALTER TABLE products ADD CONSTRAINT fk_products_categories FOREIGN KEY (category_id) REFERENCES categories(category_id)