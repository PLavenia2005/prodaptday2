categories = []
products = []
stocks = []

num_categories=3

for i in range(num_categories):
    category = input(f"Enter Category {i+1}: ")
    categories.append(category)
    
    category_products = []
    category_stocks = []

    for j in range(2):
        product  = input(f"Enter product {j+1} for {category}: ")
        stock = int(input(f"Enter stock for {product}: "))

        category_products.append(product)
        category_stocks.append(stock)

    products.append(category_products)
    stocks.append(category_stocks)

print("\n-------- Inventory Report ------------\n")

for i in range(num_categories):
    print(f"Category: {categories[i]}")
    for j in range(2):
        print(f"{products[i][j]} : {stocks[i][j]} units")
    print()
