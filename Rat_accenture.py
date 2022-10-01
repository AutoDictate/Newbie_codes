def calculate(r,unit,arr,n):
    if n==0:
        return -1
    totalfoodreq=r*unit
    foodtillnow=0
    house=0
    
    for house in range(n):
        foodtillnow+=arr[house]
        print(foodtillnow)
        if foodtillnow >=totalfoodreq:
            break
        
    if totalfoodreq>foodtillnow:
        return 0
    return house +1

r=int(input())
unit=int(input())
n=int(input())
        
arr=list(map(int,input().split()))
print(calculate(r,unit,arr,n))    