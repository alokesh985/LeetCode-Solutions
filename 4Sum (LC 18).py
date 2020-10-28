""" This program will give all the possible UNIQUE quadruplets of an array that add up 
to a given target.
Using 2 Pointer Technique. """

def fourSum(arr, target):

    subarrays = []
    
    if(len(arr) < 4):
        return subarrays

    arr.sort()

    # 'prev_i' is to take care of duplicates. So that we don't repeat consecutive i
    prev_i = None
    
    # We go till len(arr) - 3 because we need at least 3 elements in front of i
    # to create a sum of 4 elements
    for i in range(len(arr) - 3):
        if(arr[i] == prev_i):
            continue

        prev_i = arr[i]

        prev_j = None

        for j in range(i + 1, len(arr) - 2):
            if(arr[j] == prev_j):
                continue

            prev_j = arr[j]

            # Using 2 pointers technique
            lptr = j + 1
            rptr = len(arr) - 1

            while(lptr < rptr):

                current_sum = arr[i] + arr[j] + arr[lptr] + arr[rptr]

                if(current_sum == target):
                    subarrays.append([arr[i], arr[j], arr[lptr], arr[rptr]])

                    # Eliminating duplicates. We have to make sure consecutive values of lptr and rptr
                    # are NOT same

                    prev_lptr_value = arr[lptr]
                    prev_rptr_value = arr[rptr]

                    while(lptr < rptr and arr[lptr] == prev_lptr_value):
                        lptr += 1

                    while(rptr > lptr and arr[rptr] == prev_rptr_value):
                        rptr -= 1

                elif(current_sum < target):
                    lptr += 1

                else:
                    rptr -= 1

    return subarrays


def main():
    ip = list(map(int, input("Enter the input array: ").split()))
    target = int(input("Enter target: "))

    subarrays = fourSum(ip, target)

    for array in subarrays:
        print(*array)

if __name__ == "__main__":
    main()