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
    value=abs(value)
    formula = "{0} + {0}{0} + {0}{0}{0}".format(value)
    return out.format(eval(formula))

    # Альтернативный вариант решения
    parts=list()
    parts.append(int("{0}".format(value)))
    parts.append(int("{0}{0}".format(value)))
    parts.append(int("{0}{0}{0}".format(value)))
    value=0
    for part in parts:
        value+=part
    return out.format(value)

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

company = dict()
def ForTask5(value,out):
    global company
    try:        
        value = float(value)    
    except:
        raise Exception("StrIsNotNumeric")    

    if not "proceeds" in company:
        company["proceeds"]=value
        return None
    elif not "costs" in company:
        company["costs"]=value
        company["profit"]=company["proceeds"]-company["costs"]
        if company["profit"]>=0:
            company["result"]="прибыль: {0}"
            company["profitability"]="рентабельность: {0:2f}".format(company["profit"]/company["proceeds"])
        else:
            company["result"]="убыток: {0}"
            company["profitability"]=None
            # Чтобы не выводить расчет на одного сотрудника
            #company.pop("proceeds", "None")
            #company.pop("costs", "None")
        out=out.format(company["result"].format(company["profit"]),company["profitability"])
    elif not "workers" in company:
        company["workers"]=value
        if company["profit"]<=0:
            out=out.format(0)
        else:
            out=out.format(company["profit"]/company["workers"])

        company.pop("proceeds", "None")
        company.pop("workers", "None")
        company.pop("costs", "None")
    
    return out

def ForTask6(value,out):
    try:           
        v = value.replace(" ","")
        parts = v.split(",")
        a = float(parts[0].split("=")[1])
        b = float(parts[1].split("=")[1])
    except:
        raise Exception("StrFormatIsNotValid")

    i = 1
    print("{0}-й день: {1:.2f}".format(i,a))
    while True:
        i+=1
        a*=1.1
        print("{0}-й день: {1:.2f}".format(i,a))
        if b<=a:
            break
    return out.format(i,b)


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
            elif e.args[0]=="StrIsNotNumeric":
                i-=1
                print("Некорректное значение, ожидается число, пожалуйста повторите ввод!")
            elif e.args[0]=="StrFormatIsNotValid":
                i-=1
                print("Некорректный формат, пожалуйста смотрите пример и повторите ввод!")                
            continue
        finally:
            i+=1

# Конфигурируем программу добавляя задачи в список
# В каждой задаче настраиваем ввод, вывод, исполняющую функцию и тип ожидаемых данных от пользователя
# Последовательноть выволнения задач будет в соответствии со списком tasks 
# Если необходимо, то список можно сортировать, так как номера задач весьма условны
# Сортировка внутри кортежа (одной задачи), недопустима!

tasks = list()
tasks.append((  {"in":"Введите целое число: ", "def":ForTask1, "type":int}, 
                {"in":"Введите дробное число: ", "def":ForTask1, "type":float},
                {"in":"Введите строку: ", "def":ForTask1, "type":str},
                {"in":"Введите ещё строку: ", "out":" Вы ввели: {0}, {1}, {2}, {3}", "def":ForTask1, "type":str}))

tasks.append(({"in":"Введите время в секундах: ", "out":"Результат в формате времени чч:мм:сс = {0}:{1}:{2}", "def":ForTask2, "type":int}))
tasks.append(({"in":"Введите число n для формулы n + nn + nnn: ", "out":"Результат = {0}", "def":ForTask3, "type":int}))
tasks.append(({"in":"Введите целое положительное число из нескольких цифр: ", "out":"Самая большая цифра в числе = {0}", "def":ForTask4, "type":int}))
tasks.append(({"in":"Введите значения выручки фирмы: ", "def":ForTask5},
            {"in":"Введите значение издержек фирмы: ", "out":"Финансовый результат фирмы = {0}", "def":ForTask5},
            {"in":"Введите численность сотрудников фирмы: ", "out":"Прибыль фирмы в расчете на одного сотрудника = {0:2f}", "def":ForTask5, "type":int}))

tasks.append(({"in":"Введите строку, например: a = 2, b = 3: ", "out":"Ответ: на {0}-й день спортсмен достиг результата — не менее {1} км.", "def":ForTask6, "type":str}))       

# Основной цикл
while True:
    one = 'one'
    two = 'two'
    three = 'three'

    print(three)
    print(two)
    print(one)

    # Основная функция
    main(tasks)
    if 'y' != input("Введите 'y', чтобы повторить, а для выхода нажмите Enter: "):
        break

print("Завершение программы")
