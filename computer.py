import random
low=1
high=100
mid=(low+high)/2
number = random.randint (low, high)
Counter=0
while True:
    if number==mid:
        print("Win in", +Counter,"tries!")
        break
    elif number<mid:
        high=mid-1
        Counter+=1
        mid=(low+high)/2
    else:
        low=mid+1
        mid=(low+high)/2
        Counter+=1