import sqlite3

conn = sqlite3.connect("disteasy.db")
cursor = conn.cursor()

products = [
("Layina Dates 250g",0),
("Layina Dates 500g (1+1)",0),
("Lion Dates Syrup 500g",0),
("Lion Choco Dates With Almond 150g",0),
("Lion Datenuts Bites 120g",0),
("Lion Datenuts Bites 200g",0),
("Lion Datenuts Bites 240g",0),
("Lion Datenuts Bites 280g",0),
("Lion Datenuts Bites 368g (1+1)",0),
("Lion Dates Powder 500 Jar",0),
("Lion Dates Syrup 250g",0),
("Lion Delicacy Dates Branch 500g",0),
("Lion Delicacy Dates 250g",0),
("Lion Deseeded Dates 500g R",0),
("Lion Deseeded Dates 200g R",0),
("Lion Deseeded Dates 250g Cup",0),
("Lion Deseeded Dates 500g R",0),
("Lion Deseeded Dates Cup",0),
("Lion Desert King Dates 500g Cup",0),
("Lion Desert King Dates 250g R",0),
("Lion Desert King Dates 500g R",0),
("Lion Dry Dates 500g P",0),
("Lion Grape Squash 700ml",0),
("Lion Healthmix 250g (1+1)",0),
("Lion Honey 100g",0),
("Lion Honey 18g",0),
("Lion Honey 1kg SUPER SAVER",0),
("Lion Honey 250g (1+1)",0),
("Lion Honey 400g (1+1)",0),
("Lion Honey 50g",0),
("Lion Kalmi Dates 400g R",0),
("Lion Kimjo Dates 500g",0),
("Lion Mixed Fruit Squash 700ml",0),
("Lion Mixed Fruit Jam 125g",0),
("Lion Mixed Fruit Jam 250g (1+1)",0),
("Lion Mixed Fruit Jam 500g (1+1)",0),
("Lion Muesli 250g",0),
("Lion Oats 200g R",0),
("Lion Orange Squash 700ml",0),
("Lion Rose Sharabath 700ml",0),
("Lion Sulthan Dates 250g (1+1)",0),
("Lion Sulthan Dates 500g (1+1)",0),
]

cursor.executemany(
    "INSERT INTO products (name, stock) VALUES (?, ?)",
    products
)

conn.commit()
conn.close()

print("Products inserted successfully!")