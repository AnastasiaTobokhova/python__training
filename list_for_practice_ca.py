# Carly's Clippers
# You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block.
# Your job is to go through the lists of data that have been collected in the past couple of weeks.
# You will be calculating some important metrics that Carly can use to plan out the operation of the business
# for the rest of the month.
#
# You have been provided with three lists:
#
# hairstyles: the names of the cuts offered at Carly’s Clippers.
# prices: the price of each hairstyle in the hairstyles list.
# last_week: the number of purchases for each hairstyle type in the last week.
# Each index in hairstyles corresponds to an associated index in prices and last_week.
#
# For example, The hairstyle "bouffant" has an associated price of 30 from the prices list, and was purchased 2 times in the last week as shown in the last_week list. Each of these elements are in the first index of their respective lists.
#
# Let’s get started!




hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for i in prices:
  total_price = sum(prices)
print(total_price)

average_price = total_price/len(prices)
print('Average Haircut Price: ' +str(int(average_price)))

new_prices = []
for i in prices:
  i - 5
  new_prices.append(i-5)
print('New prices = '+ str(new_prices))

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue = prices[i]*last_week[i]
print('Total revenue: '+ str(total_revenue))

average_daily_revenue = total_revenue/7
print('Average daily revenue: '+ str(average_daily_revenue))

cuts_under_30 = [i for i in new_prices if i < 30]
print(cuts_under_30)



