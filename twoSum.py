    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        compl_dict = {}
        for i in range(len(nums)):
            if nums[i] in compl_dict:
                return [compl_dict[nums[i]], i]
            else:
                compl_dict[target - nums[i]] = i
        return [-1, -1]