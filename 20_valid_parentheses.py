''' 
VALID PARENTHESES 

PROBLEM:
Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same
type.
 

 Example 1:

 Input: s = "()"
 Output: true
 Example 2:

 Input: s = "()[]{}"
 Output: true
 Example 3:

 Input: s = "(]"
 Output: false


'''

'''
SOLUTION:
    
    Use a stack.
    Add opening parenthees to stack.
    If closing, compare to top of stack.
    Stack methods:
        .append(s)
        .pop(s)

'''

def valid_par(s):

    stk = []        #stack
    for s in str:
        if s == '(' or s == '[' or s == '{':
            stk.append(s)
        else:
            print("stk[-1]: ", stk[-1])
            if not stk or \                             #only pushed closing brackets, no stack elements
               stk[-1] == '(' and s != ')' or  \
               stk[-1] == '[' and s != ']' or \
               stk[-1] == '{' and s != '}':
                return False            #if top of stack not equal to close parentheses
            stk.pop()
    return len(stk) == 0        #check if empty, if not, x opening brackets did not have closing


str = "()[]{}"
val = valid_par(str)
print(str)
print("valid: ", val)

















