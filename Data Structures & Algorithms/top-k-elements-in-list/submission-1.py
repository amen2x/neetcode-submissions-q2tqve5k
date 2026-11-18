class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numCount={}
        finalList=[]

        for num in nums:
            if num in numCount:
                numCount[num]+=1
            else:
                numCount[num]=1

        for i in range(k):

            highest=next(iter(numCount.values()))
            highest_key=next(iter(numCount.keys()))

            for key, value in numCount.items():
                if value> highest:
                    highest= value
                    highest_key= key
            finalList.append(highest_key)
            numCount.pop(highest_key)

        return finalList







                