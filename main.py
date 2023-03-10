import random
arr = [10,4,9,7,11,1,0,5,8,3]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        less = []
        greater = []
        for element in arr[:-1]:
            if element < pivot:
                less.append(element)
            else:
                greater.append(element)
        print(f"pivot = {pivot}, менші = {less}, більші = {greater}")
        return quicksort(less) + [pivot] + quicksort(greater)

def quicksort_random(arr):
    l = len(arr)
    if l <= 1:
        return arr
    else:
        # Вибір опорного елементу рандомним шляхом
        pivot_index = random.randint(0, l - 1)
        pivot = arr[pivot_index]

        # Розбиття на підмасиви
        less = [elem for elem in arr[:pivot_index] + arr[pivot_index + 1:] if elem < pivot]
        greater = [elem for elem in arr[:pivot_index] + arr[pivot_index + 1:] if elem >= pivot]
        #print(f"pivot = {pivot}, менші = {less}, більші = {greater}")
        return quicksort_random(less) + [pivot] + quicksort_random(greater)
if __name__ == '__main__':
    print(arr)
    print(quicksort(arr))
    print("З рандомним вибором опорного елементу")
    print(arr)
    print(quicksort_random(arr))
