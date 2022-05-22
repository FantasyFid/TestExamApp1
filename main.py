
from msilib.schema import Error
import os
from pathlib import Path
import re
import codecs

# Эта функция ищет и записывает в список все пути до файлов .txt, которые
# находятся с main.py на одном уровне вложенности и ниже
def findAllFiles() : 
    path = os.getcwd()
    queue = []
    queue.append(path)
    txtFiles = []

    while(len(queue) > 0) :
        current = queue.pop(0)
        siblings = os.listdir(current)
        for sibling in siblings :
            crntPath = os.path.join(current, sibling)
            if (os.path.isdir(crntPath)) :
                queue.append(crntPath)
            else :
                if os.path.splitext(sibling)[1] == '.txt' :
                    txtFiles.append(crntPath)
    
    return txtFiles

txtFiles = findAllFiles()
# Сортируем эти файлы по названию
txtFiles.sort(key = lambda e : Path(e).name)
print("Список отсортированных по названию файлов: \n" + str(txtFiles))
# Записываем содержимое этих файлов в новый файл SortedByNameTxt.txt,
# который будет находится рядом с main.py 
newFile = codecs.open('SortedByNameTxt.txt', mode = 'w+', encoding = 'utf-8', errors = 'ignore')
for p in txtFiles :
    thr = codecs.open(p, mode = 'r', encoding = 'utf-8', errors = 'ignore')
    newFile.write(thr.read())
    thr.close()
newFile.close()

#Составим словарь с зависимостями для каждого файла. Ключ - путь до конкретного текстового файла.
#Значение - список с путями до файлов, от которых он зависит
D = dict()
for p in txtFiles :
    thr = codecs.open(p, mode = 'r', encoding = 'utf-8', errors = 'ignore')
    data = thr.read()
    thr.close()

    #Ищем все совпадения с RegEx для нахождения всех require
    result = re.findall("require [‘'][:\-/\\ \wА-Яа-я]*[’']", data)
    siblings = []
    #Получаем из require путь до файла с зависимостью и преобразуем
    #этот путь в абсолютный
    for elem in result :
        elem = re.split("[‘']", elem)[1][:-1]
        elem = os.path.join(os.getcwd(), Path(elem + '.txt'))
        siblings.append(elem)
    D[p] = siblings

#Реализация топологической сортировки
def TopologicalSort(G):
    in_degrees = dict((u, 0) for u in G)
    for u in G:
        for v in G[u]:
            in_degrees[v] += 1
    queue = [u for u in G if in_degrees[u] == 0]
    res = []
    while queue:
        u = queue.pop()
        res.append(u)
        for v in G[u]:
            in_degrees[v] -= 1
            
            if in_degrees[v] == 0:
                queue.append(v)
    return res[::-1]


try :
    #Применяем топологическую сортировку к словарю с зависимостями
    topologicalySorted = TopologicalSort(D)
    print("Топологически отсортированный список с зависимостями: \n" + str(topologicalySorted))
    #Объединяем все зависимые файлы в один новый и помещаем
    #его на одном уровне вложенности с main.py
    newFile = codecs.open('RelatedTxtFiles.txt', mode = 'w+', encoding = 'utf-8', errors = 'ignore')
    for p in topologicalySorted :
        thr = codecs.open(p, mode = 'r', encoding = 'utf-8', errors = 'ignore')
        newFile.write(thr.read())
        thr.close()
    newFile.close()
except KeyError :
    #KeyError во время выполнения топологической сортировки означает наличие
    #циклической зависимости
    print('В этой файловой системе присутствует циклическая зависимость')

