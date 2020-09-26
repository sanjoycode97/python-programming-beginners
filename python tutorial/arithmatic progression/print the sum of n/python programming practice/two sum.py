class solution:
    def twosum(self,nums,target):
      num_to_index={}
      for i, num in enumerate(nums):
          if target-num in num_to_index:
              return [num_to_index[target-num],i]
          num_to_index=i
      return []
t1=solution
t1.twosum()
