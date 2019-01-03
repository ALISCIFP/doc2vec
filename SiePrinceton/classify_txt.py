import os
train_list ='/home/perla/Data/Princeton/list_TRA/train.txt'
val_list = '/home/perla/Data/Princeton/list_TRA/val.txt'
test_list = '/home/perla/Data/Princeton/list_TRA/test.txt'

report_dir ='/home/zack/Data/PrincetonReports/PrincetonMRReports'
output_dir ='/home/perla/Data/Princeton/PrincetonMRReports'

def list2OneDoc(dir,_list):
    _type1 =[]
    _type2 =[]
    _type3 =[]
    _type4 =[]
    out1 = open(os.path.join(output_dir,'list_type1.txt'),'w')
    out2 = open(os.path.join(output_dir,'list_type2.txt'),'w')
    out3 = open(os.path.join(output_dir,'list_type3.txt'),'w')
    out4 = open(os.path.join(output_dir,'list_type4.txt'),'w')
    listnames = open(_list,'r')
    listnamesL = listnames.readlines()
    listnames.close()
    for ln in listnamesL:
        fdname = ln.split(' ')[1][: -1]
        f = open(os.path.join(dir+'/discrp2',fdname))
        txt =f.read() #must write this line since f.read can only excute once
        if txt.find('ABDOMEN/PELVIC') !=-1: #65
            _type1.append(ln)
        elif txt.find('Base of Chest') !=-1: #202
            _type2.append(ln)
        elif txt.find('ABDOMEN') !=-1:
            _type3.append(ln)
        else:
            _type4.append(ln)
        # print(_type2)
    out1.writelines(_type1)
    out2.writelines(_type2)
    out3.writelines(_type3)
    out4.writelines(_type4)
    out1.close()
    out2.close()
    out3.close()
    out4.close()


list2OneDoc(report_dir,train_list)
# list2OneDoc(report_dir,val_list,'val_all.txt')
# list2OneDoc(report_dir,test_list,'test_all.txt')