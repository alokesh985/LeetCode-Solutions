""" Gives the minimum substring in input string where all letters of the target string are present
Using Sliding Window with 2 pointers """

def minSub(string, target):

    # Create a HashMap (dictionary) that will hold the occurrences of the target string
    hashMap = {}
    for letter in target:
        if(letter not in hashMap):
            hashMap[letter] = 1
        else:
            hashMap[letter] += 1

    # Both the pointers will begin from the starting of the string
    lptr, rptr = 0, 0
    # The 'count' variable will hold the number of letters remaining to search in the string
    count = len(target)
    # 'minLen' will hold the size of the minimum window and the 'minSub' will hold the actual window (substring)
    minLen = float('inf')
    minSub = ""

    while(rptr < len(string)):
        
        if(string[rptr] in hashMap):
            hashMap[string[rptr]] -= 1

            if(hashMap[string[rptr]] >= 0):
                count -= 1

            rptr += 1

        else:
            rptr += 1

        if(count == 0):
            
            while(True):

                if(string[lptr] in hashMap):
                    if(hashMap[string[lptr]] == 0):

                        if (rptr - lptr) < minLen:
                            minLen = rptr - lptr
                            minSub = string[lptr : rptr]

                            hashMap[string[lptr]] += 1
                            count += 1
                            lptr += 1

                            break

                        else:
                            hashMap[string[lptr]] += 1
                            lptr += 1
                            count += 1
                            break

                    else:
                        hashMap[string[lptr]] += 1
                        lptr += 1

                else:
                    lptr += 1

    return minSub
                


def main():
    ip = input("Enter the input string: ")
    substr = input("Enter the substring to search: ")

    print(f"Minimum Window Substring: {minSub(ip, substr)}")

if __name__ == "__main__":
    main()