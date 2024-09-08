import sqlite3


conn = sqlite3.connect('sales.db')
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    total_price REAL NOT NULL,
    date DATE NOT NULL,
    FOREIGN KEY(product_id) REFERENCES products(id)
)
""")


conn.commit()
conn.close()


conn = sqlite3.connect('sales.db')
cursor = conn.cursor()


cursor.execute("INSERT INTO products (name) VALUES ('Product A')")
cursor.execute("INSERT INTO products (name) VALUES ('Product B')")


cursor.execute("INSERT INTO sales (product_id, quantity, total_price, date) VALUES (1, 10, 100.0, '2023-02-15')")
cursor.execute("INSERT INTO sales (product_id, quantity, total_price, date) VALUES (2, 5, 50.0, '2023-03-10')")


conn.commit()
conn.close()