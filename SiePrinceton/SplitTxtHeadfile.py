import glob
import os
DIR='/home/tlmguest/Documents/Data/PrincetonMRReports/head2/'
ODIR='/home/tlmguest/Documents/Data/PrincetonMRReports'

SPLITWord0='CLINICAL_STATEMENT'
SPLITWord1='IMPRESSION:'
SPLITWord1p='IMPRESSION :'
SPLITWord2 ='PROCEDURE:'
SPLITWord2p ='EXAM:'

SPLITWord3 ='COMPARISON:'
def mkdirs(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

for i in xrange(4):
    mkdirs(os.path.join(ODIR,'SPLITWord'+str(i)))


fileList=(glob.glob(DIR+'*.txt'))

#print fileList
for f in fileList:
    wholeText = open(f,'r').read()
    txtName = os.path.basename(f)
    if SPLITWord1 in wholeText:
        files = wholeText.split(SPLITWord1)
        if SPLITWord2 in files[1]:
            files2 = files[1].split(SPLITWord2)
            files.pop(1)
            files.append(files2[0])
            if SPLITWord3 in files2[1]:
                files3 = files2[1].split(SPLITWord3)
                files.append(files3[0])
                files.append(files3[1])
            else:
                print f
                print 'no SPLITWord3'
                files.append(files2[1])
                files.append('')
        elif SPLITWord2p in files[1]:
            files2 = files[1].split(SPLITWord2p)
            files.pop(1)
            files.append(files2[0])
            if SPLITWord3 in files2[1]:
                files3 = files2[1].split(SPLITWord3)
                files.append(files3[0])
                files.append(files3[1])
            else:
                print f
                print 'no SPLITWord3'
                files.append(files2[1])
                files.append('')   
        else:
            print f
            print 'no SPLITWord2'
    elif SPLITWord1p in wholeText:
        files = wholeText.split(SPLITWord1p)
        if SPLITWord2 in files[1]:
            files2 = files[1].split(SPLITWord2)
            files.pop(1)
            files.append(files2[0])
            if SPLITWord3 in files2[1]:
                files3 = files2[1].split(SPLITWord3)
                files.append(files3[0])
                files.append(files3[1])
            else:
                print f
                print 'no SPLITWord3'
                files.append(files2[1])
                files.append('')
        elif SPLITWord2p in files[1]:
            files2 = files[1].split(SPLITWord2p)
            files.pop(1)
            files.append(files2[0])
            if SPLITWord3 in files2[1]:
                files3 = files2[1].split(SPLITWord3)
                files.append(files3[0])
                files.append(files3[1])
            else:
                print f
                print 'no SPLITWord3'
                files.append(files2[1])
                files.append('')
        else:
            print f
            print 'no SPLITWord2'

    else:
        print f
        print 'no SPLITWord1'
    for num, file in enumerate(files):
        open((os.path.join(ODIR,'SPLITWord'+str(num))+'/'+txtName),'w').write(file)
    







