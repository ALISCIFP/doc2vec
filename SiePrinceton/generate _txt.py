import os
dir ='/home/zack/Data/PrincetonReports/PrincetonMRReports'
listdir = '/home/perla/Data/Princeton/PrincetonMRReports/list_type'

def generate_txt(_type):
    outf = open(os.path.join(listdir,_type+'_all.txt'),'w')
    listnames = open(os.path.join(listdir,_type+'.txt'),'r')
    listnamesL = listnames.readlines()
    listnames.close()
    for ln in listnamesL:
        fdname = ln.split(' ')[1][: -1] #nologer -2 
        f = open(os.path.join(dir+'/discrp2',fdname))
        disp= f.read()#.replace('\n','') #nologer \r\n
        disp =disp.replace('\n\n','\n')
        disp =disp.replace('Thank you for the courtesy of this referral.',ln)
        outf.write(disp+'\n')
    outf.close()

generate_txt('train_key')
generate_txt('train_others')
generate_txt('val_key')
generate_txt('val_others')
generate_txt('test_key')
generate_txt('test_others')
# generate_txt('multi')