"""
Дана строка, разделённая пробелами, посчитать количество слов в ней. Циклы не использовать. Только метод count()
Код ниже работает только при условии, что между словами ТОЛЬКО 1 пробел. Если в строке действительно один пробел,
то считает верно. В нашем случае 30 слов в строке, однако если добавить один пробел, то будет уже 31, а если убрать, то 29.
"""

s = 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Voluptate eveniet sit itaque quo facere possimus a quis aliquam nam ab officiis provident, soluta molestias labore est odit optio blanditiis inventore!'
print(s.count(' ')+1)

"""
Код ниже уберегает нас от непредвиденных обстоятельств в виде лишних пробелов
re.split(pattern, string, maxsplit=0)	
Аналог str.split(), только разделение происходит по подстрокам, подходящим под шаблон pattern;
"""
import re
#\s+	один или больше space символов, то же что и [\n\t\r\f]
def counter(s):
    return len(re.split('\s+', s))
 
string = 'Lorem ipsum dolor          sit amet consectetur, adipisicing elit. Voluptate eveniet sit itaque quo facere possimus a quis aliquam nam ab officiis provident, soluta molestias labore est odit optio blanditiis inventore!'
print(counter(string))

