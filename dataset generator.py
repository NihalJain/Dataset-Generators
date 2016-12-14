import sys
import os

working_dir = input("Enter Working Directory: ")
if (working_dir[len(working_dir)-1] != '/'):
    working_dir=working_dir + '/'
sys.path.append(working_dir)

datasetname = input("Enter Dataset Name: ")
if not os.path.exists(working_dir+datasetname):
    os.makedirs(working_dir+datasetname)


# items=[ "pepsi",
#         "cola",
#         "nokia mobile",
#         "samsung mobile",
#         "tide",
#         "ariel",
#         "lays",
#         "kurkure",
#         "kohinoor rice",
#         "taj tea",
#         "lux soap",
#         "dove shampoo",
#         "dove soap",
#         "cheetos",
#         "uncle chips",
#         "dairy milk",
#         "milky bar",
#         "parle g",
#         "center fresh",
#         "levis shirt",
#         "spykar jeans",
#         "jockey uv",
#         "fastrack watch",
#         "rebook shoes",
#         "citizen watch",
#         "funskool toys",
#         "blackberry suit",
#         "prestige cooker",
#         "nirlep pan",
#         "pepsodent",
#         "colgate"]


#ADDED
items = []
for i in range(10001):
	items.append(str(i))


no_of_items = int(input("Number of Items: "))
items = items[:no_of_items]

id_item_map=dict()
item_id_map=dict()

#creating a dictionary / mapping
for i in range(len(items)):
    id_item_map[i]=items[i]
    item_id_map[items[i]]=i   

#writing this mapping to a file
f1 = open(working_dir+datasetname+'/'+'id_item_mapping.txt','w')
for item_no,item in id_item_map.items():
    f1.write(str(item_no)+'\t'+item+'\n')
f1.close()

f1 = open(working_dir+datasetname+'/'+'item_id_mapping.txt','w')
for item,item_no in item_id_map.items():
    f1.write(item+'\t'+str(item_no)+'\n')
f1.close()

# print "Items: "
# print "ID::\tItem"
# for i in id_item_map.keys():
#     print str(i)+"::\t"+id_item_map[i]
    
#print "\n"

me_items_map =dict()
no_of_me_items = int(input("Number of Mutual Exclusive Pairs: "))
for i in range(0,no_of_me_items):    
    itm1 = int(input("Enter Item ID 1: "))
    itm2 = int(input("Enter Item ID 2 (this item will be treated mutually exclusive of item 1): "))    
    me_items_map[item_id_map[items[itm1]]] = item_id_map[items[itm2]]
    me_items_map[item_id_map[items[itm2]]] = item_id_map[items[itm1]]


no_of_transactions = int(input("Number of Transactions: "))

#generating dataset
import random
f1=open(working_dir+datasetname+'/'+'hor_'+str(no_of_items)+'_'+str(no_of_transactions)+'.txt','w')
f2=open(working_dir+datasetname+'/'+'dataset_verbrose.txt','w')
f3=open(working_dir+datasetname+'/'+'dataset.csv','w')
f4=open(working_dir+datasetname+'/'+'dataset_verbrose.csv','w')

#ADDED
f5 = open(working_dir+datasetname+'/'+'vert_'+str(no_of_items)+'_'+str(no_of_transactions)+'.txt','w')
item_list = list()
for i in range(no_of_items):
	item_list.append([])

for trans in range(0, no_of_transactions):    
    no_of_items_this_transaction = random.randint(1,int(len(items)/3))
    this_trans = list()
    this_trans_verbose=list()
    while(len(this_trans) <= no_of_items_this_transaction):
        rand_item = random.randint(0,len(items)-1)
        if (rand_item not in this_trans):	
            if (me_items_map.__contains__(rand_item)):
                if (me_items_map[rand_item] not in this_trans):
                    this_trans.append(rand_item)
                    this_trans_verbose.append(id_item_map[rand_item])
                    #ADDED
                    item_list[rand_item].append(trans)
                    #print(item_list)

                    #print("1.Transaction No:: "+str(trans)+" added item: "+str(rand_item))
            else:
                this_trans.append(rand_item)
                this_trans_verbose.append(id_item_map[rand_item])
                #ADDED
                item_list[rand_item].append(trans)
                #print(item_list)

                #print("2.Transaction No:: "+str(trans)+" added item: "+str(rand_item))
    this_trans.sort()
    for it in this_trans:
        f1.write(str(it)+'\t')
        f3.write(str(it)+' , ')
    f1.write('\n')
    f3.write('\n')
    this_trans_verbose.sort()
    #print(str(this_trans_verbose))
    for it in this_trans_verbose:
        f2.write(str(it)+'\t')
        f4.write(str(it)+' , ')
    f2.write('\n')
    f4.write('\n')

#ADDED
f5.write(str(no_of_transactions)+'\t'+str(no_of_items)+'\n')
for item in item_list:
	for tID in item:
		f5.write(str(tID)+'\t')
	f5.write('\n')

f1.close()
f2.close()
f3.close()
f4.close()

#ADDED
f5.close()
