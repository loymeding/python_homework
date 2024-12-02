import requests
from bs4 import BeautifulSoup


def main():
    # URL для получения данных
    url = 'https://github.com/'

    # Получение HTML-кода страницы
    response = requests.get(url)

    # Проверка успешности запроса
    if response.status_code == 200:
        print("Успешно получен HTML-код")

        # Парсинг HTML с помощью BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Пример: Извлечение заголовка страницы
        title = soup.title.string
        print("Заголовок страницы:", title)

        # Пример: Извлечение всех ссылок на странице
        links = soup.find_all('a')
        for link in links:
            print(link.get('href'))
    else:
        print("Ошибка при получении страницы:", response.status_code)


if __name__ == '__main__':
    main()
