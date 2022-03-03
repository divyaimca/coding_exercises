from itertools import count


def raiin_water(n,li):
    w_counter = 0
    try:
        for i in range(1,n):  
            leftheight = max(li[:i])
            rightheight = max (li[i:])
            counter = min(leftheight,rightheight) - li[i]
            if counter > 0:
                w_counter += counter

    except IndexError:
        pass

    return w_counter

def optimized_rain_water(arr):
    print(arr)
    w_counter = 0



print(raiin_water(4,[7,4,0,9]))
print(raiin_water(3,[6,9,9]))
print(raiin_water(12,[0,1,0,2,1,0,1,3,2,1,2,1]))

