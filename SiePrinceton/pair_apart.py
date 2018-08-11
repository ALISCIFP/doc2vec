fr = open('/home/tlmguest/Documents/Data/list_pair_all_subfolder.txt','r')
fru = open('/home/tlmguest/Documents/Data/list_pair_all_subfolder_unique.txt','w')

frm = open('/home/tlmguest/Documents/Data/list_pair_all_subfolder_multiple.txt','w')

lines=fr.readlines()
pre =['a','b','c']

for line in lines:
    cur = line.split(' ')
    print cur
    print cur[0]
    if cur[0] == pre[0]:
        frm.write(line)

    else:
        fru.write(line)

    pre = cur





fr.close()
fru.close()
frm.close()

