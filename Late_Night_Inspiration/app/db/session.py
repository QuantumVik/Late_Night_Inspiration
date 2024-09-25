from mysql.connector import pooling

pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    host="localhost",
    user="quantumvik",
    password="3d2y",
    database="ideas"
)

def get_db_connection():
    return pool.get_connection()