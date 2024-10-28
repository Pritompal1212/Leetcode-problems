def ispalindrome(x):
    convert_string=str(x)
    if convert_string == convert_string[::-1]:      #[::-1] = [start:stop:step]  basically for -1 it reversed a string
        print("its a palindrome")
    else:
        print("not a palindrome")

ispalindrome(10)
        