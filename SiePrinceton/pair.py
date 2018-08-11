import os, sys
def splitall(path):
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts

def splitpath(path, maxdepth=20):
    (head, tail) = os.path.split(path)
    return splitpath(head, maxdepth - 1) + [tail] \
        if maxdepth and head and head != path \
        else [head or tail]

raw_list='/home/tlmguest/Documents/Data/listxt_processed.txt'
fr = open('/home/tlmguest/Documents/Data/list_pair_all_subfolder.txt','w')


f=open(raw_list,'r')
lines=f.readlines()
i=0
j=0
every5lines = []
for line in lines:
    every5lines.append(line)
    i=i+1
    if i%5 == 0:
        # print every5lines
        fpair = every5lines[0][35:45]+' '+every5lines[2][-22:-2]+' '+every5lines[0][46:-1]+'\n'
        print fpair
        fr.write(fpair)

        every5lines = []




f.close()

