# Sales Registration System

A simple Python program to manage product sales and calculate the total purchase price. This application allows users to register multiple products and receive a complete purchase summary.

## Description

This program helps you register products interactively. You can enter the product name, unit price, and quantity. The system calculates individual totals and provides a comprehensive invoice at the end of your shopping session.

## Project Structure

The code is organized into three main files: 


- **main.py**: Entry point that initializes the program
- **SalesRegistration.py**: Handles individual product registration with validation
- **ContinueShopping.py**: Manages the shopping loop and displays the purchase summary

---

## Function Documentation

### `SalesRegistration()`

**Location:** [SalesRegistration.py](SalesRegistration.py)

**Purpose:** Collects product information from the user with validation.

**Parameters:** None

**Return Value:** 
- Returns a tuple containing: `(ProductName, ProductPrice, ProductQuantity, Total)`
  - `ProductName` (str): Name of the product
  - `ProductPrice` (float): Unit price of the product
  - `ProductQuantity` (int): Quantity requested
  - `Total` (float): Product price × quantity

**Error Handling:** 
- Validates that price and quantity are numeric values
- Prompts user to retry if a `ValueError` is raised (e.g., non-numeric input)

**Example Flow:**
```
Enter the product name: Laptop
Enter the product price: 500.00
How many products do you want to buy?: 2
Returns: ("Laptop", 500.0, 2, 1000.0)
```

---

### `ContinueShopping()`

**Location:** [ContinueShopping.py](ContinueShopping.py)

**Purpose:** Main shopping loop that manages multiple product registrations and displays the final bill.

**Parameters:** None

**Return Value:** None (prints results to console)

**Functionality:**
1. Initializes an empty `History` list to store product data
2. Loops through a shopping session:
   - Prompts user if they want to buy something (yes/no)
   - If **"yes"**: Calls `SalesRegistration()` and appends result to history
   - If **"no"**: Displays purchase summary and exits loop
   - If invalid input: Shows error message and reprompts
3. **Purchase Summary** displays:
   - Each product with its name, unit price, quantity, and subtotal
   - Final total amount to pay
   - Thank you message

---

## How to Use

1. **Install Python** (version 3.x required)
2. **Place all three files in the same folder:**
   - main.py
   - SalesRegistration.py
   - ContinueShopping.py
3. **Run the program:**
   ```bash
   python main.py
   ```
4. **Follow the prompts:**
   - Enter "yes" to add a product
   - Enter product details when prompted
   - Enter "no" when finished shopping
   - Review your purchase summary

## Main Features

✓ **Error Validation:** Automatically detects and rejects non-numeric inputs for price and quantity  
✓ **Product History:** Maintains a list of all products added during the session  
✓ **Purchase Summary:** Displays itemized list with individual totals and grand total  
✓ **User-Friendly:** Clear prompts and error messages guide the user through the process  
✓ **Calculation Accuracy:** Automatically computes subtotals and final amount  

## Example Session

```
Do you want to buy something? (yes/no): yes
Enter the product name: Apple
Enter the product price: 1.50
How many products do you want to buy?: 5
Product registered successfully.
Do you want to buy something? (yes/no): yes
Enter the product name: Bread
Enter the product price: 2.00
How many products do you want to buy?: 3
Product registered successfully.
Do you want to buy something? (yes/no): no

--- PURCHASE SUMMARY ---
Product: Apple | Unit Price: 1.5 | Quantity: 5 | Total to pay: 7.5
Product: Bread | Unit Price: 2.0 | Quantity: 3 | Total to pay: 6.0
------------------------------
FINAL TOTAL TO PAY: $ 13.5
Thank you for your purchase, come back soon
```

## Technical Notes

- Uses Python's built-in `input()` for user interaction
- Implements exception handling with try-except blocks
- Stores data in tuples and lists for efficient management
- Case-insensitive input handling (`.lower()` method)
- String formatting for clean console output



