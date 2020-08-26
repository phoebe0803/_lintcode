def binarySearch(nums, target):
        # write your code here
        start=0
        end=len(nums)-1
        while start+1 < end:
            mid = int(start+(end-start)/2)
            if nums[mid] >=target:
                end = mid
            if nums[mid] < target:
                start = mid

        if start+1 == end:
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            else:
                return  -1


if __name__ == '__main__':
    nums=[1,4,4,5,7,7,8,9,9,10]
    target=0
    position=binarySearch(nums,target)
    print(position)


