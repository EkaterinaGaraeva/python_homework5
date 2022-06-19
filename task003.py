# 3. Вот вам текст:
# «Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. 
# Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, 
# по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. 
# Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. 
# Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. 
# Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. 
# В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, 
# в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил».
# Отфильтруйте его, чтобы этот текст можно было нормально прочесть. Предусмотрите вариант, 
# что мусорные слова могли быть написаны без использования запятых.

def del_some_words(my_text):
    trash_words = ['ну', 'короче', 'общем', 'говоря', 'кажется', 'эээ', 'как', 'бы', 'ясен', 'пень', 'кстати']
    my_text = my_text.lower().split()
    for word in trash_words:
        my_text = list(filter(lambda x: word not in x, my_text))
    return " ".join(my_text)

my_text = "Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. \
Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, \
по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. \
Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. \
Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. \
Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. \
В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, \
в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил."
my_text = del_some_words(my_text)
print(my_text)