import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')
n = 10
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON users (email)")
# for i in range(10):
#     n+=10
#     cursor.execute("INSERT INTO users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"user{i}", f"example{i}@gmail.com", f"{n}", "1000"))
# for i in range(0, 10, 2):
#     cursor.execute("UPDATE users SET balance = ? WHERE id = ?", ("500", f"{i+1}"))
# for i in range(0, 10, 3):
#     cursor.execute("DELETE FROM users WHERE id = ?", (f"{i+1}",))
# cursor.execute("SELECT * FROM users")
# cursor.execute("SELECT username, email, age, balance FROM users WHERE age != ?", (60,))
# users = cursor.fetchall()
# for user in users:
#     print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")
# cursor.execute("DELETE FROM users WHERE id = ?", ("6",))
cursor.execute("SELECT COUNT(*) FROM users")
total = cursor.fetchone()[0]
print(total)
cursor.execute("SELECT SUM(balance) FROM users")
all_balance = cursor.fetchone()[0]
print(all_balance)
cursor.execute("SELECT AVG(balance) FROM users")
average_balance = cursor.fetchone()[0]
print(all_balance / total)
print(average_balance)


connection.commit()
connection.close()