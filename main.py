from query_handler import QueryHandler
from search_history import SearchHistory
from setup_database import setup_database

def main():
    query_handler = QueryHandler()
    search_history = SearchHistory()

    while True:
        print("\nВведите команду:")
        print("1. Поиск фильмов по ключевому слову (например, 'поиск stunning')")
        print("2. Поиск фильмов по жанру и году (например, 'жанр comedy 2006')")
        print("3. Поиск фильмов по жанру (например, 'жанр comedy')")
        print("4. Поиск фильмов по году (например, 'год 2006')")
        print("5. Показать популярные запросы (введите 'популярные')")
        print("6. Показать все фильмы (введите 'все фильмы')")
        print("7. Показать все жанры (введите 'все жанры')")
        print("8. Показать все запросы (введите 'все запросы')")
        print("9. Выход (введите 'exit')")

        command = input("Команда: ").strip().lower()

        if command == 'exit':
            break
        elif command.startswith('поиск '):
            keyword = command[6:].strip()
            print(f"Выполняется поиск по ключевому слову: '{keyword}'")
            results = query_handler.search_by_keyword(keyword)
            print(f"Результаты поиска по ключевому слову '{keyword}':")
            if results:
                for movie in results:
                    print(movie['title'])
            else:
                print("Ничего не найдено.")
            search_history.save_search(keyword)
        elif command.startswith('жанр '):
            parts = command.split()
            if len(parts) == 3:
                genre = parts[1]
                year = parts[2]
                results = query_handler.search_by_genre_and_year(genre, year)
                print(f"Результаты поиска по жанру '{genre}' и году '{year}':")
                for movie in results:
                    print(movie['title'])
                search_history.save_search(f"жанр {genre} {year}")
            elif len(parts) == 2:
                genre = parts[1]
                results = query_handler.search_by_genre(genre)
                print(f"Результаты поиска по жанру '{genre}':")
                for movie in results:
                    print(movie['title'])
                search_history.save_search(f"жанр {genre}")
            else:
                print("Неверный формат команды. Используйте: жанр <жанр> <год> или жанр <жанр>")
        elif command.startswith('год '):
            parts = command.split()
            if len(parts) == 2:
                year = parts[1]
                results = query_handler.search_by_year(year)
                print(f"Результаты поиска по году '{year}':")
                for movie in results:
                    print(movie['title'])
                search_history.save_search(f"год {year}")
            else:
                print("Неверный формат команды. Используйте: год <год>")
        elif command == 'популярные':
            results = search_history.get_popular_searches()
            print("Популярные запросы:")
            for query in results:
                print(f"{query['query']} - {query['count']} раз(а)")
        elif command == 'все фильмы':
            results = query_handler.search_by_keyword('')
            print("Все фильмы:")
            for movie in results:
                print(movie['title'])
        elif command == 'все жанры':
            query = "SELECT name FROM category"
            results = query_handler.film_db_connector.execute_query(query)
            print("Все жанры:")
            for category in results:
                print(category['name'])
        elif command == 'все запросы':
            results = search_history.search_history_db_connector.execute_query("SELECT * FROM search_history")
            print("Все запросы:")
            for search in results:
                print(search)
        else:
            print("Неизвестная команда. Попробуйте снова.")

if __name__ == "__main__":
    setup_database()
    main()
