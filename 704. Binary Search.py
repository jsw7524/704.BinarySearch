class Solution(object):
    def search(self, nums, target):
        self.nums=nums
        return self.BinarySearch(0,len(nums)-1,target)

    def BinarySearch(self,l,r,target):
        mid = (l+r)//2
        if self.nums[mid] == target:
            return mid
        elif l >= r :
            return -1
        else:
            if self.nums[mid] <= target:
                return self.BinarySearch(mid + 1, r, target)
            else:
                return self.BinarySearch(l,mid-1,target)

sln = Solution()
print(sln.search([-1,0,3,5,9,12],-999))
