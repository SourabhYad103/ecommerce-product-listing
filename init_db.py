import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    price REAL NOT NULL,
    image TEXT
)
""")

products = [
    ("Laptop", "A laptop for everyday use", 55000, "laptop.jpg"),
    ("Smartphone", "A smartphone with modern features", 25000, "phone.jpg"),
    ("Headphones", "Wireless headphones with clear sound", 2000, "headphones.jpg"),
    ("Keyboard", "A keyboard for computers", 1500, "keyboard.jpg"),
    ("Mouse", "A wireless computer mouse", 800, "mouse.jpg")
]

count = cursor.execute("SELECT COUNT(*) FROM products").fetchone()[0]

if count == 0:
    cursor.executemany("""
    INSERT INTO products (name, description, price, image)
    VALUES (?, ?, ?, ?)
    """, products)


conn.commit()
conn.close()

print("Database created and products inserted successfully!")
