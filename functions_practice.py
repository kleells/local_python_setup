# Problem 2a
def hello():
    print("Hello")

hello()

# Problem 2b
def pack(item1, item2, item3):
    return[item1, item2, item3]

print(pack('towel', 'sunglasses', 'sunscreen'))
print(pack(1, 2, 3))

# Problem 2c 
def eat_lunch(lunch_menu):
    if len(lunch_menu) == 0:
        print("My lunchbox is empty!")
    elif:
        for x in range(len(lunch_menu)):
            if x == 0:
                print(f"First I'll eat {lunch_menu[0]}")
            else:
                print(f"Next I'll eat {lunch_menu[i]}")

eat_lunch(['soup', 'salad', 'cheese'])
eat_lunch([])
