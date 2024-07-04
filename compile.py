import json 
file1 = open("first.kal.json")
data = json.load(file1)
data[0] = 'brilisp'

list1=[]
for i in data:
    list1.append(i)

for i in range(len(list1[1])):
    if list1[1][i] == 'define':
        for j in range(len(list1[1][i+1])):
            list2=[]
            list2.append(list1[1][i+1][j])
            list2.append('int')
            print(list2)
            list1[1].insert(i+j+2,list2)      
        list1[1][i+1].clear()
    else:
        pass
print(list1)            
file2 = open("out_first.kal.json","w")
json.dump(list1,file2)
file1.close()
file2.close()
