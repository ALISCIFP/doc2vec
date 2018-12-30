import os
train_txt ='/home/perla/Data/Princeton/PrincetonMRReports/train_all.txt'
val_txt = '/home/perla/Data/Princeton/PrincetonMRReports/val_all.txt'
test_txt = '/home/perla/Data/Princeton/PrincetonMRReports/test_all.txt'

def list2OneDocv2(txt,outdoc): 
    outf = open(outdoc,'w')
    txt = open(txt,'r')
    julias =''
    lines = txt.readlines()
    for line in lines:
        for julia in line.split():
            julia = julia.rstrip(';').rstrip('.')
            if julia.find('CM') != -1 or julia.find('MMM') != -1:
                if julia.find('XX') != -1:
                    if julia.find('XX', julia.find('XX')+2 ) != -1:
                        line = line.replace(julia, '**VOLUME**')
                        # print(line)
                    else:
                        line = line.replace(julia, '**AREA**')
                        # print(julia)
                else:
                    line = line.replace(julia, '**LENGTH**')
                    # print(julia)
            # print(line
        # break
        outf.write(line)
        # how to fully replace julia ??
    # outf.wirtelines(lines)
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