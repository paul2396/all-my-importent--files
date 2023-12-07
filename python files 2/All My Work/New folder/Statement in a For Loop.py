for i in range(1, 20):
    print('Multiplication table of', i)
    for j in range(1, 20):
        if i > 5 and j > 5:
            break
        print(i * j, end=' ')
    print('')
#!===========================================
for letters in "authorization":
    if letters == "O":
        continue
    print(letters)
print("The End")
#!==========================================