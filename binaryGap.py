def solution(N):
    p = binary(N)                       #created a helper function to convert in binary
    a = [int(x) for x in str(p)]        #converted number to list
    count = 0                           #count variable to keep counting
    b = [0,0]                           #another list for storing several occurences of zeroes
    for i in range(0,len(a)-1):         
        if a[i] == 1 and a[i+1] == 0:
            j = i+1
            count = 0
            for j in range(j,len(a)):
                if a[j] == 0:
                    count = count + 1
                else:
                    b.append(count)
                    break
        else:

            pass
    maximum = max(b)
    if maximum >= 1:
        return maximum                 #returning count values if any length of zeroes in between two ones.
    else:
        return 0                       #returning zero because no length is availabel as per requirement
    pass

def binary(num):
    return "{0:b}".format(int(num))
    
# added driver code below to check your own values
num = 20
k = solution(num)
print(k)
