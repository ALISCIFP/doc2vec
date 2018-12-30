import os
train_txt ='/home/perla/Data/Princeton/PrincetonMRReports/train_all.txt'
val_txt = '/home/perla/Data/Princeton/PrincetonMRReports/val_all.txt'
test_txt = '/home/perla/Data/Princeton/PrincetonMRReports/test_all.txt'

def list2OneDocv2(txt,outdoc): 
    outf = open(outdoc,'w')
    txt = open(txt,'r')
    julias =''
    for lines in txt.readlines():
        for julia in lines.split():
            if julia.find('CMCM') != -1: #or julia.find('MMMM'):
                if julia.find('XX') != -1:
                    if julia.find('XX', julia.find('XX')+1 ) != -1:
                        lines.replace(julia, '**VOLUME**')
                        print(julia)
                    else:
                        lines.replace(julia, '**AREA**')
                        # print(julia)
                else:
                    lines.replace(julia, '**LENGTH**')
                    print(julia)
            # print(line
        break
        # how to fully replace julia ??
    outf.wirtelines(lines)
    outf.close()

list2OneDocv2(train_txt,'/home/perla/Data/Princeton/PrincetonMRReports/train_all_v2.txt')
list2OneDocv2(val_txt,'/home/perla/Data/Princeton/PrincetonMRReports/val_all_v2.txt')
list2OneDocv2(test_txt,'/home/perla/Data/Princeton/PrincetonMRReports/test_all_v2.txt')
# for string in text.split():
#             if re.match("^\d+?\.\d+?$", string): #is None:
#                 print(string)
#                 string = '*FLOATE*'
#             else:
#                 string = string.replace('.', '')