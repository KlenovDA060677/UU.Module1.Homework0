#Практическое задание по уроку "Базовые структуры данных"

a = "Я изучаю Python."

print (a) #выводим значение переменной 'a'
print (len(a)) #выводим длину строки в переменной 'a'


first = 3
second = 5
third = 9

sum = first + second #сумма переменной first и second
diff = first - second #разность переменной first и second
mean = (first + second + third)/3 #средне арифмет. перемен. first, second и third

print (sum)
print (diff)
print(mean)

first_string = 'понедельник'
second_string = 'вторник'
week_days = first_string + ", " + second_string

print (week_days) #вывод переменных first_string и second_string через , с пробелом

a = 3
b = 5
c = 7
f = (((a + b) * (a + c))**3) / 2 #вычисление заданного выражения

print(f) #вывод рез-та вычисления заданного выражения