

dict = dict()
n = int(input("input N: "))
for i in range(0,n):
    strs = input("input country and cities: ").split()
    for j in range(1,len(strs)):
        dict[strs[j]] = strs[0]
print(dict)
m = int(input("input M: "))
for i in range(0,m):
    city = input("input your city: ")
    print(dict[city])