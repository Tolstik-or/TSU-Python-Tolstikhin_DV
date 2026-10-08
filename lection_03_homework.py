# C to F <>
# check for correct input

UserInput = str(input())
if UserInput == '':
    print('Пустой ввод.')

else:
    Grade = UserInput[-1]
    Degrees = UserInput [:-1]


    def degree_checker(word):
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
    
    def grade_checker(word):
        chalist = [] # заводит список совпадений
        grades = 'cfCF'  # это шкалы
        for char in word:  # прогоняет по каждому символу в введенной строке
            if char not in grades: # если символ не из цифр -
                chalist.append(False)  # добавляет Ложь в список
            else:
                chalist.append(True)  # если смимвол цифра то Правду
        if all(chalist) == True:  # проверка что все символы были цифрами и лжи не было ни разу
            return(True)
        else:
            return(False)
    
    
    
    
    if (degree_checker(Degrees) and grade_checker(Grade)) == True:
        Degrees = int(Degrees)
        if (('F' in Grade) or ('f' in Grade)):
            # °F − 32) × 5/9
            print(Degrees, 'градусов Фаренгейта это', ((Degrees - 32) / 1.8 ), 'Цельсия')
        else:
              # °F = (°C × 1,8) + 32
              print(Degrees, 'градусов Цельсия это', ((Degrees * 1.8) + 32), 'Фаренгейта')
    
        
    else:
        print('В вашем вводе что-то не так')