# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1:])

# Вывести количество букв "а" в слове
word = 'Архангельск'
n = 0 
for later in word:
    if later.lower() == 'а':
        n += 1
print(f'Буква "а" в слове {word} встречается {n} раз(а).')

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'уеёэоаыяию'
n = 0
for later in word:
    if later.lower() in vowels:
        n += 1
print(f'В слове {word} {n} гласные буквы.')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
amount_words = len(sentence.split(' '))
print(f'В предложении {amount_words} слов(а).')

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence_list = sentence.split(' ')
for word in sentence_list:
    print(word[0:1])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sentence_list = sentence.split(' ')
lenght_words = 0
for word in sentence_list:
    lenght_words += len(word)
print(round(lenght_words / len(sentence_list), 2))
