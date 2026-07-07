products = {
    "Black Dates": [800, 900, 1000],
    "Kimia Dates": [300, 350, 400],
    "Honey 1kg": [50, 60, 70]
    "Jam 1kg": [100, 120, 140]
}

highest_product = ""
highest_average = 0

for product, sales in products.items():

    average = sum(sales) / 4
    order = average * 1.1

    print(product)
    print("Average Sales:", round(average))
    print("Recommended Order:", round(order))
    print()

    if average > highest_average:
        highest_average = average
        highest_product = product

print("Top Selling Product:", highest_product)