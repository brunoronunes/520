numeros = [1,5,2,6,8,9,1002,3041,762]
par = []

# for num in numeros:
#     if num % 2 == 0:
#         par.append(num)
# print(par)

par = [x for x in numeros if x % 2 == 0]
print(par)