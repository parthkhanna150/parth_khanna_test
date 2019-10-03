"""
Question B
The goal of this question is to write a software library that accepts 2 version string as input
and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is
greater than “1.1”. Please provide all test cases you could think of.
"""

# given two versions, returns which one is higher
def compare_version(v1, v2):

    # split version strings into arrays
    arr1 = v1.split(".")
    arr2 = v2.split(".")
    i = 0

    # in a while loop compare the corresponding int values of the arrays
    while(i < len(arr1) and i < len(arr2)):
        if int(arr2[i]) > int(arr1[i]):
            return -1

        elif int(arr1[i]) > int(arr2[i]):
            return 1
        i += 1

    # if nothing returned yet -> all numbers upto the last common index are equal
    # next check, for whether there exist non-zero numbers after this index in each array
    # copy value of i (last common index) in a temp variable
    j = i

    # check for presence of non-zero numbers in both arrays
    if i!=len(arr1):
        while i < len(arr1):
            if int(arr1[i])!=0:
                return 1
            i+=1

    elif j!=len(arr2):
        while j < len(arr2):
            if int(arr2[j])!=0:
                return -1
            j+=1

    return 0


if __name__ == '__main__':

    try:
        v1 = input("Enter version 1: ")
        v2 = input("Enter version 2: ")

        result = compare_version(v1,v2)
        if result == 0:
            print("Same version numbers!")
        elif result == 1:
            print(v1,"is higher than",v2)
        else:
            print(v1,"is less than",v2)

    except Exception as e:
        print(e)
