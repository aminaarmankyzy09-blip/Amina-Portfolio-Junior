import random
asd = random.randint(1,100)

print('Я загадала число от 1 до 100, Попробуй угадать!')

while True:
   chislo = int(input('Введи число:'))

   if chislo < asd:
    print('Ты не угадал, попробуй снова! Подсказка: загаданное число больше :)')
   elif chislo > asd:
       print('Ты не угадал, попробуй снова! Подсказка: загаданное число меньше :)')
   else:
    print("Поздравляю, ты угадал!")
    break

