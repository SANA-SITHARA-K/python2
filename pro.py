nums=[1,2,5]
target=7
def sol(nums,target):
    dictionary={}
    solutions=[]
    for i in range(len(nums)):
        dictionary[nums[i]]=i
    for i in range(len(nums)):
        currentnumber=nums[i]
        remaining=target-currentnumber
        if remaining in dictionary:
            solutions.append((i,dictionary[remaining]))
    return solutions
print(sol(nums,target))
#end=time.perf_counter()
#print(end-start)