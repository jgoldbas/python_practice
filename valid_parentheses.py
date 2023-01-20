#This is problem 20 on Leetcode.com
#https://leetcode.com/problems/valid-parentheses/description/

def isValid(s):
    # initialize the empty stack, list treated as a stack
    myList = []
    # loop through each char in string
    for i in s:
        # print("current element:" + i)
        # check if i is an opening bracket, '(', '{', or '['
        if (i == '(' or i == '{' or i == '['):
            # if yes, append it to the stack
            myList.append(i)
        else:  # you have a closing bracket
            # if not, we pop the topmost element & check to see if it matches with  the current closing parentheses stored in i.
            if (len(myList) != 0):
                topmost = myList.pop()
                if i == ']':
                    if topmost != "[":
                        return False
                elif i == '}':
                    if topmost != "{":
                        return False
                elif i == ')':
                    if topmost != "(":
                        return False
                else:
                    print("wrong character")
            else:  # otherwise, there is no opening bracket for this # closing bracket
                return False
    #print("MY stack:")
    #print(myList)
    return len(myList) == 0
# ------------------------------------------------------
if __name__ == '__main__':

    input_string = "({)"
    print(isValid(input_string))