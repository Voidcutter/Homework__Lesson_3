import pymorphy2
morph = pymorphy2.MorphAnalyzer()

file = open('text.txt', 'r', encoding = 'utf-8')

text = file.read()

text = text.replace('-', " ").replace('\n', " ").replace('.', '').replace(':', '').replace('!', '').replace(',','').replace('«','').replace('»','').replace(';','').replace('?','').replace('(','').replace(')','').replace('— ','').replace('"', '')

text = text.split(' ')

text = list(map(str.lower, text))

for i in range(0, len(text)):
    text[i] = morph.parse(text[i])[0].normal_form

dict_i = 0
text_dict = {}

while len(text) > 0:
    counter = 0
    delete = text[0]
    for i in text:
        if i == delete:
            counter += 1
            text.pop(text.index(i))
    text_dict[delete] = counter

text_list = list(text_dict.items())
text_list.sort(key=lambda i: i[1])

print("Пять наиболее часто встречающихся слов:")
for i in text_list[len(text_list) - 5: len(text_list)]:
    print(i[0], ' — ', i[1], sep = '')

print("")

print("Количество разных слов:", len(text_dict.keys()))

# print(text_dict)
# print(text_list[len(text_list) - 5: len(text_list)])

