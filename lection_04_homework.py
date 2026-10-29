userinput = input()

def charac_checker(word):
    chalist = []
    chisla = '0123456789'
    for char in word:
        if char not in chisla: 
            chalist.append(False)
        else:
            chalist.append(True)
    if all(chalist) == True:
        return(True)
    else:
        return(False)


if userinput == '':
    print('Пустой ввод.')
elif (charac_checker(userinput) == False):
         print('Это не число')
else:
     N = int(userinput)

     

list = [i for i in range(2, N+1)]

for p in list:
    # print(p)
    for j in list:
        if j == p:
            placeholder = p
            #print('бугагага')
            
        elif j % p == 0:
            list.remove(j)

# print(list)
for lmk in list:
    print(lmk)


# Зачеркнуть в списке числа от 2p до n, считая шагами по p (это будут числа, кратные p: 2p, 3p, 4p, ...).
# Найти первое незачёркнутое число в списке, большее чем p, и присвоить значению переменной p это число.
# Повторять шаги 3 и 4, пока возможно.
