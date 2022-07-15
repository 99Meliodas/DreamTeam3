# 5. Строка считается заглавной,
# если каждое слово в строке либо (а) пишется с заглавной буквы
# (то есть только первая буква слова в верхнем регистре),
# либо (б) считается исключением и полностью помещается в строчными буквами,
# если только это не первое слово, которое всегда пишется с большой буквы.

# Напишите функцию, которая преобразует строку в заглавный регистр,
# учитывая необязательный список исключений (второстепенные слова).
# Список второстепенных слов будет представлен в виде строки,
# где каждое слово отделено пробелом.
# Ваша функция должна игнорировать регистр строки второстепенных слов —
# она должна вести себя так же, даже если регистр строки второстепенных слов изменен.
# Первый аргумент (обязательный): исходная строка для преобразования.
# Второй аргумент (необязательный): список второстепенных слов, разделенных пробелами,
# которые всегда должны быть строчными, за исключением первого слова в строке
#
# примеры:
# title_case('a clash of KINGS', 'a an the of') #
# должен вернуть: 'A Clash of Kings'
#
# title_case('THE WIND IN THE WILLOWS', 'The In') #
# должен вернуть: 'The Wind in the Willows'
#
# title_case('the quick brown fox') #
# должен вернуть: 'The Quick Brown Fox'

def title_case(words, sort=''):
    sort_list = [i for i in sort.lower().split(' ')]
    words_list = [i for i in words.split(' ')]
    first = words_list[0].title()
    words_list.pop(0)
    for i in range(len(words_list)):
        words_list[i] = words_list[i].title()
        if words_list[i].lower() in sort_list:
            words_list[i] = words_list[i].lower()
    title_str = ' '.join(words_list)
    title_str = first + ' ' + title_str

    return title_str

print(title_case('Somebody once told me that the world is gonna rolle me', 'Somebody me is'))