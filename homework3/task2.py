import string
from collections import Counter


def count_unique_words(text):
    # Приводим строку к нижнему регистру и удаляем знаки
    text = text.lower()
    translator = str.maketrans('', '', string.punctuation)
    cleaned_string = text.translate(translator)
    words = cleaned_string.split()
    # Подсчитываем количество уникальных слов
    unique_words = Counter(words)

    return len(unique_words)


# Пример использования функции
input_text = "Привет, мир! Привет мир, четыре слова?"
unique_word_count = count_unique_words(input_text)
print("Количество уникальных слов:", unique_word_count)
