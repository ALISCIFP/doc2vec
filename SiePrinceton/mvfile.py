import os
import shutil
fr = open('/home/tlmguest/Documents/Data/list_pair_all_subfolder.txt','r')
fru = open('/home/tlmguest/Documents/Data/list_pair_all_subfolder_unique.txt','w')
single = open('/home/tlmguest/Documents/Data/singleScan_list.txt','r')
multi= open('/home/tlmguest/Documents/Data/folders_with_multiple_scans.txt','r')

frm = open('/home/tlmguest/Documents/Data/list_pair_all_subfolder_multiple.txt','w')
newFolder ='/home/tlmguest/data/Princeton/images'

def mkdirs(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
view_folder = newFolder+'/TRA'
mkdirs(view_folder)
single_lines = single.readlines()

for s_line in single_lines:
    s_cur = s_line.split(' ')
    mkdirs(os.path.join(newFolder,s_cur[0]))
    shutil.copy()

lines=fr.readlines()


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

