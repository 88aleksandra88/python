glass_1="water"
glass_2="soda"

temp=glass_1
glass_1=glass_2
glass_2=temp

print('glass_1='+str(glass_1))
//glass_1=soda
print('glass_2='+str(glass_2))
//glass_2=water



number_of_steps=70
print("You're on step:")
print("number_of_steps +1")



//kilometer convert
miles=500
kilometers=miles * 1.609344
print(kilometers)
//804.674



//switch light
is_day = False
lights_on = not is_day

print('Daytime?')
print(is_day)

print('Lights on ?')
print(lights_on)



//checking numbers equality
print(10==10)
//numbers inequality
print(1 != 10)
result = 1 != 2
print(result)



//tarck sales data
stock = 600
kitten_sold = 500
target =500

target_hit = kitten_sold == target
print('Hit kitten sale target: ')
print(target_hit)

current_stock = stock - kitten_sold
in_stock = current_stock != 0
print('Kitten in stock')
print(in_stock)
