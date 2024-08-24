import sqlite3
import hashlib
import socket

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('account_database.db')
cursor = conn.cursor()

# Create users table if it doesn't exist (bisa tambah lagi data lain)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

# Connect to SQLite database (or create it if it doesn't exist)

# Create daily_data table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS daily_data (
        user_id INTEGER,
        date DATE,
        data_value REAL,
        PRIMARY KEY (user_id, date),
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )
''')

conn.commit()

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))  #can be set to local IP address if used in a network
server.listen()

def register(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        return True
    except sqlite3.IntegrityError:
        print('Username already exists')
        return False

def login(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    
    return cursor.fetchone() is not None

def update_daily_data(username, data_date, data_value):
    cursor.execute('SELECT user_id FROM users WHERE username = ?', (username,))
    user_id = cursor.fetchone()
    if user_id:
        cursor.execute('''
            SELECT data_value 
            FROM daily_data
            WHERE user_id = ? AND date = ?
        ''', (user_id[0], data_date))
        existing_value = cursor.fetchone()
        if existing_value:
            new_value = existing_value[0] + data_value
        else:
            new_value = data_value
        cursor.execute('''
            INSERT OR REPLACE INTO daily_data (user_id, date, data_value)
            VALUES (?, ?, ?)
        ''', (user_id[0], data_date, new_value))
        conn.commit()
    else:
        print(f"User {username} not found.")

def get_daily_data(username):
    cursor.execute('''
        SELECT u.username, d.date, d.data_value 
        FROM daily_data d
        JOIN users u ON d.user_id = u.user_id
        WHERE u.username = ?
        ORDER BY d.date
    ''', (username,))
    return cursor.fetchall()

conn.close()
