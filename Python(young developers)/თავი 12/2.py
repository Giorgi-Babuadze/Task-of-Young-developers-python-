import sqlite3
from datetime import datetime

def create_table():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            created_at TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def add_user(name, email):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (name, email, created_at)
        VALUES (?, ?, ?)
    ''', (name, email, datetime.now()))
    conn.commit()
    conn.close()
    print("User added successfully!")

def view_all_users():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    
    if not users:
        print("database is empty")
    else:
        print("\nlist of all users:")
        for user in users:
            print(f"ID: {user[0]}, Имя: {user[1]}, Email: {user[2]}, Создан: {user[3]}")

def update_user(user_id, name, email):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users 
        SET name = ?, email = ?
        WHERE id = ?
    ''', (name, email, user_id))
    conn.commit()
    conn.close()
    print("Users data updated!")

def delete_user(user_id):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    print("User deleted!")

def main():
    create_table()
    
    while True:
        print("\nMenu:")
        print("1. Add new user")
        print("2. View all users")
        print("3. Update user data")
        print("4. Delete user")
        print("5. Exit")
        
        choice = input("\nChoose action (1-5): ")
        
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        
        elif choice == '2':
            view_all_users()
        
        elif choice == '3':
            user_id = input("Enter user ID: ")
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            update_user(user_id, name, email)
        
        elif choice == '4':
            user_id = input("Enter user ID for deletion: ")
            delete_user(user_id)
        
        elif choice == '5':
            print("Program ended!")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
