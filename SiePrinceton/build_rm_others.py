import os
train_txt ='/home/perla/Data/Princeton/PrincetonMRReports/old/train_others_pre.txt'
val_txt = '/home/perla/Data/Princeton/PrincetonMRReports/old/val_others_pre.txt'
test_txt = '/home/perla/Data/Princeton/PrincetonMRReports/old/test_others_pre.txt'

def list2OneDocv2(txt,outdoc): 
    outf = open(outdoc,'w')
    txt = open(txt,'r')
    julias =''
    lines = txt.readlines()
    for line in lines:

        line = line.replace('February 22, 2016','**DATE**')\
            .replace('July 7, 2016','**DATE**').replace('February 2015','**DATE**')\
            .replace('September 14, 2015','**DATE**').replace('September 2012','**DATE**').replace('April 26','**DATE**')\
            .replace('2012','**DATE**').replace('2013','**DATE**').replace('2014','**DATE**')\
            .replace('2015','**DATE**').replace('2016','**DATE**').replace('2017','**DATE**')\
            .replace('2006','**DATE**').replace('2008','**DATE**').replace('2010','**DATE**')\
            .replace('2007','**DATE**').replace('2009','**DATE**').replace('2011','**DATE**')\
            .replace('2002','**DATE**').replace('2009','**DATE**')
        for julia in line.split():
            julia = julia.rstrip('.').rstrip(';').rstrip(',')

            if julia.find('/', julia.find('/')+2 ) != -1:
                line = line.replace (julia, '**DATE**')

            if julia.find('XX') != -1:
                if julia.find('XX', julia.find('XX')+2 ) != -1:
                    line = line.replace(julia, '**VOLUME**')
                else:
                    line = line.replace(julia, '**AREA**')

        for julia in line.split():
            julia = julia.rstrip('.').rstrip(';').rstrip(',')
            if julia.find('CM') != -1 or julia.find('MMM') != -1 or julia.find('1cm') != -1 or julia.find('16mm') != -1 or julia.find('8-mm') != -1 or julia.find('14mm') != -1:
                line = line.replace(julia, '**LENGTH**', 1)
        outf.write(line)
    outf.close()

list2OneDocv2(train_txt,'/home/perla/Data/Princeton/PrincetonMRReports/parts/train_others_all.txt')
list2OneDocv2(val_txt,'/home/perla/Data/Princeton/PrincetonMRReports/parts/val_others_all.txt')
list2OneDocv2(test_txt,'/home/perla/Data/Princeton/PrincetonMRReports/parts/test_others_all.txt')
# for string in text.split():
#             if re.match("^\d+?\.\d+?$", string): #is None:
#                 print(string)
#                 string = '*FLOATE*'
#             else:
#                 string = string.replace('.', '')
