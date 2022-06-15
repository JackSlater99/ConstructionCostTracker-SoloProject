DROP TABLE transactions;
DROP TABLE products;
DROP TABLE suppliers;
DROP TABLE categories;


CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    main_cat VARCHAR(255),
    sub_cat VARCHAR(255)
);

CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(255),
    supplier_number VARCHAR(255),
    supplier_manager VARCHAR(255),
    supplier_address VARCHAR(255),
    supplier_phone VARCHAR(255)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    supplier_id INT REFERENCES suppliers(id) ON DELETE CASCADE,
    category_id INT REFERENCES categories(id) ON DELETE CASCADE,
    product VARCHAR(255),
    price INTEGER,
    po_number VARCHAR(255),
    order_date DATE,
    invoice_number INTEGER
)
