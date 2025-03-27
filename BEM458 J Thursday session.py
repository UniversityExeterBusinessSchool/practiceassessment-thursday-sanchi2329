#######################################################################################################################################################
# 
# Name:SAnchit Gupta
# SID:750028037
# Exam Date:27/03/2001
# Module:final assessment
# Github link for this assignment:  
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 
#code for the problem

# The customer feedback text
customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# Dictionary keywords comments
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Allocated keys based on first and last digit of SID 
# My SID is  750028037 so  both digits are 7
allocated_keys = [7]

# Making an empty list to store
my_list = []

# Loop through each key
for key in allocated_keys:
    # corresponding keyword from the dictionary
    word = key_comments[key]
    
    # to find the start index of the word 
    start = customer_feedback.find(word)
    
    # If the word is found (find() returns -1 if not found)
    if start != -1:
        # To calculate the end index of the word 
        end = start + len(word)
        
        # Append the (start, end) tuple to the list
        my_list.append((start, end))

# Output 
print(my_list)



##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:
# Insert last two digits of ID number here:

# Write your code for Operating Profit Margin

# Write your code for Revenue per Customer

# Write your code for Customer Churn Rate

# Write your code for Average Order Value

# Call your designed functions here



# code for Question 2

# entering the first two digits of my SID so my SID IS 750028037
first_two_digits = 75

# entering the last two digits of my SID
last_two_digits = 37

# now as per the question calculating 

# code for Operating Profit Margin
# Formula for operating profit margin is (Operating Profit / Revenue) * 100
def operating_profit_margin(operating_profit, revenue):
    return (operating_profit / revenue) * 100

# code for Revenue per Customer
# Formula for  Revenue / Total Customers
def revenue_per_customer(revenue, customers):
    return revenue / customers

# code for Customer Churn Rate
# Formula for (Customers Lost / Total Customers at Start) * 100
def customer_churn_rate(customers_lost, total_customers_start):
    return (customers_lost / total_customers_start) * 100

# code for Average Order Value
# Formula for  Revenue / Number of Orders
def average_order_value(revenue, number_of_orders):
    return revenue / number_of_orders

# Calling the designed functions here
# Using 75 as Revenue / Total Customers, and 37 as Operating Profit / Customers Lost / Orders

revenue = first_two_digits
operating_profit = last_two_digits
customers = first_two_digits
customers_lost = last_two_digits
total_customers_start = first_two_digits
number_of_orders = last_two_digits

# Calling the functions
opm = operating_profit_margin(operating_profit, revenue)
rpc = revenue_per_customer(revenue, customers)
ccr = customer_churn_rate(customers_lost, total_customers_start)
aov = average_order_value(revenue, number_of_orders)

# Print results
print(f"Operating Profit Margin: {opm:.2f}%")
print(f"Revenue per Customer: £{rpc:.2f}")
print(f"Customer Churn Rate: {ccr:.2f}%")
print(f"Average Order Value: £{aov:.2f}")







##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here

# importing the libraries
import numpy as np
from sklearn.linear_model import LinearRegression
# Data
prices = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
demand = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])

# Create and fit linear regression model
model = LinearRegression()
model.fit(prices, demand)

# Predict demand at price £52
predicted_demand_52 = model.predict(np.array([[52]]))[0]

# Calculate revenue = price * predicted demand
revenues = prices.flatten() * model.predict(prices)
max_revenue_index = np.argmax(revenues)
optimal_price = prices[max_revenue_index][0]
max_revenue = revenues[max_revenue_index]

# Output results
print(f"Demand at £52: {predicted_demand_52:.2f} units")
print(f"Optimal Price for Maximum Revenue: £{optimal_price}")
print(f"Maximum Revenue: £{max_revenue:.2f}")


##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

# importing all the libraries 

import random
import matplotlib.pyplot as plt

# Get max value from student ID
max_value = int(input("Enter your Student ID: "))

#  to generate 100 random numbers between 1 and the student ID
random_numbers = [random.randint(1, max_value) for i in range(100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='o', linestyle='--', label='Random Numbers', color='blue')
plt.title("Line Chart of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Random Number")
plt.legend()
plt.grid(True)
plt.show()




