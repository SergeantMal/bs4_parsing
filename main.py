from bs4 import BeautifulSoup
import requests
from deep_translator import GoogleTranslator


# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")

def translate(word):
    translator = GoogleTranslator(source='auto', target='ru')
    translated = translator.translate(word)
    return translated


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру!")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word_eng = word_dict.get("english_words")
        word = translate(word_dict.get("english_words"))
        word_definition_eng = word_dict.get("word_definition")
        word_definition = translate(word_dict.get("word_definition"))

        # Начинаем игру
        print(f"Значение слова - {word_definition} / {word_definition_eng}")
        user = input("Что это за слово? ")
        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word} / {word_eng}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? (y/n) ")
        if play_again != "y":
            print("Спасибо за игру!")
            break


word_game()

