class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        this_dict={}
        for i in nums:
            if i in this_dict:
                return True
            this_dict[i]=i
        return False
            

        