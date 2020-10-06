# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  

print("Welcome to the Pizza Shack! Every pizza is served with tomato sauce and cheese, but you can add toppings on top of that, as you'd like, and as your money permits!")
print("Today's add-on toppings are pepperoni, sausage, olives, mushrooms, bell pepper, and extra cheese!")
x = int(input("How much money do you have to spend?: "))


toppings = []
y = 4
while y <= x: 
    topping = input("Enter a topping you would like or type 'order' to submit your order: ")
    toppings.append(topping)
    
    if topping == 'sausage' or topping == 'pepperoni':
        y = y + 1.50
        if y > x:
            print("You don't have enough money to afford this topping.")
    elif topping == 'olives' or topping == 'bell pepper' or topping == 'mushrooms':
        y = y + .50
        if y > x:
            print("You don't have enough money to afford this topping.")
    elif topping == 'extra cheese':
        y = y + 1.00
        if y > x:
            print("You don't have enough money to afford this topping.")
    elif topping == 'order':
        break
    
print("Your pizza will cost $" + str(y))

