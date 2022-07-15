# 6. Напишите функцию to_weird_case,
# которая принимает строку и возвращает ту же строку,
# в которой все символы с четным индексом
# в каждом слове отображаются в верхнем регистре,
# а все символы с нечетным индексом в каждом слове — в нижнем регистре.
# Только что объясненная индексация основана на нуле,
# поэтому нулевой индекс четный,
# поэтому этот символ должен быть в верхнем регистре,
# и вам нужно начинать заново для каждого слова.
# Передаваемая строка будет состоять только из букв алфавита и пробелов (' ').
# Пробелы будут присутствовать только в том случае,
# если слов несколько.
# Слова будут разделены одним пробелом (' ').
#
# ПрИмЕрЫ:
# to_weird_case('String'); # => returns 'StRiNg'
# to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
# to_weird_case('This') # => returns 'ThIs'
# to_weird_case('is') # => returns 'Is'
# to_weird_case('This is a test') # => returns 'ThIs Is A TeSt'

def to_weird_case(word):
    word_list = [i for i in word.split(' ')]
    weird_list = []
    for i in range(len(word_list)):
        for j in range(len(word_list[i])):
            if j % 2 == 0:
                weird_list.append(word_list[i][j].upper())
            if j % 2 != 0:
                weird_list.append(word_list[i][j].lower())
        weird_list.append(' ')
    weird_str = ''.join(weird_list)
    return weird_str

print(to_weird_case('Smells like teen spirit'))