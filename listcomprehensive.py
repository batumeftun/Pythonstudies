number = [1,2,3,4,5,6,7,8,9]
list2= []
for number in numbers:
  list2.append(number) #append: listeleri birleştiriyor
print(list2)

#comprehensive liste
list3=[number for number in numbers]

X = int(raw_input())
Y = int(raw_input())
Z = int(raw_input())
N = int(raw_input())

ans = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print ans
