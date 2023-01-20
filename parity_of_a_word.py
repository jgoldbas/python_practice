"""
Elements of Programming in Python
4.1 Computing the Parity of a word
The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise is it 0.
For example, the parity of 1011 is 1, and the parity of 10001000 is 0.
"""
# Brute force solution:
def parity(x):
    # print(str("res: "))
    # res = ''.join(format(ord(i), '08b') for i in str(x))
    # print(res)

    result = 0
    while x:
        result = result ^ (x & 1)   # same as "result ^= x & 1"
        x >>= 1
    #    print(''.join(format(ord(i), '08b') for i in str(x)))
    return result

# Time complexity is O(n), where n is the word size

def parity1(n):
    parity = False
    while n:
        # if the rightmost value is 1, then parity = 1 (odd)
        if n & 1 == 1:
            parity = not parity # same as XOR operation
        n = n >> 1              # shift n to be the next digit
    return parity


if __name__ == '__main__':
    print(parity(0b10101)) # must pass 0b in before the number

    print("-----")
    print(parity(0b1))

