import sqlite3

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect('Credentials.db')

# Create a cursor object to execute SQL statements
cur = conn.cursor()

# Execute an SQL statement
cur.execute('SELECT * FROM user_credentials')

# Fetch the results
results = cur.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and the connection
cur.close()
conn.close()
