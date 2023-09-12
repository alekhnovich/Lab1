vowels = 0
consonants = 0
words = 1
vowelsInText = []
allVowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
count = 0
text = input("Введите текст: ")
for i in text:
    if i.isalpha():
        if i in allVowels:
            vowels += 1
            vowelsInText.append(i)
        else:
            consonants += 1
    if i.isspace():
        words += 1
count += 1
print('Кол-во гласных:', vowels)
print('Кол-во согласных:', consonants)
if vowels == consonants:
    print("Все гласные в тексте: ", vowelsInText)
print("Кол-во слов в тексте: ", words)
