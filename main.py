
import os
from pathlib import Path
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

# Записываем содержимое этих файлов в новый файл SortedByNameTxt.txt,
# который будет находится рядом с main.py 
newFile = open('SortedByNameTxt.txt', 'w+')
for p in txtFiles :
    thr = open(p, 'r')
    newFile.write(thr.read())
    thr.close()
newFile.close()
