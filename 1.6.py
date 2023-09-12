text = input("Введите текст: ")
text_list = []
for i in text:
    if i.isalpha():
        text_list.append(i)
    else:
        continue
print("Полученный список: ", text_list)
kortezh = tuple(text_list)
print("Кортеж: ", kortezh)
