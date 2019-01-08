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
                # print(julia)
                # if julia.find('XX') != -1:
                #     if julia.find('XX', julia.find('XX')+2 ) != -1:
                #         line = line.replace(julia, '**VOLUME**')
                #     else:
                #         line = line.replace(julia, '**AREA**')
                # else:
                line = line.replace(julia, '**LENGTH**', 1)
            
        outf.write(line)
    # outf.wirtelines(lines)
    outf.close()

list2OneDocv2(train_txt,'/home/perla/Data/Princeton/PrincetonMRReports/train_others_all.txt')
list2OneDocv2(val_txt,'/home/perla/Data/Princeton/PrincetonMRReports/val_others_all.txt')
list2OneDocv2(test_txt,'/home/perla/Data/Princeton/PrincetonMRReports/test_others_all.txt')
# for string in text.split():
#             if re.match("^\d+?\.\d+?$", string): #is None:
#                 print(string)
#                 string = '*FLOATE*'
#             else:
#                 string = string.replace('.', '')
'''
February 22, 2016
July 7, 2016
February 2015
'''