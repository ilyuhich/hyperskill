meals = {"pasta": "tomato, basil, garlic, salt, pasta, olive oil",
         "apple pie": "apple, sugar, salt, cinnamon, flour, egg, butter",
         "ratatouille": "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt",
         "chocolate cake": "chocolate, sugar, salt, flour, coffee, butter",
         "omelette": "egg, milk, bacon, tomato, salt, pepper"}

ingridient = input()

for key, val in meals.items():
    if ingridient in val:
        print(f"{key} time!")
