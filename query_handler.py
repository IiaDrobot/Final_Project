
from db_connector import DBConnector
from config import sakila_dbconfig

class QueryHandler:
    def __init__(self):
        self.film_db_connector = DBConnector(db_config=sakila_dbconfig)

    def search_by_keyword(self, keyword):
        query = "SELECT title FROM film WHERE title LIKE %s OR description LIKE %s LIMIT 10"
        return self.film_db_connector.execute_query(query, ('%' + keyword + '%', '%' + keyword + '%'))

    def search_by_genre_and_year(self, genre, year):
        query = """
        SELECT f.title
        FROM film f
        JOIN film_category fc ON f.film_id = fc.film_id
        JOIN category c ON fc.category_id = c.category_id
        WHERE c.name = %s AND f.release_year = %s
        LIMIT 10
        """
        return self.film_db_connector.execute_query(query, (genre, year))

    def search_by_genre(self, genre):
        query = """
        SELECT f.title
        FROM film f
        JOIN film_category fc ON f.film_id = fc.film_id
        JOIN category c ON fc.category_id = c.category_id
        WHERE c.name = %s
        LIMIT 10
        """
        return self.film_db_connector.execute_query(query, (genre,))

    def search_by_year(self, year):
        query = """
        SELECT title
        FROM film
        WHERE release_year = %s
        LIMIT 10
        """
        return self.film_db_connector.execute_query(query, (year,))
