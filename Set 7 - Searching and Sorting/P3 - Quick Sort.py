import listmaker

print('Quick Sort')
partition_count = 0

def quicksort(nums, left, right):
    if left >= right:    
        return
    pivot = nums[(int((left + right) / 2))] 
    index = partition(nums, left, right, pivot)
    quicksort(nums, left, index - 1)
    quicksort(nums, index, right)
    
    
    
def partition(nums, left, right, pivot):
    while left <= right: # left needs to overtake right
        while nums[left] < pivot: # finding a value on the left that is greater than the pivot
            left += 1
    
        while nums[right] > pivot: # find a value of the right that is less than the pivot
            right -= 1

        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1 
    return left
        
list1 = [70, 58, 63, 76, 77, 74, 8, 12, 1, 78, 67, 50, 78, 47, 25, 44, 8, 76, 33, 56]
quicksort([70, 58, 63, 76, 77, 74, 8, 12, 1, 78, 67, 50, 78, 47, 25, 44, 8, 76, 33, 56], 0, len(list1) - 1)

