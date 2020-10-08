# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  https://www.geeksforgeeks.org/python-return-statement/

def pizzashack():

    print("Welcome to the Pizza Shack! Every pizza is served with tomato sauce and cheese, but you can add toppings on top of that, as you'd like, and as your money permits!")
    print("Every cheese pizza starts at $4. Today's add-on toppings are pepperoni, sausage, olives, mushrooms, bell pepper, and extra cheese!")
    x = int(input("How much money do you have to spend?: "))

    toppings = []
    y = 4
    try:
        while y <= x: 
            topping = input("Enter a topping you would like or type 'order' to submit your order: ")
            toppings.append(topping)
            
            if topping == 'sausage' or topping == 'pepperoni':
                y = y + 1.50
                if y > x:
                    y = y - 1.50
                    print("You don't have enough money to afford this topping. Please type 'order'")
                    break
            elif topping == 'olives' or topping == 'bell pepper' or topping == 'mushrooms':
                y = y + .50
                if y > x:
                    y = y - .50
                    print("You don't have enough money to afford this topping. Please type 'order'")
                    break
            elif topping == 'extra cheese':
                y = y + 1.00
                if y > x:
                    y = y - 1.00
                    print("You don't have enough money to afford this topping. Please type 'order'")
                    break
            elif topping == 'order':
                break
    except:
        print("Please enter a valid topping.")
                    
    print("Your " + str(toppings[:-1]) + " pizza will cost $" + str(y))
    change = x - y
    return change #why is change not being returned and used 


pizzashack() 
print("You have $" + str(change) + " left.") 
#again = input("You have $" + str(change) + " left. Would you like to order anither pizza?")
