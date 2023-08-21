"""
HackerRank problem: Lonely Integer
- Given an array of integers, where all elements except one element occur twice, find the unique element.
EX. input: a = [1,2,3,4,3,2,1]
    output: 4
"""
def lonelyinteger(a):
    for num in a:
        if a.count(num) == 1:
            return num

if __name__ == '__main__':
    result = lonelyinteger([1,1,2,2,4])
    print(result)