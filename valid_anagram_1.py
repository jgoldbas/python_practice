# This is problem 242 on Leetcode.com
# https://leetcode.com/problems/valid-anagram/description/

def isAnagram(s: str, t):
    # check for same length of the two strings, if lengths are different then they're automatically not anagrams
    if (len(s) != len(t)):
        return False

    # check for same letter count
    # need 2 dictionaries
    dict_s, dict_t = {}, {}

    for el in s:
        # print("ele:"+ el)
        dict_s[el] = dict_s.get(el, 0) + 1
        # print(dict_s)
    for el in t:
        dict_t[el] = dict_t.get(el, 0) + 1
    # s=    [a, b, c, d, e]
    # in_s= [0, 1, 2, 3, 4]

    """
    for i in range(len(s)):
        el = s[i]
        el2 = t[i]
        dict_s[el] = dict_s.get(el, 0) + 1
        dict_t[el2]= dict_t.get(el2, 0) + 1
   """

    # compare that the 2 dictionaries are the same
    return dict_t == dict_s

if __name__ == '__main__':
    input_string = "anagram"
    input_string2 = "nagaram"
    print(isAnagram(input_string, input_string2))

    input_string3 = "apple"
    input_string4 = "banana"
    print(isAnagram(input_string3, input_string4))