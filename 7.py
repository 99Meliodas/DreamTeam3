# 7. ваша задача — создать функцию, которая превращает строку в мексиканскую волну.
# Вам будет передана строка, и вы должны вернуть эту строку в виде массива,
# где заглавная буква означает стоящего человека (https://ru.wikipedia.org/wiki/Волна_(стадион).
# Правила:
# 1. Строка ввода всегда будет строчной, но может быть и пустой.
# 2. Если символ в строке является пробелом, пропустите его, как если бы это было пустое место.
#
# Пример:
# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
#
# https://ru.wikipedia.org/wiki/Волна_(стадион)

def mexican_wave(word):
    word = word.replace(' ', '')
    words = (word + ' ') * len(word)
    word_list = words.split(' ')
    word_list.pop()
    char_list = [[j for j in i] for i in word_list]
    mexican_list = []
    for i in range(len(char_list)):
        for j in range(len(char_list[i])):
            if i == j:
                char_list[i][j] = char_list[i][j].upper()

        mexican_list.append(''.join(char_list[i]))
    return mexican_list
print(mexican_wave('good game'))


