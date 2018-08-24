import os
import shutil
import glob
import re
# fr = open('/home/tlmguest/Documents/Data/list_pair_all_subfolder.txt','r')
# d = {}
# al_lines = fr.readlines()
# for al_line in al_lines:
#     kv = al_line.split(' ')
#     kv[2] = kv[2].strip('\n').strip('\r')
#     d[kv[1]] = [kv[0],kv[2]]

# print (d)


# abd = open('/home/tlmguest/Documents/Data/abd_mhd_flist.txt','w')
# cor = open('/home/tlmguest/Documents/Data/cor_mhd_flist','w')
# sag = open('/home/tlmguest/Documents/Data/sag_mhd_flist','w')


single = open('/home/tlmguest/Documents/Data/singleScan_list.txt','r')
multi= open('/home/tlmguest/Documents/Data/folders_with_multiple_scans.txt','r')

frm = open('/home/tlmguest/Documents/Data/list_pair_all_subfolder_multiple.txt','w')
newFolder ='/home/tlmguest/data/Princeton/images'
oldFolder1 = '/home/tlmguest/data/princeton_mhd'
oldFolder2 ='/home/tlmguest/data/mhd_multi'


single_lines = single.readlines()

for s_line in single_lines:
    s_cur = s_line.split(' ')
    
    src_dir = os.path.join(oldFolder1,s_cur[0])
    src_f = glob.glob(src_dir+'/*mhd')
    abdcheck = False
    corcheck = False
    sagcheck = False
    for v_f in src_f:
        if re.search('abd',v_f,re.IGNORECASE):
            abdcheck = True

        if re.search('sag',v_f,re.IGNORECASE):
            sagcheck =True
  
        if not re.search('cor',v_f,re.IGNORECASE):
            corcheck = True
    if not abdcheck:
        print 'abd', s_line
    if not corcheck:
        print 'cor', s_line        
    if not sagcheck:
        print 'sag', s_line







# fr.close()
# fru.close()
frm.close()
single.close()
multi.close()

