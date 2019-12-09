import glob
import re
import os

#Собираем все имена файлов по шаблону
txtfiles = []
for file in glob.glob("*.txt"):
    txtfiles.append(file)

#Открываем файл для дозаписи, открываем файл для чтения, преобразовываем, дописываем
j = 0
while j < 29:
    with open('ip_ban.txt', 'a', encoding="UTF-8") as fi:
        f = open(txtfiles[j], encoding="UTF-8")
        for line in f:
            st=""
            line=line.strip()
            for i in range(len(line)):
                n=line.find(" ")
                if n==-1:
                    st=st+line
                    break
                st=st+line[:n]+' '
                line=line[n+1:]
                line=line.lstrip()
            print(st.rstrip())
            fi.write(st + "\n")
        f.close()
    j = j + 1
