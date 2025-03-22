import webbrowser

def search_rutube(query):
    # Формируем URL для поиска в рутуб
    url = f"https://rutube.ru/search/?query={query}"
    # Открываем URL в веб-браузере
    webbrowser.open(url)

def search_vkvideo(query):
    # Формируем URL для поиска в ВК Видео
    url = f"https://vkvideo.ru/?q={query}"
    # Открываем URL в веб-браузере
    webbrowser.open(url)

def search_dzen(query):
    # Формируем URL для поиска в Дзен
    url = f"https://dzen.ru/search?query={query}&type_filter=video%2Cshort"
    # Открываем URL в веб-браузере
    webbrowser.open(url)

print('RUVideoSearch v0.1.0')
query = input("Введите текст для поиска: ")
search_rutube(query)
search_vkvideo(query)
search_dzen(query)