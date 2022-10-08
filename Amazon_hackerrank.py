nums=[3,2,4]
target = 6
index=[]

x=len(nums)

for i in range(0,3):
    for j in range(0,i):
        if nums[i]+nums[j] == target:
            index.append(j)
            index.append(i)
            print(index)
print("Bye...")


            

    