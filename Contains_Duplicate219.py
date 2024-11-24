
#def containsNearbyDuplicate(self, nums, k):
    # for i in range(len(nums)):
    #     for j in range(i + 1, min(i+k+1,len(nums))):
    #         if nums[i]==nums[j]:
    #             return True
    # return False

# here i i an gatting time limit Exceeded so see new method  


def containsNearbyDuplicate(nums, k):
    # Create a set to store elements within the range of k
    window = set()
    
    for i in range(len(nums)):
        # If the current element is already in the set, return True
        if nums[i] in window:
            return True
        
        # Add the current element to the set
        window.add(nums[i])
        
        # Ensure the window size does not exceed k
        if len(window) > k:
            window.remove(nums[i - k])
    
    return False

nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums, k))