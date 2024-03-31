class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_dict = {}
        result = []
        remianing_value = 0
        for i in range(len(nums)):
            remianing_value = target - nums[i]
            print(remianing_value)
            total = result_dict.get(remianing_value,"empty")
            if total == "empty":
                result_dict[nums[i]] = i
            if total != "empty":
                result.append(result_dict[remianing_value])
                result.append(i)
        return result
