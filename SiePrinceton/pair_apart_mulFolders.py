fr = open('/home/tlmguest/Documents/Data/list_pair_all_subfolder_multiple.txt','r')

frm = open('/home/tlmguest/Documents/Data/mulfolderlist.txt','w')

lines=fr.readlines()
pre =['a','b','c']

for line in lines:
    cur = line.split(' ')
    print cur
    print cur[0]
    if not cur[0] == pre[0]:
        frm.write(cur[0]+'\n')

    pre = cur





fr.close()
frm.close()

