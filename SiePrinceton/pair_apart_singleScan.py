fr = open('/home/tlmguest/Documents/Data/list_pair_all.txt','r')
fru = open('/home/tlmguest/Documents/Data/singleScan_list.txt','w')

frm = open('/home/tlmguest/Documents/Data/mulfolderlist.txt','r')

lines=fr.readlines()
mlines = frm.readlines()
print mlines

for line in lines:
    line_s = line.split(' ')
    print line_s[0]
    if not line_s[0]+'\n' in mlines:
        fru.write(line)

fr.close()
fru.close()
frm.close()

