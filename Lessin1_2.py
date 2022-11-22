# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат


for x in range(False, True):
    for y in range(False, True):
        for z in range(False, True):
            if (not (x or y or z)) == (not x and not y and not z):
                print('Утверждение истино')
            else:
                print('Утверждение ложно')
