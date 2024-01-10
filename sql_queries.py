import sqlite3

conn = sqlite3.connect("Artistc.db")
cursor = conn.cursor() #створюєм курсор

cursor.execute("SELECT * FROM artists")


# Запитання 1. Інформація про скількох художників представлена у базі даних?
data = cursor.fetchall()
print(len(data))

# Запитання 2. Скільки жінок (Female) у базі?
cursor.execute('''SELECT * FROM artists WHERE "Gender"=="Female" ''')
data = cursor.fetchall()
print(len(data))

# Запитання 3. Скільки людей у базі даних народилися до 1900 року?
cursor.execute('''SELECT * FROM artists WHERE "Birth Year"<1900 ''')
data = cursor.fetchall()
print(len(data))


# Запитання 4*. Як звати найстаршого художника?
cursor.execute('''SELECT * FROM artists ORDER BY "Birth Year" ''')
data = cursor.fetchone()
print(data[1])

cursor.execute('''INSERT INTO artists("Artist ID", "Name", "Nationality", "Gender", "Birth Year")
               VALUES( (?), (?), (?), (?), (?) )''', [650, "Ван Гог", "голандець", "Male", "1853"])

cursor.execute('''INSERT INTO artists("Artist ID", "Name", "Nationality", "Gender", "Birth Year")
               VALUES( (?), (?), (?), (?), (?) )''', [652, "Леонардо Да Вінчі", "італієць", "Male", "1893"])

conn.commit()

cursor.close()
conn.close()