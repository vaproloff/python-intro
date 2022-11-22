# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

false_count = 0
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not (x or y or z)) != ((not x) and (not y) and (not z)):
                false_count += 1

if false_count == 0:
    print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z верно для всех значений предикат')