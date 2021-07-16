#Krati Younes
answer = raw_input("Do you need an internationnal shipping ?") 
if answer == 'yes': 
    print("please enter your Total :")
    total = input()
    shipping_cost = 15
    print("Internationnal base cost applied")
    if total <= 50:
        shipping_cost += 20
    elif total <= 100: 
        shipping_cost += 15
    else :
        shipping_cost += 5
    print("Your final internationnal cost is :")
    print(shipping_cost)
elif answer == 'no': 
    print("the cost of your shipping is 0")
else: 
    print("Please enter yes or no.") 

