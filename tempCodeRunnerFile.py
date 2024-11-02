if len(nums1) < len(nums2):
        nums2.extend(nums1)
        nums2.sort()
        mid1=(nums2[0]+nums2[-1])/2
        return mid2
    else:
        nums1.extend(nums2)
        nums1.sort()
        mid2=(nums1[0]+nums1[-1])/2
        return mid2  