#Прочитать файл
#имя файла с текстом
#имя файля для дозаписи(нижний регистр)
#номер строки которую надо дозаписать
text_in = open('file.txt', 'r', encoding="UTF-8")
lines = text_in.read().split('\n')
text_in.close()

text_in = open(lines[0], 'r', encoding="UTF-8")
wr = text_in.read().split('\n')
wr = wr[int(lines[2])]
text_in.close()

text_in = open(lines[1], 'a', encoding="UTF-8")
text_in.write(wr)
text_in.close()
