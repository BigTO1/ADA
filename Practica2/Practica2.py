def mediana(nums):
    n = len(nums)/2

    if(n.is_integer()):
        num1 = nums[len(nums)//2]
        num2 = nums[(len(nums)//2)-1]
        mediana = (num1+num2)/2
        
    else:
        n = len(nums)//2
        mediana = nums[n]
    return mediana

nums1 = [34, -56, 78, 12, -3, 45, 67, 89, -90, 23,9]
nums2 = [-105, 23, 45, -34, 87, 56, 102, -76, 39]

merged = list(nums1 + nums2)
merged.sort()

mediana = mediana(merged)

print(f"La mediana del conjunto de números es: {mediana}")