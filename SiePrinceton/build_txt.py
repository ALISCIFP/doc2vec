import os
train_list ='/home/perla/Data/Princeton/list_TRA/train.txt'
val_list = '/home/perla/Data/Princeton/list_TRA/val.txt'
test_list = '/home/perla/Data/Princeton/list_TRA/test.txt'

report_dir ='/home/zack/Data/PrincetonReports/PrincetonMRReports'
output_dir ='/home/perla/Data/Princeton/PrincetonMRReports'
3271152296296079
def list2OneDoc(dir,list,outdoc):
    outf = open(os.path.join(output_dir,outdoc),'w')
    listnames = open(list,'r')
    listnamesL = listnames.readlines()
    listnames.close()
    for ln in listnamesL:
        fdname = ln.split(' ')[1][: -1]
        f = open(os.path.join(dir+'/discrp2',fdname))
        romeos =' '
        count =0
        for line in f.read().split('\n'):#'f.read()delete the \r automatically apply  # or f.readlines() not line ='\n' has other problems
            if (line.find('Thank you') != -1
                    or line.find('I discussed') != -1
                    or line.find('was faxed to') != -1
                    or line.find('appreciate your') != -1 ):
                break
            if not line =='':
                count += 1
                for romeo in line.strip().lstrip('-').split():
                    try:
                        float(romeo)
                        romeos += romeo + ' '
                    except ValueError:
                        romeo = romeo.replace('.',';')
                        romeos += romeo + ' '
                romeos = romeos[:-1].rstrip(';')+ '. ' #delete space and the last simicolon ';'
        romeos = romeos[1:]
        outf.write(romeos+'\n') #drop the first '. '
        # print('lines count',count)
        if count == 0:  print(fdname)
            '''
            delete two in train because of void:
            
            1406651423 2335494428060423.txt in line 405
            1902028535 5974164134543241.txt in line 36

            '''
    outf.close()


list2OneDoc(report_dir,train_list,'train_all_v2.txt')
list2OneDoc(report_dir,val_list,'val_all_v2.txt')
list2OneDoc(report_dir,test_list,'test_all_v2.txt')