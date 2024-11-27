arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
subArrays = list()
n = len(arr)

for i in range(n-k+1):
    count = 0
    avg = 0
    for j in range (k):
        count += arr[i+j]
        if j==k-1:
            avg = count/k
            if avg >= threshold:
                subArrays.append(arr[i:i+k:])

numSubArrays = len(subArrays)
print(f"Para {arr} el numero de sub-arrays de longitud {k} y que promedien {threshold} es: {numSubArrays} y son los siguientes: {subArrays}")
