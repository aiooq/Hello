'''
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.'''

m_var_1 = None
m_var_2 = None
m_var_3 = None
m_var_4 = None
def ForTask1(value,out):
    global m_var_1
    global m_var_2
    global m_var_3
    global m_var_4

    if not m_var_3 is None:
        m_var_4 = value
        out=out.format(m_var_1,m_var_2,m_var_3,m_var_4)
        m_var_1 = None
        m_var_2 = None
        m_var_3 = None
        return out

    if not m_var_2 is None:
        m_var_3 = value
        return None        

    if not m_var_1 is None:
        m_var_2 = value
        return None

    m_var_1 = value
    return None

def ForTask2(value,out):
    def GetCorrect(value):
        if value<10:
            value=str('0'+str(value))
        else:
            value=str(value)
        return value

    h=GetCorrect(value//3600)
    m=GetCorrect((value//60)%60)
    s=GetCorrect(value%60)
    return out.format(h,m,s)

def ForTask3(value,out):
    formula = "{0} + {0}{0} + {0}{0}{0}".format(abs(value))
    return out.format(eval(formula))

def ForTask4(value,out):
    if value<0:
        raise Exception("PositiveNumber")
    elif value==0:
        return out.format(0)

    value=str(value)
    i=0
    value_max=0
    while len(value)>i:
        if value_max<=int(value[i]):
            value_max=int(value[i])
        i+=1
    return out.format(value_max)

tasks = list()
tasks.append((  {"in":"Введите целое число: ", "def":ForTask1, "type":int}, 
                {"in":"Введите дробное число: ", "def":ForTask1, "type":float},
                {"in":"Введите строку: ", "def":ForTask1, "type":str},
                {"in":"Введите ещё строку: ", "out":" Вы ввели: {0}, {1}, {2}, {3}", "def":ForTask1, "type":str}))

tasks.append(({"in":"Введите время в секундах: ", "out":"Результат в формате времени чч:мм:сс = {0}:{1}:{2}", "def":ForTask2, "type":int}))
tasks.append(({"in":"Введите число n для формулы n + nn + nnn: ", "out":"Результат = {0}", "def":ForTask3, "type":int}))
tasks.append(({"in":"Введите целое положительное число: ", "out":"Самую большая цифра в числе = {0}", "def":ForTask4, "type":int}))


def main(tuple):
    i=0
    while len(tuple)>i:
        if not isinstance(tuple[i], dict):
            main(tuple[i])
            i+=1
            continue

        if not "in" in tuple[i]:
            i+=1
            continue
        
        out = None
        if "out" in tuple[i]:
            out = tuple[i]["out"]

        value = input(tuple[i]["in"])

        if "type" in tuple[i]:
            try:
                if tuple[i]["type"] == str and value.isdigit():
                    raise Exception()
                elif tuple[i]["type"] == float and value.isdecimal():
                    raise Exception()
                else:
                    value=tuple[i]["type"](value)
            except:
                print("Некорректное значение, ожидается {0}, пожалуйста повторите ввод!".format(tuple[i]["type"]))
                continue

        try:
            value = tuple[i]["def"](value,out)
            if value != None:
                print(value)
        except Exception as e:
            
            if e.args[0]=="PositiveNumber":
                i-=1
                print("Некорректное значение, ожидается положительное число, пожалуйста повторите ввод!")
            continue
        finally:
            i+=1

while True:
    one = 'one'
    two = 'two'
    three = 'three'

    print(three)
    print(two)
    print(one)

    main(tasks)
    if 'y' != input("Введите 'y', чтобы повторить, а для выхода нажмите Enter: "):
        break

print("Завершение программы")
