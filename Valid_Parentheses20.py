# this is using replace 
def isValid(s):
    while '()' in s or '{}' in s or '[]' in s:
        s=s.replace('()','').replace('{}','').replace('[]','')
    return s==''

s="()[]{}"
print(isValid(s))

#see another one

def isValid(s):
    stack = [] # create an empty stack to store opening brackets
    for c in s: # loop through each character in the string
        if c in '([{': # if the character is an opening bracket
            stack.append(c) # push it onto the stack
        else: # if the character is a closing bracket
            if not stack or \
                (c == ')' and stack[-1] != '(') or \
                (c == '}' and stack[-1] != '{') or \
                (c == ']' and stack[-1] != '['):
                return False # the string is not valid, so return false
            stack.pop() # otherwise, pop the opening bracket from the stack
    return not stack # if the stack is empty, all opening brackets have been matched with their corresponding closing brackets,
                         # so the string is valid, otherwise, there are unmatched opening brackets, so return false
                    
s="()[]{}"
print(isValid(s))



#using manually
def isValid(s):
    p=0
    q=0
    r=0
    
    for c in s:
        if c == '(':
            p+=1
        elif c == ')':
            p-=1
            if p<0:
                return False
            
        if c == '{':
            q+=1
        elif c== '}':
            q-=1
            if q<0:
                return False
        
        if c == '[':
            r+=1
        elif c == ']':
            r-=1
            if r<0:
                return False
            
    return p==0 and q==0 and r==0 


s="()[]{}"
print(isValid(s))