# Small Business Sales Calculator

print("===== SMALL BUSINESS SALES CALCULATOR =====")

# Input section
business_name = input("Enter business name: ")
product_name = input("Enter product name: ")

quantity = int(input("Enter quantity sold: "))
price = float(input("Enter price per product: "))

# Calculations
total_sales = quantity * price

tax = total_sales * 0.05      # 5% tax
discount = total_sales * 0.10 # 10% discount

final_amount = total_sales + tax - discount

# Output section
print("\n===== SALES REPORT =====")
print("Business Name:", business_name)
print("Product Name:", product_name)
print("Quantity Sold:", quantity)
print("Price Per Product: Le", price)

print("Total Sales: Le", total_sales)
print("Tax (5%): Le", tax)
print("Discount (10%): Le", discount)

print("Final Amount: Le", final_amount)

print("\nThank you for using the Sales Calculator!")
