import pyinputplus as pyip

prices = {"Wheat": 10, "White": 15, "Sourdough": 10, "Chicken": 20, "Turkey": 20, "Ham": 25, "Tofu": 15, 
        "Cheddar": 7, "Swiss": 10, "Mozzarella": 10, "Mayo": 3, "Lettuce": 5, "Tomato": 5, "Mustard": 5}
order=[]
a = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], "Choose bread type : \n")
b = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], "Choose meat type : \n")

order.append(a)
order.append(b)

cheese = pyip.inputYesNo("Cheese ? ")
if cheese == "yes":
        c=pyip.inputMenu(['Cheddar','Swiss','Mozzarella'],"Choose cheese type : \n")

add = ['Mayo', 'Lettuce', 'Tomato', 'Mustard']

for i in add:
        inp = pyip.inputYesNo("Do you want {} ? ".format(i))
        if inp =='yes':
                order.append(i)

num = pyip.inputInt("Number of sandwhiches: ", min=1)

cost = 0
for i in order:
        cost += prices[i]

print("Cost = ", cost*num)