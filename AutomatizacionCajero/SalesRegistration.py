def SalesRegistration():
    VALIDATOR = True
    while VALIDATOR:  
        try:
            ProductName = input("Enter the product name: ")  
            ProductPrice = float(input("Enter the product price: "))
            ProductQuantity = int(input("How many products do you want to buy?: "))
            Total = ProductPrice * ProductQuantity  
            VALIDATOR = False
            # Returning the data as a tuple
            return (ProductName, ProductPrice, ProductQuantity, Total)
        except ValueError:       
            print("ERROR! You must enter a number. Try again.")
            