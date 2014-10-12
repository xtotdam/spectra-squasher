Spectra-Squasher
================

Собирает файлы со спектрами в один большой, для последующй вставки в Excel.
Для использования необходим интерпретатор Python 2.x. [(например, Python 2.7.8)](https://www.python.org/downloads/release/python-278/)

###Использование
1. Положить скрипт в папку с файлами спектров
2. Ввести маску и диапазон
3. Скопировать результат в Excel

####Маска
Предполагается, что имена файлов со спектрами имеют вид:
```
проба1 200.txt
проба1 210.txt
проба1 220.txt
проба1 230.txt
проба1 240.txt
...
```
Отсюда маска для них будет выглядеть `проба1 {}.txt`, где `{}`-место для диапазона.
Маску для файлов с пробелами в имени **обязательно** оборачивать в кавычки `""`

####Диапазон
`x:y:z` - набор значений от `x` до `z` включительно с шагом `y`

`x,y,z` - просто перечисление

####Примеры
`"проба1 {}.txt" 200:400,480,500:50:700` - **ошибка**: не указан шаг

`"проба1 {}.txt" 200:50:400:10:450,480,500:50:700` - **ошибка**: все значения после третьего двоеточия до запятой будут потеряны.

`проба1 {}.txt 200:50:400,480,500:50:700` - **ошибка**: в маске есть пробел, после ее разбора имя разобьется на два куска.

`"проба1 {}.txt" 200:50:400,480,500:50:700` - **правильно**, преобразуется в 
```
проба1 200.txt
проба1 250.txt
проба1 300.txt
проба1 350.txt
проба1 400.txt
проба1 480.txt
проба1 500.txt
проба1 550.txt
проба1 600.txt
проба1 650.txt
проба1 700.txt
```
