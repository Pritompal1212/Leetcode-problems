def addStrings(num1, num2):
    i=len(num1)-1
    j=len(num2)-1
    carr=0
    rsl=""
    while i>=0 or j>=0 or carr:
        d1 = int(num1[i]) if i>= 0 else 0
        d2 = int(num2[j]) if j>= 0 else 0
        
        total = d1 + d2 + carr
        rsl=str(total % 10)+rsl
        carr = total // 10
        
        i-=1
        j-=1
    return rsl

num1 = "456"
num2 = "77"
print(addStrings(num1, num2))