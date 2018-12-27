import os



train_list ='/home/tlmguest/Documents/Data/train.txt'
val_list = '/home/tlmguest/Documents/Data/val.txt'
test_list = '/home/tlmguest/Documents/Data/test.txt'

report_dir ='/home/tlmguest/Documents/Data/PrincetonMRReports'
#/home/zack/Data/PrincetonReports/PrincetonMRReports

def list2OneDoc(dir,list,outdoc):
    outf = open(os.path.join(dir,outdoc),'w')
    listnames = open(list,'r')
    listnamesL = listnames.readlines()
    listnames.close()
    for ln in listnamesL:
        fdname = ln.split(' ')[1][: -2]
        f = open(os.path.join(dir+'/discrp2',fdname))
        disp= f.read().replace('\r\n','')
        disp =disp.replace('Thank you for the courtesy of this referral.','')


        outf.write(disp+'\n')
    outf.close()


list2OneDoc(report_dir,train_list,'train_all.txt')
list2OneDoc(report_dir,val_list,'val_all.txt')
list2OneDoc(report_dir,test_list,'test_all.txt')


