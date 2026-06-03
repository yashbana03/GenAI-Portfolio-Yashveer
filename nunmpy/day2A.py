# %%
import numpy as np
import matplotlib.pyplot as plt


# %%
# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])

print("+++ ZOMATO SALES ANALYSIS +++")
print("\n Sales Data shape:" , sales_data.shape)

print("\n Sample data for first 3 restaurants:")
print(sales_data[0:3])
print("\n ")

# %%
# total salse per year 
print(np.sum(sales_data, axis = 0 ))
yearly_total = np.sum(sales_data[:, 1:], axis=0)
print("\n Total sales per year:")
print(yearly_total)


# minimum sales per restaurant
print("\n Minimum sales per restaurant:")
min_sales= np.min(sales_data[: , 1:], axis= 1)
print(min_sales)

# max sales per year 
print("\n Maximum sales per year:")
max_sales = np.max(sales_data[:, 1:], axis= 0)
print(max_sales)

#avg sales per reataurant 
print("\n Average sales per restaurant:")
avg_sales  = np.mean(sales_data[:, 1:], axis = 1)
print(avg_sales)

# cummulative 
cumsum = np.cumsum(sales_data[: , 1:], axis = 1)
print("\n Cumulative sales per restaurant:")
print(cumsum)

# %%
plt.figure(figsize=(8, 6))

plt.plot(np.mean(cumsum, axis= 0))
plt.title("Average Cumulative Sales Over restaurant ")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)


