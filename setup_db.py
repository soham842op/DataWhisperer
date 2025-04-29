import sqlite3

# Connect to (or create) a new SQLite database
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# Create a table for sales data
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL,
    date TEXT
)
''')

# Insert some sample rows
sample_rows = [
    ('Laptop', 5, 1200.00, '2024-03-01'),
    ('Phone', 10, 800.00, '2024-03-02'),
    ('Tablet', 3, 400.00, '2024-03-05'),
    ('Monitor', 7, 300.00, '2024-03-07'),
    ('Keyboard', 15, 50.00, '2024-03-08'),
]

cursor.executemany('''
INSERT INTO sales_data (product, quantity, price, date)
VALUES (?, ?, ?, ?)
''', sample_rows)

# Save (commit) and close
conn.commit()
conn.close()

print("✅ Database 'sales.db' created and populated successfully!")
