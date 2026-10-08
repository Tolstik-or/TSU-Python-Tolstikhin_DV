# 0-99
# only numbers
# text

UserInput = str(input('Введите число от 0 до 99: ')) # ввод текста как строчки

# функция защиты от дурака

def charac_checker(word):
    chalist = [] # заводит список совпадений
    numbers = '0123456789'  # это цифры
    for char in word:  # прогоняет по каждому символу в введенной строке
        if char not in numbers: # если символ не из цифр -
            chalist.append(False)  # добавляет Ложь в список
        else:
            chalist.append(True)  # если смимвол цифра то Правду
    if all(chalist) == True:  # проверка что все символы были цифрами и лжи не было ни разу
        return(True)
    else:
        return(False)



if UserInput == '':  # пустой ввод
    print('Если вы ничего не введёте, вы ничего не получите.')

elif len(UserInput) > 2:  # ввод 3+ символа
     print('Один или два символа, пожалуйста.')

elif (charac_checker(UserInput) == False):  # ввод не цифр
    print('Мне кажется, это не только цифры.')


if len(UserInput) == 1:  # числа 0-9
    if UserInput == '1':
        Output = 'Один'
    elif UserInput == '2':
        Output = 'Два'
    elif UserInput == '3':
        Output = 'Три'
    elif UserInput == '4':
        Output = 'Четыре'
    elif UserInput == '5':
        Output = 'Пять'
    elif UserInput == '6':
        Output = 'Шесть'
    elif UserInput == '7':
        Output = 'Семь'
    elif UserInput == '8':
        Output = 'Восемь'
    elif UserInput == '9':
        Output = 'Девять'
    elif UserInput == '0':
        Output = 'Ноль'
    
    print(Output)

# Числа 10-19
elif (len(UserInput) == 2) and (int(UserInput[0]) == 1):    
    if UserInput[1] == '1':
        Output = 'Одиннадцать'
    elif UserInput[1] == '2':
        Output = 'Двенадцать'
    elif UserInput[1] == '3':
        Output = 'Тринадцать'
    elif UserInput[1] == '4':
        Output = 'Четырнадцать'
    elif UserInput[1] == '5':
        Output = 'Пятнадцать'
    elif UserInput[1] == '6':
        Output = 'Шестнадцать'
    elif UserInput[1] == '7':
        Output = 'Семнадцать'
    elif UserInput[1] == '8':
        Output = 'Восемнадцать'
    elif UserInput[1] == '9':
        Output = 'Девятнадцать'
    elif UserInput[1] == '0':
        Output = 'Десять'
    
    print(Output)
    

## Числа 20-99
elif ((len(UserInput) == 2) and (int(UserInput[0]) > 1)):    
    No_1 = int(UserInput[0])
    No_2 = int(UserInput[1])
    
    if No_1 == 2:
        decimal = ('Двадцать')
    elif No_1 == 3:
        decimal = ('Тридцать')
    elif No_1 == 4:
        decimal = ('Сорок')
    elif No_1 == 5:
        decimal = ('Пятьдесят')
    elif No_1 == 6:
        decimal = ('Шестьдесят')
    elif No_1 == 7:
        decimal = ('Семьдесят')
    elif No_1 == 8:
        decimal = ('Восемьдесят')
    elif No_1 == 9:
        decimal = ('Девяносто')

    if No_2 == 1:
        singular = ('один')
    elif No_2 == 2:
        singular = ('два')
    elif No_2 == 3:
        singular = ('три')
    elif No_2 == 4:
        singular = ('четыре')
    elif No_2 == 5:
        singular = ('пять')
    elif No_2 == 6:
        singular = ('шесть')
    elif No_2 == 7:
        singular = ('семь')
    elif No_2 == 8:
        singular = ('восемь')
    elif No_2 == 9:
        singular = ('девять')
    elif No_2 == 0:
        singular = ('')

    print(decimal, singular)


# "{first} {second}".format(second="World", first="Hello")

# a = "{1} {0} {1} {1}"
# a.format("world", "hello")