num_periodico = 10 / 3
print(num_periodico)
num_str = str(num_periodico) 
len_num = len(num_str)
print(len_num)

que_debolver = ""
num_list =  list()
num_str = str(num_periodico) 
len_num = len(str(num_periodico))
if(len_num > 8):
    for i in num_str:
        num_list.append(i)

while(len(num_list) > 7):
    num_list.pop(-1)

for i in range(0, len(num_list)):
    que_debolver = que_debolver + str(num_list[i])
    if(i == len(num_list) - 1):
        que_debolver = que_debolver + "*"

print(que_debolver)