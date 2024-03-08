pizza_size = {}
slices = int(input())
for i in range(1,slices+1):
    pizza_size[i] = int(input())
pizza_size[0] =0
max_pizza = max(pizza_size, key = pizza_size.get)
def eat_pizza(slices,max_pizza,pizza_size):
    chihuo_list = []
    chihuo_list.append(pizza_size[max_pizza])
    right = max_pizza+1
    left = max_pizza-1
    del pizza_size[max_pizza]
    for i in range(2,slices+1):
        if right == slices+1:
            right = 0
        elif left>0 and right < slices+1:
            if i%2 == 0:
                if pizza_size[right]>pizza_size[left]:
                    del pizza_size[right]
                    right+=1
                else:
                    del pizza_size[right]
                    left -=1

            else:
                if pizza_size[right]>pizza_size[left]:
                    chihuo_list.append(pizza_size[right])
                    del pizza_size[right]
                    right += 1
                else:
                    chihuo_list.append(pizza_size[left])
                    del pizza_size[left]
                    left -=1

    return sum(chihuo_list)

print(eat_pizza(slices,max_pizza,pizza_size))