import os.path
if os.path.isfile("y.txt"):
    file = open("y.txt",'a')
    file.write('檔案94存在')
else:
    file = open('y.txt','w')
    file.write('這是新的')
file.close()