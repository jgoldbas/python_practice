# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
"""
Coding Question
You can use any language you want -- do your best to think out loud and walk me through your thought process as you
break down this problem.

Mathematically, there is a concept called a happy number.  Every number is either happy or sad.

Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process.
Those numbers for which this process ends in 1 are happy numbers,   while those that do not end in 1 are sad numbers.

7 is a happy number.

7 * 7 = 49

4*4 + 9*9 = 97

9*9 + 7*7 = 130

1*1 + 3*3 + 0*0 = 10

1*1 + 0*0 = 1

4 is a sad number - if you repeat the process with 4, it will never reach 1 and will just go on infinitely.

4*4 = 16

1*1 + 6*6 = 37

3*3 + 7+7 = 56

5*5 + 6*6 = 61

6*6 + 1*1 = 37

etc.

Write a function, is_happy, that takes an integer and returns a boolean indicating whether or not the number is happy or sad.


"""

def is_happy(num):
    #iterate through input num
    past_sums = set()
    while num != 1:
        sum = 0
        while num > 0:
            #isolate rightmost digit
            curr_digit = num % 10

            #take isolated digit and square it
            digit_sqrd = curr_digit * curr_digit
            #get the sum of squares:
            sum += digit_sqrd
            #update the num:
            num = num // 10

        if sum in past_sums:
            return False
        #otherwise add it to past_sums
        past_sums.add(sum)

        num = sum
    return True


if __name__ == '__main__':
    print(is_happy(4)) #should output False

    print(is_happy(7)) #should output True
