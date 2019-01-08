import os
all_list ='/home/perla/Data/Princeton/list_TRA/test.txt'

report_dir ='/home/zack/Data/PrincetonReports/PrincetonMRReports'
output_dir ='/home/perla/Data/Princeton/PrincetonMRReports/list_type'

def list2OneDoc(dir,_list):
    _type1 =[]
    # _type2 =[]
    # _type3 =[]
    # _type4 =[]
    # _type5 =[]
    _type6 =[]
    out1 = open(os.path.join(output_dir,'test_key.txt'),'w')
    # out2 = open(os.path.join(output_dir,'multi.txt'),'w')
    # out3 = open(os.path.join(output_dir,'short.txt'),'w')
    # out4 = open(os.path.join(output_dir,'BaseChest_wo.txt'),'w')
    # out5 = open(os.path.join(output_dir,'list_type5.txt'),'w')
    out6 = open(os.path.join(output_dir,'test_others.txt'),'w')
    listnames = open(_list,'r')
    listnamesL = listnames.readlines()
    listnames.close()
    for ln in listnamesL:
        fdname = ln.split(' ')[1][: -1]
        f = open(os.path.join(dir+'/discrp2',fdname))
        txt =f.read() #must write this line since f.read can only excute once
       
        # count = 0
        # count2 = 0
        # keyword = ['The appendix','The liver','The spleen','The kidneys','The bladder',\
        #     'The urinary','The pancreas','The gallbladder','The uterus','The lung'] #more than 200
        # for i in range(len(keyword)):
        #     if txt.find(keyword[i]) !=-1:
        #         count +=2
        # keyword2 = ['The adrenal','The visualized','The bowel','The prostate','The adrenal'] 
        # #'The pelvi' 'The arota',The left','The right' are below 100
        # for i in range(len(keyword2)):
        #     if txt.find(keyword2[i]) !=-1:
        #         count2 +=1
        # count += count2

        # a = txt.find('\n') #very beginning there is a \n
        # b = txt.find('\n',a+3) #exclude the \n\n situation
        # c = txt.find('\n',b+3)
        # d = txt.find('\n',c+3)
        # e = txt.find('\n',d+3)
        # f = txt.find('\n',e+3)

        if txt.find('Pancreas:') !=-1: #65
            _type1.append(ln)

        # elif txt.find('The liver, ') !=-1 or txt.find('The spleen, ')!=-1\
        #     or txt.find('The gallbladder, ')!=-1 or txt.find(', pancreas')!=-1\
        #     or txt.find(', spleen')!=-1 or txt.find('The pancreas, ')!=-1:
        #     _type2.append(ln)
        
        # elif (a == -1) or (b == -1) or (c == -1) or (d == -1) or (e == -1) or (f == -1): #define short
        #     # print(a,b,c,d,e,ln)
        #     _type3.append(ln)

        else:
            _type6.append(ln)

    out1.writelines(_type1)
    # out2.writelines(_type2)
    # out3.writelines(_type3)
    # out4.writelines(_type4)
    # out5.writelines(_type5)
    out6.writelines(_type6)
    out1.close()
    # out2.close()
    # out3.close()
    # # out4.close()
    # out5.close()
    out6.close()

list2OneDoc(report_dir,all_list)
