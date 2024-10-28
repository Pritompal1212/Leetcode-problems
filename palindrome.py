def ispalindrome(x):
    convert_string=str(x)
    if convert_string == convert_string[::-1]:      #[::-1] = [start:stop:step]  basically for -1 it reversed a string
        print("its a palindrome")
    else:
        print("not a palindrome")

ispalindrome(10)


#if we dont want to create string and store then
''' 
def isPalindrome(self, x: int) -> bool:
	if x<0:
		return False

	inputNum = x
	newNum = 0
	while x>0:
		newNum = newNum * 10 + x%10
		x = x//10
	return newNum == inputNum

'''
