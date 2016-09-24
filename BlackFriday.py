import sys 
from sys import stdin
import io


num  = int(stdin.read(1))
text  = stdin.read()
bestNumber = 0
numbers = map(int, text.split())
dict = {}
list = []

for x in numbers:
    list.append(x)
    if x not in dict:
        dict.update({x : 1})
    else:
        dict[x] = (dict[x] + 1)     
            
    

for y in dict:
    if dict[y] == 1:
        if int(y) > bestNumber:
            bestNumber = int(y)
            # print int(y)
        pass
if bestNumber == 0:
    sys.stdout.write("none")

else:
    i = 1
    for j in list:
        if j == bestNumber:
            sys.stdout.write(str(i))
            break
        i = i + 1
quit()