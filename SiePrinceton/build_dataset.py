import random

def wirteList2txt(listname,f):
    for itm in listname:
        f.write(itm)

all_list = open('/home/tlmguest/Documents/Data/singleScan_list.txt','r')

train_list = open('/home/tlmguest/Documents/Data/train.txt','w')
val_list = open('/home/tlmguest/Documents/Data/val.txt','w')
test_list = open('/home/tlmguest/Documents/Data/test.txt','w')


filenames = all_list.readlines()
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


