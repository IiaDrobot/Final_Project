from db_connector import DBConnector
from config import search_history_db

def setup_database():
    db_connector = DBConnector(db_name=search_history_db)


    db_connector.execute_query('''
    CREATE TABLE IF NOT EXISTS search_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT NOT NULL,
        search_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

if __name__ == "__main__":
    setup_database()

