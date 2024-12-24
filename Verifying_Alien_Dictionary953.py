def isAlienSorted(words, order):
    arr=[]
    for i in words:
        arr.append( [order.index(j) for j in i])
    return arr == sorted(arr)

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(isAlienSorted(words, order))