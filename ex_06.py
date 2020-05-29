a = float(input("Введите результаты пробежки первого дня в км "))
b = float(input("Введите общий желаемый результат в км "))
day = 1
f = str("Ответ: на")
v = str("день спортсмен достиг результат - не менее")
k = str("км.")
if a > b:
    print(f, day, v, b, k)
while a < b:
        a = a + 0.1 * a
        day += 1
print(f, day, v, b, k)