def parmute(nums):
    def backtrack(st,en):
        if st == en:
            res.append(nums[:])
        for i in range(st , en):
            nums[st],nums[i]=nums[i],nums[st]
            backtrack(st+1,en)
            nums[st],nums[i]=nums[i],nums[st]
            
    res=[]
    backtrack(0,len(nums))
    return res

nums=[1,2,3]
print(parmute(nums))