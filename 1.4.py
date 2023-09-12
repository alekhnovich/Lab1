print("Строка: Never look back")
stroka = " Never look back"
dictionary = {}
for i in stroka:
    if i not in dictionary:
        dictionary[i] = stroka.count(i)
print("Полученный словарь: ", dictionary)
