# int = int(input('Son: '))

# for i in range(1,int):
#     if int % i == 0:
#         print(i)

# son_1 = int(input('Son: '))
# son_2 = int(input('Son: '))
# count_1 = 0
# count_2 = 0

# for i in range(son_1+1, son_2):
#     if i % 2 == 0:
#         count_1 +=1
#         print(i)
#     else:
#         count_2 +=1
#         print(i)

# print(count_1, "Juft")
# print(count_2,"Toq")

# list_1 = [12,24,25,31,33]
# list_2 = [12,25,32,34,33]

# for i in list_1:
#     if i in list_2:
#         print(i)

# l = [1,2,3,3]
# count = 0
# for i in l:
#    int = l.count(i)
#    if int >= 2:
#     count +=1


# print(count >= 2)

min_max = (4, 1, 8, 7)

print(min(min_max),max(min_max))

sort = (5, 3, 1, 4) 

sorted = sorted(sort)
print(tuple(sorted))

for x in range(len(sorted)-1,-1,-1):
    print(sorted[x])

juft = 0
toq = 0

for z in sorted:
    if z % 2==0:
        juft +=z
    else:
        toq +=z

print(f"Juft: {juft} - Toq: {toq}")





  











