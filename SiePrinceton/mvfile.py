import os
import shutil
import glob
import re



# abd = open('/home/tlmguest/Documents/Data/abd_mhd_flist.txt','w')
# cor = open('/home/tlmguest/Documents/Data/cor_mhd_flist','w')
# sag = open('/home/tlmguest/Documents/Data/sag_mhd_flist','w')


single = open('/home/zack/Data/PrincetonReports/singleScan_list.txt','r')

newFolder ='/home/zack/Data/Princeton/images'
oldFolder1 = '/home/zack/Data/princeton_mhd'
oldFolder2 ='/home/zack/Data/mhd_multi'


def mkdirs(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
TRA_folder = newFolder+'/TRA'
mkdirs(TRA_folder)
SAG_folder = newFolder+'/SAG'
mkdirs(SAG_folder)
COR_folder = newFolder+'/COR'
mkdirs(COR_folder)

single_lines = single.readlines()

for s_line in single_lines:
    s_cur = s_line.split(' ')
    
    src_dir = os.path.join(oldFolder1,s_cur[0])
    src_f = glob.glob(src_dir+'/*mhd')
    for v_f in src_f:
        if re.search('abd',v_f,re.IGNORECASE):
            dst_dir = os.path.join(TRA_folder,s_cur[0])
            mkdirs(dst_dir)
            basename = os.path.basename(v_f)
            basename_ =basename.replace('.mhd','')
            new_basename_ = basename_.replace(' ','_')
            dst_f = os.path.join(dst_dir,basename.replace(' ','_'))
            v_fh =open(v_f,'r')
            dst_fh = open(dst_f,'w')
            fcontent = v_fh.read()
            dst_content = fcontent.replace(basename_,new_basename_)
            dst_fh.write(dst_content)
            v_fh.close()
            dst_fh.close()
            shutil.copy(v_f.replace('.mhd','.img'),dst_f.replace('.mhd','.img'))
        if re.search('sag',v_f,re.IGNORECASE):
            dst_dir = os.path.join(SAG_folder,s_cur[0])
            mkdirs(dst_dir)
            basename = os.path.basename(v_f)
            basename_ =basename.replace('.mhd','')
            new_basename_ = basename_.replace(' ','_')
            dst_f = os.path.join(dst_dir,basename.replace(' ','_'))
            v_fh =open(v_f,'r')
            dst_fh = open(dst_f,'w')
            fcontent = v_fh.read()
            dst_content = fcontent.replace(basename_,new_basename_)
            dst_fh.write(dst_content)
            v_fh.close()
            dst_fh.close()
            shutil.copy(v_f.replace('.mhd','.img'),dst_f.replace('.mhd','.img'))    
        if re.search('cor',v_f,re.IGNORECASE):
            dst_dir = os.path.join(COR_folder,s_cur[0])
            mkdirs(dst_dir)
            basename = os.path.basename(v_f)
            basename_ =basename.replace('.mhd','')
            new_basename_ = basename_.replace(' ','_')
            dst_f = os.path.join(dst_dir,basename.replace(' ','_'))
            v_fh =open(v_f,'r')
            dst_fh = open(dst_f,'w')
            fcontent = v_fh.read()
            dst_content = fcontent.replace(basename_,new_basename_)
            dst_fh.write(dst_content)
            v_fh.close()
            dst_fh.close()
            shutil.copy(v_f.replace('.mhd','.img'),dst_f.replace('.mhd','.img'))







single.close()
# abd.close()
# cor.close()
# sag.close()

