import sqlite3
import pandas as pd

# Connect to the existing database
conn = sqlite3.connect('sales.db')

# Run a query to select all data
df = pd.read_sql_query('SELECT * FROM sales_data', conn)

# Print the result
print(df)

# Close the connection
conn.close()
