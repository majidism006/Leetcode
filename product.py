def productExceptSelf(nums: list[int]) -> list[int]:
    res = []
    for num in nums:
        product = 1
        new_list = nums.copy()
        new_list.remove(num)
        for remaining_num in new_list:
            product = product * remaining_num
        res.append(product)
            
    return res


print(productExceptSelf([1,2,3,4]))