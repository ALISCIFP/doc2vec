import random

def wirteList2txt(listname,f):
    for itm in listname:
        f.write(itm)

all_list = open('/home/tlmguest/Documents/Data/singleScan_list.txt','r')
TRA_folder_list = open('/home/tlmguest/data/Princeton/images/TRA_list.txt')

train_list = open('/home/tlmguest/data/Princeton/list/train.txt','w')
val_list = open('/home/tlmguest/data/Princeton/list/val.txt','w')
test_list = open('/home/tlmguest/data/Princeton/list/test.txt','w')


filenames = all_list.readlines()
filenames_TRA = TRA_folder_list.readlines()
TRA_dic=[]
all_dic={}

for filename in filenames:
    kv = filename.split(' ')
    all_dic[kv[0]] = kv[1]

for filename_TRA in filenames_TRA:
    print filename_TRA
    TRA_dic.append(filename_TRA.replace('\n',' ')+all_dic[filename_TRA.strip('\n')])
    

    
filenames = TRA_dic
print filenames
filenames.sort()  # make sure that the filenames have a fixed order before shuffling
random.seed(230)
random.shuffle(filenames) # shuffles the ordering of filenames (deterministic given the chosen seed)

split_1 = int(0.8 * len(filenames))
split_2 = int(0.9 * len(filenames))
train_filenames = filenames[:split_1]
dev_filenames = filenames[split_1:split_2]
test_filenames = filenames[split_2:]

wirteList2txt(train_filenames,train_list)
wirteList2txt(dev_filenames,val_list)
wirteList2txt(test_filenames,test_list)


train_list.close()
val_list.close()
test_list.close()
all_list.close()


