class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count={}
        lst=[]
        i=0
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1

        freq = [[] for i in range(len(nums) + 1)]
        
       
        
        for num, c in count.items():
            freq[c].append(num)
            
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                lst.append(num)
                if len(lst) == k:
                    return lst

            
        
        
            
            
        
        
            
        
        
        
        

                
        