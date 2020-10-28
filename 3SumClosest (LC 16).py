def closestSum(arr, target):
    arr.sort()

    best_sum = arr[0] + arr[1] + arr[len(arr) - 1]
    best_difference = abs(target - best_sum)

    for i in range(len(arr) - 2):
        ptr1, ptr2 = i + 1, len(arr) - 1

        while(ptr1 < ptr2):
            current_sum = arr[ptr1] + arr[ptr2] + arr[i]

            current_difference = abs(target - current_sum)

            if(current_sum > target):
                ptr2 -= 1
            else:
                ptr1 += 1

            if(current_difference < best_difference):
                best_sum = current_sum
                best_difference = current_difference

    return best_sum

if __name__ == "__main__":
    arr = list(map(int, input("Enter the array: ").split()))
    target = int(input("Enter target: "))

    print(closestSum(arr, target))