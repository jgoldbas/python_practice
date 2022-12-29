def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    Hash = []
    i = 0
    while (i < len(nums)):
        if (nums[i] in Hash):
            return True
        else:
            Hash.append(nums[i])
        i += 1
    return False

if __name__ == '__main__':
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    answer = containsDuplicate(nums2)
    print(answer)