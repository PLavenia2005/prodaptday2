products = ["Laptop","Mouse","Keyboard"]
print("Initial products:",products)

products.append("Monitor")
print("\nAfter adding monitor:")
print(products)

new_products = ["Tablet","Webcam"]
products.extend(new_products)
print("\nAfter combining another warehouse:")
print(products)

products.remove("Mouse")
print("\nAfter removing mouse:")
print(products)

shipped = products.pop()
print("\nShipped product:",shipped)
print("Remaining products:", products)

count = products.count("Laptop")
print("\nLaptop appears", count, "time(s).")

position = products.index("Monitor")
print("Monitor is located at index:", position)

products.sort()
print("\nSorted products:")
print(products)

products.reverse()
print("\nReverse order:")
print(products)

backup = products.copy()
print("\nBackup inventory:")
print(backup)

temp_inventory = backup.copy()
temp_inventory.clear()
print("\nTemporrary inventory after clear:")
print(temp_inventory)