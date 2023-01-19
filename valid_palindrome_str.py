#This is problem 125 on Leetcode.com
#https://leetcode.com/problems/valid-palindrome/description/

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    # remove all non-alphanumerical characters
    clean_s = ""
    # iterate through input string
    for i in s:
        if (i.isalnum()):
            clean_s += i
    # print(clean_s)

    # Convert clean_s to all lowercase, update clean_s:
    clean_s = clean_s.lower()

    # single line cleaning:
    # another_clean_s= "".join(char.lower() for char in s if ch.isalnum())

    # Not recursive because we don't want to clean every time the function is called
    while (len(clean_s) > 1):
        if (clean_s[0] == clean_s[-1]):
            clean_s = clean_s[1:-1]
        # print(clean_s)
        # if clean_s== "":
        #    print("Empty value")
        else:
            return False
    # After the while loop ends, that means we've checked all elements and they are a palindrome
    return True

if __name__ == '__main__':
    input_string = "A man, a plan, a canal: Panama"

    print(isPalindrome(input_string)) #should return True

    input_string2 = "This is definitely not a palindrome."
    print(isPalindrome(input_string2)) #should return False

