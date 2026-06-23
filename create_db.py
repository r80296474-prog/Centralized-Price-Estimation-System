import sqlite3

conn = sqlite3.connect("price.db")

cursor = conn.cursor()

cursor.execute("""
ALTER TABLE estimate 
ADD COLUMN date_time TEXT
""")

conn.commit()

conn.close()

print("date_time column added")