def superPow(a, b):
    c="".join(map(str,b))  
    d=int(c)
    return pow(a,d,1337)

a = 2
b = [3]

a = 2
b = [1,0]

a = 1
b = [4,3,3,8,5,2]

print(superPow(a, b))