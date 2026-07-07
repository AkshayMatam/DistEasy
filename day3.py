import csv

with open("products_with_stock.csv") as file:

    reader = csv.DictReader(file)

    for row in reader:

        product = row["Product"]
        stock = int(row["Current_Stock"])

        month1 = int(row["Month1"])
        month2 = int(row["Month2"])
        month3 = int(row["Month3"])

        average = (month1 + month2 + month3) / 3

        recommended_order = average * 1.1

        print("-------------------")
        print("Product:", product)
        print("Current Stock:", stock)
        print("Recommended Order:", round(recommended_order))

        if stock < 50:
            print("LOW STOCK ALERT")