def reachNumber(target):
    ans, k = 0, 0
    target = abs(target)
    while ans < target:
        ans += k
        k += 1
    while (ans - target) % 2:
        ans += k
        k += 1
    return k - 1

target = 2
print(reachNumber(target))