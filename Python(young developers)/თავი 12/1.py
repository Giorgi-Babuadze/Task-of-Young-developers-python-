import sqlite3

conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        salary REAL NOT NULL
    )
''')

# Добавляем данные о сотрудниках
employees_data = [
    (1, 'Giorgi', 'Manager', 7500.00),
    (2, 'Nika', 'Developer', 8500.00),
    (3, 'Luka', 'Designer', 6500.00)
]

cursor.executemany('INSERT OR REPLACE INTO employees VALUES (?, ?, ?, ?)', employees_data)

conn.commit()

print("Информация о сотрудниках:")
cursor.execute('SELECT * FROM employees')
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Имя: {row[1]}, Должность: {row[2]}, Зарплата: {row[3]}")

conn.close()
