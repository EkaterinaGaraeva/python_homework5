# 4. Чисто для тренировки новый функций, ничего сложного. Создайте два списка — 
# один с названиями языков программирования, другой — с числами от 1 до длины первого плюс 1. 
# Вам нужно сделать две функции: первая из которых создаст список кортежей, 
# состоящих из номера и языка, написанного большими буквами. Вторая — которая отфильтрует 
# этот список следующим образом: если сумма очков слова имеет в делителях номер, 
# с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков. 
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы. 
# С помощью reduce сложите получившиеся числа и верните из функции в качестве ответа.

from functools import reduce

def create_list_of_tuples(list_of_numbers, list_of_languages):
    list_of_tuples = list(zip(list_of_numbers, list(map(lambda language: language.upper(), list_of_languages))))
    return list_of_tuples

def filter_list_of_tuples(list_of_tuples):
    list_of_filtered_tuples = []
    for i in range(len(list_of_tuples)):
        count = 0
        for j in list_of_tuples[i][1]:
            count += ord(j)
        if count % list_of_tuples[i][0] == 0:
            buf = list(list_of_tuples[i])
            buf[0] = count
            list_of_tuples[i] = tuple(buf)
            list_of_filtered_tuples.append(list_of_tuples[i])
    print(f'Отфильтрованный по условию список кортежей - {list_of_filtered_tuples}')
    sum = reduce(lambda s, y: s + y[0], list_of_filtered_tuples, 0)
    return sum
    

languages = ['Python', 'Java', 'Go', 'C']
numbers = list(range(1, len(languages) + 1))
tuples = create_list_of_tuples(numbers, languages)
print(f'Список кортежей - {tuples}')
print(f'Сумма чисел - {filter_list_of_tuples(tuples)}')

