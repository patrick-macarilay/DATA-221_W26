def distribution_analysis(nums):
    if not nums:
        return {}

    total = len(nums)
    sorted_nums = sorted(nums)
    final_dict = {}
    count = 0

    for num in sorted_nums:
        count += 1
        if num not in final_dict:
            final_dict[num] = f"{count / total * 100:2f}%"

    return final_dict

print(distribution_analysis([3,1,2,3,4,2]))
print(distribution_analysis([]))