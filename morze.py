"""
    TODO:
    import winsound
    Озвучить полученный код
    Закодировать пробелы
"""

import time

codes = {}

# буквы
codes["а"] = ".-"
codes["б"] = "-..."
codes["в"] = ".--"
codes["г"] = "--."
codes["д"] = "-.."
codes["е"] = "."
codes["ж"] = "...-"
codes["з"] = "--.."
codes["и"] = ".."
codes["й"] = ".---"
codes["к"] = "-.-"
codes["л"] = ".-.."
codes["м"] = "--"
codes["н"] = "-."
codes["о"] = "---"
codes["п"] = ".--."
codes["р"] = ".-."
codes["с"] = "..."
codes["т"] = "-"
codes["у"] = "..-"
codes["ф"] = "..-."
codes["х"] = "...."
codes["ц"] = "-.-."
codes["ч"] = "---."
codes["ш"] = "----"
codes["щ"] = "--.-"
codes["ъ"] = ".--.-."
codes["ы"] = "-.--"
codes["ь"] = "-..-"
codes["э"] = "...-..."
codes["ю"] = "..--"
codes["я"] = ".-.-"
codes["0"] = "-----"
codes["1"] = ".----"
codes["2"] = "..---"
codes["3"] = "...--"
codes["4"] = "....-"
codes["5"] = "....."
codes["6"] = "-...."
codes["7"] = "--..."
codes["8"] = "---.."
codes["9"] = "----."
codes[" "] = " "

phrase = input("Введите фразу из кириллических букв, цифр и пробелов. ").lower()


def encode_phrase(phrase: str) -> list:
    """
        Паузы пробелами:
            между частями симовла - 1  пробел
            между символами - 3 пробела
            между словами - 7 пробелов
    """
    encoded_list = []
    for symbol in phrase:
        encoded_list.append(codes[symbol])
    return encoded_list


print(encode_phrase(phrase))
