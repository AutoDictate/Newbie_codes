arr=[1,2,3,5]
arr1=[]

for i in range(1,6):
    arr1.append(i)
print(arr1)

for i in arr1:
    if arr[i]!=arr1[i]:
        break
print(arr1[i])