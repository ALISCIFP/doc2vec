import os
train_list ='/media/Hitachi/Data/Princeton/PrincetonMRReports/list_type/train_key.txt'
val_list = '/media/Hitachi/Data/Princeton/PrincetonMRReports/list_type/val_key.txt'
test_list = '/media/Hitachi/Data/Princeton/PrincetonMRReports/list_type/test_key.txt'

report_dir ='/home/zack/Data/PrincetonReports/PrincetonMRReports'
output_dir ='/home/perla/Data/Princeton/PrincetonMRReports/parts'

def list2OneDoc(dir,list,outdoc):
    outf = open(os.path.join(output_dir,outdoc),'w')
    listnames = open(list,'r')
    listnamesL = listnames.readlines()
    listnames.close()
    for ln in listnamesL:
        fdname = ln.split(' ')[1][: -1]
        f = open(os.path.join(dir+'/discrp2',fdname))
        contents =' '
        count =0
        txt = f.read().replace(' cm','CM').replace(' x ','XX').replace(' mm','MMM')

        for julia in txt.split():
            julia = julia.rstrip('.').rstrip(';').rstrip(',')
            if julia.find('/', julia.find('/')+2 ) != -1:
                txt = txt.replace (julia, '**DATE**')
            if julia.find('XX') != -1:
                if julia.find('XX', julia.find('XX')+2 ) != -1:
                    txt = txt.replace(julia, '**VOLUME**')
                else:
                    txt = txt.replace(julia, '**AREA**')
        for julia in txt.split():
            julia = julia.rstrip('.').rstrip(';').rstrip(',')
            if julia.find('CM') != -1 or julia.find('MMM') != -1 or julia.find('1cm') != -1 or julia.find('16mm') != -1 or julia.find('8-mm') != -1 or julia.find('14mm') != -1:
                txt = txt.replace(julia, '**LENGTH**', 1)
        txt = txt.replace('\n\n','\n').replace('ABDOMEN/PELVIC CT:','').replace('ABDOMEN:','').replace('PELVIS:','')\
            .replace('ABDOMEN CT:','').replace('PELVIC CT:','')\
            .replace('CT pelvis\n','Pelvis:').replace('CT PELVIS\n','Pelvis:').replace('CT pelvis:\n','Pelvis:')\
            .replace('CT ABDOMEN','').replace('CT abdomen:','').replace('CT abdomen','')\
            .replace('\n\n','\n').replace('Bones  ','Bones:').replace(' :',':').replace(';','.') #  replace('\s\s','\s')
            # .replace('Uterus and Adnexa:','Reproductive Organs:').replace('Reproductive Organs: Reproductive Organs:','')
        txt = txt.replace('\s\s','\s')


        for line in txt.split('\n'):#'f.read()delete the \r automatically apply  # or f.readlines() not line ='\n' has other problems
            if (line.find('Thank you') != -1
                    or line.find('PCW7') != -1
                    or line.find('communicated') !=-1 #results communicated by phone.
                    or line.find('I discussed') != -1
                    or line.find('was faxed to') != -1
                    or line.find('appreciate your') != -1 
                    or line.find('The results') != -1
                    or line.find('PROTOCOL') !=-1 ):
                break
            if not line =='' or line =='.':
                count += 1
                # key = 'key'
                for romeo in line.strip().lstrip('-').split('.'):
                    if romeo.find(':') == -1 and (romeo !='') and (romeo.isspace()==False):
                        romeo = key + romeo +'. '# '.' will be spilted
                         #add key before each begining of a sentence
                        for rom in romeo.strip().lstrip('-').split(): #how to exclude ''key
                            contents += rom + ' '    
                        contents =contents[:-2] + '. '#+'\n' #-2 is '. ' '@@'
                    else:
                        key = romeo[:romeo.find(':')+1]
                        for rom in romeo.strip().lstrip('-').split(): #how to exclude ''key
                            contents += rom + ' '
                        contents =contents[:-1] + '. '#+'\n' # =+ already equals to = +

        contents = contents[1:].replace('...','.').replace('..','.').replace(':.',':')\
            .replace('August 2016','**DATE**').replace('October 2016','**DATE**').replace('May 31, 2016','**DATE**')\
            .replace('June 27, 2016','**DATE**').replace('March 2017','**DATE**')\
            .replace('2012','**DATE**').replace('2013','**DATE**').replace('2014','**DATE**')\
            .replace('2015','**DATE**').replace('2016','**DATE**').replace('2017','**DATE**')\
            .replace('2006','**DATE**').replace('2008','**DATE**').replace('2010','**DATE**')\
            .replace('2007','**DATE**').replace('2009','**DATE**').replace('2011','**DATE**')
        outf.write(contents+'\n') #drop the first '. '
        # print('lines count',count)
        if count == 0:  print(fdname)
    outf.close()

list2OneDoc(report_dir,train_list,'train_key_all.txt')
list2OneDoc(report_dir,val_list,'val_key_all.txt')
list2OneDoc(report_dir,test_list,'test_key_all.txt')