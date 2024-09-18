def remove_duplicates(nums):
    seen = set()
    k = 0

    for num in nums:
        if num not in seen:
            seen.add(num)
            i = nums.index(num)
            nums[k],nums[i] = num,nums[k]
            k += 1
    
    return k
nums = [1, 2, 3, 1, 2, 4, 5]
print(f"Entrada: {nums}")
k = remove_duplicates(nums)
print(f"Valores unicos: {k}") 
print(f"Primeros {k} valores {nums[:k]} , Salida completa: {nums}")  


