import sqlite3
def init_db():
    # Connect to SQLite (this will create data.db if it doesn't exist)
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
 
    # Create the responses table
    c.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            age INTEGER,
            gender TEXT,
            contact_number TEXT,
            email TEXT,
            address TEXT,
            education TEXT,
            occupation TEXT,
            income_range TEXT,
            device_availability TEXT,
            learning_language TEXT,
            learning_mode TEXT,
            time_slot TEXT,
            main_skill TEXT,
            sub_skill TEXT,
            experience_level TEXT,
            motivation TEXT,
            commitment TEXT,
            special_needs TEXT,
            referred_by TEXT
        )
    ''')
 
    # Commit changes and close connection
    conn.commit()
    conn.close()
 
    print("✅ Database initialized and table created (if not already).")
