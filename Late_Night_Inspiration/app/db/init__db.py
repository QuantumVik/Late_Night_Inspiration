from Late_Night_Inspiration.app.db.session import get_db_connection



def init_db():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
            CREATE TABLE IF NOT EXISTS ideas(
                id INT AUTO_INCREMENT PRIMARY KEY,
                content TEXT NOT NULL,
                searched INTEGER DEFAULT 0,
                clarification TEXT)''')
    conn.commit()
    conn.close()
    c.close()