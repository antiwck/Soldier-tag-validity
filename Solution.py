tag = input()
flag = 0
vowel = ['A', 'E', 'I', 'O', 'U', 'Y']
for i in range(len(tag)-1):
    if(tag[i].isdigit() and tag[i+1].isdigit()):
        if((int(tag[i])+int(tag[i+1]))%2==0):
            flag = 0
        else:
            flag = 1
            break
    if tag[i].isalnum():
        if tag[i] in vowel:
            flag = 1
            break
if(tag[6] != '-'):
    flag = 1
if flag:
    print("invalid")
else:
    print("valid")
