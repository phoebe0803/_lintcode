import copy
def subsets(nums):
    #nums  is a non-decent
    lists=[]
    result=[]
    position=0

    result=subsets_helper(result,lists,nums,position)
    return result



def subsets_helper(result,lists,nums,position):
    length=len(nums)
    result.append(lists)
    # sub=[]
    for i in range(position,length):
        print(i)
        lists.append(nums[i])
        a=lists()
        j=i
        j=j+1
        subsets_helper(result,a,nums,j)
        a.pop()







if __name__ == '__main__':
    nums=[1,2,3]
    print(subsets(nums))

