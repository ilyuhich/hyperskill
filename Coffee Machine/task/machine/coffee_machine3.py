# Write your code here
# i make it using lists and some dicts
# will think about using lists inner lists or something like multilevel arrays
import time

make_list = ['Starting to make a coffee',
             'Grinding coffee beans',
             'Boiling water',
             'Mixing boiled water with crushed coffee beans',
             'Pouring coffee into the cup',
             'Pouring some milk into the cup',
             'Coffee is ready!']

ingridients = {'espresso': [250, 0, 16, 1, -4],
               'latte': [350, 75, 20, 1, -7],
               'cappuccino': [200, 100, 12, 1, -6]  # water, milk, coffee, cups, money
               }

fill_input = ['Write how many ml of water do you want to add: ',
              'Write how many ml of milk do you want to add: ',
              'Write how many grams of coffee beans do you want to add: ',
              'Write how many disposable cups of coffee do you want to add: '
              ]

fixed_how_many_has = [400, 540, 120, 9, 550]  # water, milk, coffee, cups, money


def action():
    global ingridients, fill_input, fixed_how_many_has
    action = input('\nWrite action (buy, fill, take):')
    if action == 'take':
        print(f'I gave you ${fixed_how_many_has[4]}')
        fixed_how_many_has[4] = 0

    elif action == 'fill':
        for kind in range(0, len(fixed_how_many_has) - 1):
            fixed_how_many_has[kind] += int(input(fill_input[kind]))
#        now_water += int(input('Write how many ml of water do you want to add: '))
#        now_milk += int(input('Write how many ml of milk do you want to add: '))
#        now_coffee_beans += int(input('Write how many grams of coffee beans do you want to add: '))
#        disposable_cups += int(input('Write how many disposable cups of coffee do you want to add: '))
    elif action == 'buy':
        coffee = int(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: '))
        if coffee == 1:
            coffee = 'espresso'
        elif coffee == 2:
            coffee = 'latte'
        elif coffee == 3:
            coffee = 'cappuccino'
            for a in range(0, len(fixed_how_many_has)):
                fixed_how_many_has[a] += -ingridients[coffee][a]
    var_var()
    now_print()


def var_var():
    global now_water, now_milk, now_coffee_beans, money, disposable_cups
    now_water, now_milk, now_coffee_beans, disposable_cups, money = fixed_how_many_has


def now_print():
    global now_water, now_milk, now_coffee_beans, disposable_cups, money
    print('\nThe coffee machine has:')
    print(f'{now_water} of water')
    print(f'{now_milk} of milk')
    print(f'{now_coffee_beans} of coffee beans')
    print(f'{disposable_cups} of disposable cups')
    print(f'{money} of money')


var_var()
now_print()
action()
