filein = open("mydoc.txt",'r')
line =" "
while line:
     line = filein.readline()
     #print(line)
     for w in line:
          if w == ' ':
               print('#',end = '')
          else:
               print(w,end = '')
filein.close()

filein = open("Mydoc.txt",'r')
for  line in filein:
     word= line .split()
     for w in word:
          print(w + '#',end ='')
     print()
filein.close()
