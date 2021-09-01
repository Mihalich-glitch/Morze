def choice():
    type = int(input())
    if type > 2 or type < 1:
        print('Ошибка. Такого варианта нет')
    else:
        if type == 1:
            morze_to_rus()

        elif type == 2:
            rus_to_morze()

def rus_to_morze():
    word = input('Введите слово: ')
    word = word.lower()

    for letter in word:
        if letter in morze_dict.keys():
            print(morze_dict[letter])
        else:
            print('Ошибка. Вы ввели неверный символ')

def morze_to_rus():
    db = []
    letter = ''
    while letter != '1':
        letter = input('Вводите каждую новую букву с новой строки. После ввода нужных вам букв, напишите 1 на новой строке: ')

        if letter in morze_dict.values():
            inv_morze_dict = {value: key for key, value in morze_dict.items()}
            print(inv_morze_dict[letter])
            db.append(inv_morze_dict[letter])
        elif letter == '1':
            print('Отлично. Вот ваше сообщение')
        else:
            print('Ошибка. Вы ввели неверный символ')

    for element in db:
        print(element)

morze_dict = {
    'а': '.-',
    'б': '-...',
    'в': '.--',
    'г': '--.',
    'д': '-..',
    'е': '.',
    'ж': '...-',
    'з': '--..',
    'и': '..',
    'й': '.---',
    'к': '-.-',
    'л': '.-..',
    'м': '--',
    'н': '-.',
    'о': '---',
    'п': '.--.',
    'р': '.-.',
    'с': '...',
    'т': '-',
    'у': '..-',
    'ф': '..-.',
    'х': '....',
    'ц': '-.-.',
    'ч': '---.',
    'ш': '----',
    'щ': '--.-',
    'ъ': '.--.-.',
    'ы': '-.--',
    'ь': '-..-',
    'э': '..-..',
    'ю': '..--',
    'я': '.-.-'
}

print('Как вы будете вводить символы? С помощью азбуки морзе или на русском?')
print('азбука морзе - нажмите 1; русский - нажмите 2')
choice()
