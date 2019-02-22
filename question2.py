class Solution:

    def compareVersion(self, version1: 'str', version2: 'str') -> 'int':
        v1=version1
        v2=version2

        arr1 = v1.split(".")
        arr2 = v2.split(".")

        i = 0

        while(i < len(arr1) and i < len(arr2)):
            if int(arr2[i]) > int(arr1[i]):
                return -1

            elif int(arr1[i]) > int(arr2[i]):
                return 1
            i += 1

        j = i
        if i==len(arr2) and i!=len(arr1):
            while i < len(arr1):
                if int(arr1[i])!=0:
                    return 1
                i+=1

        elif j!=len(arr2) and j==len(arr1):
            while j < len(arr2):
                if int(arr2[j])!=0:
                    return -1
                j+=1

        return 0
