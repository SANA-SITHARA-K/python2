nums=[1,2,3,2]
def solutions(nums):
    counter={}
    for i in nums:
        if i in counter:
            return True
        else:
            counter[i]=1
    return False

print(solutions(nums))