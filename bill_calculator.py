# Simple Bill Calculator

price = float(input("Enter price of one item: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(f"{quantity} items at {price:.2f} each = {total:.2f}")
