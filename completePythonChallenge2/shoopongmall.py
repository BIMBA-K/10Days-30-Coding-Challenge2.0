def shopping():
    products = {
        "Pen": 10,
        "Book": 50,
        "Pencil": 5,
        "Bag": 500
    }

    total = 0
    items = 0
    expensive = ""
    max_price = 0

    while True:
        product = input("Enter product (or 'done'): ")

        if product.lower() == "done":
            break

        if product in products:
            quantity = int(input("Enter quantity: "))

            total += products[product] * quantity
            items += quantity

            if products[product] > max_price:
                max_price = products[product]
                expensive = product

        else:
            print("Product Not Available")

    print("\n------ BILL ------")
    print(f"Total Items : {items}")
    print(f"Total Bill : ₹{total}")
    print(f"Most Expensive Item : {expensive}")

shopping()