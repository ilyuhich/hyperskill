# Write your code here
import time

text_list = ['Starting to make a coffee',
             'Grinding coffee beans',
             'Boiling water',
             'Mixing boiled water with crushed coffee beans',
             'Pouring coffee into the cup',
             'Pouring some milk into the cup',
             'Coffee is ready!']

ingridients = {'water': 200,
               'milk': 50,
               'coffee beans': 15
               }


def cups_need_query():
    # Ask to user to enter how many coffee to prepare
    cups_number = int(input('Write how many cups of coffee you will need: '))
    # print(f'You order {cups_number} cups of coffee')
    return (cups_number)


def how_many_has():
    now_water = int(input('Write how many ml of water the coffee machine has: '))
    now_milk = int(input('Write how many ml of milk the coffee machine has: '))
    now_coffee_beans = int(input('Write how many grams of '
                                 'coffee beans the coffee machine has: '))
    #    now_water = 300
    #    now_milk = 65
    #    now_coffee_beans = 100
    return now_water, now_milk, now_coffee_beans


def calc(cups_number):  # calculate how much ingridients we neeed
    water_need = ingridients['water'] * cups_number
    milk_need = ingridients['milk'] * cups_number
    coffee_beans_need = ingridients['coffee beans'] * cups_number
    return water_need, milk_need, coffee_beans_need


def calc_output(cups_number, water_need, milk_need, coffee_beans_need):
    # output of our calculations, what we need to prepare coffee
    print('For %s cups of coffee you will need:' % cups_number)
    print('%s ml of water' % water_need)
    print('%s ml of milk' % milk_need)
    print('%s g of cofee beans' % coffee_beans_need)  # some comments


def cups_enought(now_water, now_milk, now_coffee_beans):
    max_cups = min(now_water // ingridients['water'],
                   now_milk // ingridients['milk'],
                   now_coffee_beans // ingridients['coffee beans'])
    return max_cups


now_water, now_milk, now_coffee_beans = how_many_has()
cups_number = cups_need_query()
water_need, milk_need, coffee_beans_need = calc(cups_number)
cups_can_do = cups_enought(now_awater, now_milk, now_coffee_beans)


if cups_can_do == cups_number:
    print('Yes, I can make that amount of coffee')
elif cups_can_do > cups_number:
    print(f"Yes, I can make that amount of coffee (and even "
          f"{cups_can_do - cups_number} more than that)")
else:
    print(f"No, I can make only {cups_can_do} cups of coffee")
