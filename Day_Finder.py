days=("Monday","tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
given=61        #given days in problem
day="Monday"    #given day in problem

if given%7==0:
    print(day)
else:
    digit=given%7
    ans=days[digit]
    print(ans)
