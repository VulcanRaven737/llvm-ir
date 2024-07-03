file1 = open("x.sexp","r")
file_content = file1.read()
print(file_content)
list1 = file_content.split()
list2 = []
for i in range (len(list1)):
    if ')' in list1[i] or '(' in list1[i]:
        for j in range (len(list1[i])):
            list2.append(list1[i][j])
    else:
        list2.append(list1[i])
print(list2)

'''
list4 = []
for k in range(len(list2)):
    if file_content[k] == ('('):
        continue
    elif file_content[k] == (')'):
        continue
    else:
        list4.append(list2[k])
print(list4)
'''

def parse(string_list):
    val = string_list.pop(0)
    if val == '(':
        new_list = []
        while string_list[0] != ')':
                new_list.append(parse(string_list))
        return new_list          
    else:
         return str(val)
    
list4 = parse(list2)
print(list4)

