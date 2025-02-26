
from db_connector import DBConnector
from config import search_history_db

class SearchHistory:
    def __init__(self):
        self.search_history_db_connector = DBConnector(db_name=search_history_db)

    def save_search(self, query):

        query = query.strip().lower()
        insert_query = "INSERT INTO search_history (query) VALUES (?)"
        self.search_history_db_connector.execute_insert(insert_query, (query,))

    def get_popular_searches(self):
        query = "SELECT query, COUNT(*) as count FROM search_history GROUP BY query ORDER BY count DESC LIMIT 3"
        return self.search_history_db_connector.execute_query(query)
