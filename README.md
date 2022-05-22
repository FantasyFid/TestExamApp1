# TestExamApp1

Файл main.py является решением первой задачи отборочного этапа на стажировку в Doczilla.
Я использовал язык программирования python 3.8 и некоторые стандартные библиотеки.
Для проверки его работы поместите main.py в желаемую директорию с текстовыми файлами.

![image](https://user-images.githubusercontent.com/79358824/169711760-46e108ef-bdee-4bfb-8ebd-b90d3b9ccb36.png)

Затем запустите интерпретацию любым способом:
  /d/Desctop/test> py main.py
В дирректории на одном уровне вложенности с main.py появятся 2 файла:

![image](https://user-images.githubusercontent.com/79358824/169711848-659d927e-4379-426f-9088-59051107e0b3.png)

  1)SortedByNameTxt.txt - ответ на основную часть задачи. (Склеенные в алфавитном порядке текстовые файлы)
  2)RelatedTxtFiles.txt - ответ на дополнительную задачу. (Склеенные в топологически отсортированном порядке текстовые файлы)
Также полезная информация будет выведена в консоль:
  /d/Desctop/test> py main.py
  Список отсортированных по названию файлов:
  ['D:\\Desctop\\test\\Folder 1\\File 1-1.txt', 'D:\\Desctop\\test\\Folder 2\\File 2-1.txt', 'D:\\Desctop\\test\\Folder 2\\File 2-2.txt']
  Топологически отсортированный список с зависимостями:
  ['D:\\Desctop\\test\\Folder 2\\File 2-1.txt', 'D:\\Desctop\\test\\Folder 1\\File 1-1.txt', 'D:\\Desctop\\test\\Folder 2\\File 2-2.txt']
В случае циклической зависимости в консоль будет выведено сообщение:
  В этой файловой системе присутствует циклическая зависимость
