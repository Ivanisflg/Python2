#   Юзер вводит слово, нужно проверить, есть ли оно в списке.
#       ВАРИАНТ 1
# wordsList= []
# while True:
#     try:
#         inp = input('Введите массив слов, для окончания ввода, введите q:')
#         if inp == 'q':
#            break
#
#         wordsList.append(inp)
#     except ValueError:
#         print('Доступен ввод только целых чисел')
#
# inputWord = input('Введите слово поиска:')
#
# for word in wordsList:
#     if word==inputWord:
#         print(f"Слово {word} есть в списке " )

#       ВАРИАНТ 2
wordsList=set()
searchWordList=set()
while True:
    inp = input('Введите массив слов, для окончания ввода, введите q:')
    if inp == 'q':
        break

    wordsList.add(inp)

while True:
    inp = input('Введите массив слов для поиска, для окончания ввода, введите q:')
    if inp == 'q':
        break
    searchWordList.add(inp)
print(f'Ищем слова: {searchWordList} \nв списке слов: {wordsList}')

print(f'Найденные слова: {wordsList.intersection(searchWordList)}')
