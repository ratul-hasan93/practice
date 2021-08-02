# marge sort implementation ascending order

def marge_sort(item_list):

    if len(item_list) > 1:

        # splitting
        mid = len(item_list) // 2
        left = item_list[:mid]
        right = item_list[mid:]

        marge_sort(left)
        marge_sort(right)

        # initialize
        i,j,k = 0,0,0

        # marging
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
               item_list[k] = left[i]
               i+=1
            else:
                item_list[k] = right[j]
                j+=1
            k+=1

        # insert remaining elemennts from left side list
        while i < len(left):
            item_list[k] = left[i]
            i+=1
            k+=1
        
        # insert remaining elemennts from right side list
        while j < len(right):
            item_list[k] = right[j]
            j+=1
            k+=1

if __name__ == '__main__':
    item_list = [4,5,7,3,9,2,8,6,1,10]
    marge_sort(item_list)
    print('Sorted list:', item_list)