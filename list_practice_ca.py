# list practice
# Your code below:
toppings = ['pepperoni','pineapple','cheese','sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2,6,1,3,2,7,2]

# boss wants to know count the number or occurences
# of 2 in the prices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# find the lenght of the toppings lust
num_pizzas = len(toppings)
print(num_pizzas)

print('We sell', num_pizzas, 'different kinds of pizza!')

# data about the pizza toppings
pizza_and_prices = [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]
# print(pizza_and_prices)
# sort our pizza from low to high
pizza_and_prices.sort()
print(pizza_and_prices)
# store cheapest
cheapest_pizza = pizza_and_prices[0]
# store expensive
priciest_pizza = pizza_and_prices[-1]
# man bought expensive one need to remove it
pizza_and_prices.pop()
# we add new type of topping - peppers add it
pizza_and_prices.append([2.5, 'peppers'])
# store 3 low price pizzas to three cheapest
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)



