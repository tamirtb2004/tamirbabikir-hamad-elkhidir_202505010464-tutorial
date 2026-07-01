# Week 5 - Café Billing System Documentation

## 1. Problem Analysis

### 1.1 Problem Statement
The café currently calculates customer bills manually, which is slow and 
error-prone. We need a Python program that automatically calculates the 
total bill based on item quantities and prints a formatted receipt.

### 1.2 Inputs
- Customer name
- Quantity of coffee ordered
- Quantity of tea ordered
- Quantity of sandwiches ordered

### 1.3 Outputs
- A formatted receipt showing the customer name, quantity of each item, 
  and the total price

### 1.4 Process Flow
1. Get customer name and item quantities from the user
2. Calculate the cost for each item (quantity × price)
3. Sum all costs to get the total
4. Print a formatted receipt

### 1.5 Constraints
- Prices are fixed (Coffee RM8.50, Tea RM6.00, Sandwich RM12.00)
- Quantities must be whole numbers (non-negative)
- Only three menu items are supported

## 2. Task Decomposition
- Get user input (name + quantities)
- Calculate total cost (utils.py: calculate_total)
- Format and print the receipt (utils.py: print_receipt)
- Tie it together in main.py

## 3. Pseudocode
```
START
  ASK for customer name
  ASK for coffee quantity
  ASK for tea quantity
  ASK for sandwich quantity

  total = calculate_total(coffee_qty, tea_qty, sandwich_qty)

  print_receipt(name, coffee_qty, tea_qty, sandwich_qty, total)
END
```