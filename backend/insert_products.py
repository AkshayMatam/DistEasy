from database.connection import get_connection

conn = get_connection()
cursor = conn.cursor()

products = [
    ("Layina Dates 250g", 150, 0),
    ("Layina Dates 500g (1+1)", 284, 0),
    ("Lion Dates Syrup 500g", 206, 0),
    ("Lion Choco Dates With Almond 150g", 100, 0),
    ("Lion Datenuts Bites 120g", 150, 0),
    ("Lion Datenuts Bites 200g", 250, 0),
    ("Lion Datenuts Bites 240g", 300, 0),
    ("Lion Datenuts Bites 280g", 350, 0),
    ("Lion Datenuts Bites 368g (1+1)", 400, 0),
    ("Lion Dates Powder 500 Jar", 324, 0),
    ("Lion Dates Syrup 250g", 107, 0),
    ("Lion Delicacy Dates Branch 500g", 354, 0),
    ("Lion Delicacy Dates 250g", 154, 0),
    ("Lion Deseeded Dates 500g R", 154, 0),
    ("Lion Deseeded Dates 200g R", 62, 0),
    ("Lion Deseeded Dates 250g Cup", 89, 0),
    ("Lion Deseeded Dates Cup", 162, 0),
    ("Lion Desert King Dates 500g Cup", 299, 0),
    ("Lion Desert King Dates 250g R", 135, 0),
    ("Lion Desert King Dates 500g R", 279, 0),
    ("Lion Dry Dates 500g P", 186, 0),
    ("Lion Grape Squash 700ml", 172, 0),
    ("Lion Healthmix 250g (1+1)", 153, 0),
    ("Lion Honey 100g", 60, 0),
    ("Lion Honey 18g", 10, 0),
    ("Lion Honey 1kg SUPER SAVER", 560, 0),
    ("Lion Honey 250g (1+1)", 160, 0),
    ("Lion Honey 400g (1+1)", 270, 0),
    ("Lion Honey 50g", 38, 0),
    ("Lion Kalmi Dates 400g R", 280, 0),
    ("Lion Kimjo Dates 500g", 240, 0),
    ("Lion Mixed Fruit Squash 700ml", 165, 0),
    ("Lion Mixed Fruit Jam 125g", 25, 0),
    ("Lion Mixed Fruit Jam 250g (1+1)", 116, 0),
    ("Lion Mixed Fruit Jam 500g (1+1)", 210, 0),
    ("Lion Muesli 250g", 124, 0),
    ("Lion Oats 200g R", 50, 0),
    ("Lion Orange Squash 700ml", 192, 0),
    ("Lion Rose Sharabath 700ml", 144, 0),
    ("Lion Sulthan Dates 250g (1+1)", 112, 0),
    ("Lion Sulthan Dates 500g (1+1)", 215, 0),
]

cursor.executemany(
    "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
    products
)

conn.commit()
conn.close()

print("Products inserted successfully!")