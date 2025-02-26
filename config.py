import os
from dotenv import load_dotenv
from pymysql.cursors import DictCursor


load_dotenv()

sakila_dbconfig = {
    'host': os.getenv('HOST'),
    'user': os.getenv('USER'),
    'password': os.getenv('PASSWORD'),
    'database': os.getenv('DATABASE'),
    'cursorclass': DictCursor
}

search_history_db = 'movie_search.db'



