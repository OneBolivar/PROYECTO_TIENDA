from SalesRegistration import SalesRegistration 

def ContinueShopping():    
    History = []
    Loop = True
    while Loop:
        KeepShopping = input("Do you want to buy something? (yes/no): ")
        if KeepShopping == "yes":
            ProductData = SalesRegistration()
            History.append(ProductData)
            print("Product registered successfully.")
        elif KeepShopping == "no":
            print("\n--- PURCHASE SUMMARY ---")
            TotalToPay = 0
            for Position in History:
                print(f"Product: {Position[0]} | Unit Price: {Position[1]} | Quantity: {Position[2]} | Total to pay: {Position[3]}")
                TotalToPay = TotalToPay + Position[3]
            print("-" * 30)
            print("FINAL TOTAL TO PAY: $", TotalToPay)
            print("Thank you for your purchase, come back soon")
            Loop = False
        else:
            print("ERROR!!! Only enter yes or no")