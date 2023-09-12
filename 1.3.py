my_list = []
new_list = []
n = int(input("Введите количество элементов в списке: "))
for i in range(n):
    new_el = int(input())
    my_list.append(new_el)
print(my_list)
j = 0
for j in my_list:
    if my_list.count(j) > 2:
        continue
    else:
        new_list.append(j)
print("Полученный список: ", new_list)
new_list.sort()
new_list.reverse()
print("Отсортированный по убыванию список: ", new_list)
