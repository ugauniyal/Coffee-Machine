class CoffeeMachine():
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550
        self.action()

    def action(self):
        ui = input('\nWrite action (buy, fill, take, remaining, exit): ')
        if ui == 'buy':
            self.buy()
        elif ui == 'fill':
            self.fill()
        elif ui == 'take':
            self.take()
        elif ui == 'remaining':
            self.remaining()
        elif ui == 'exit':
            self.exit()

    def buy(self):
        choice = (input('What do you want to buy? 1 - espresso, 2 - latte,'
                        ' 3 - cappuccino, back - to main menu: '))
        if choice == '1':
            self.espresso()
        elif choice == '2':
            self.latte()
        elif choice == '3':
            self.cappuccino()
        elif choice == 'back':
            self.back()

    def espresso(self):
        if self.water >= 250 and self.coffee_beans >= 16:
            print('I have enough resources, making you a coffee!')
            self.cups -= 1
            self.water -= 250
            self.milk -= 0
            self.coffee_beans -= 16
            self.money += 4
            self.action()
        elif self.water < 250:
            print('Sorry, not enough water!')
            self.action()
        elif self.coffee_beans < 16:
            print('Sorry, not enough coffee beans!!')
            self.action()

    def latte(self):
        if self.water >= 350 and self.coffee_beans >= 20 and self.milk >= 75:
            print('I have enough resources, making you a coffee!')
            self.cups -= 1
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.money += 7
            self.action()
        elif self.water < 350:
            print('Sorry, not enough water!')
            self.action()
        elif self.coffee_beans < 20:
            print('Sorry, not enough coffee beans!!')
            self.action()
        elif self.milk < 75:
            print('Sorry, not enough milk!!')
            self.action()

    def cappuccino(self):
        if self.water >= 200 and self.coffee_beans >= 12 and self.milk >= 100:
            print('I have enough resources, making you a coffee!')
            self.cups -= 1
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.money += 6
            self.action()
        elif self.water < 200:
            print('Sorry, not enough water!')
            self.action()
        elif self.coffee_beans < 12:
            print('Sorry, not enough coffee beans!!')
            self.action()
        elif self.milk < 100:
            print('Sorry, not enough milk!!')
            self.action()

    def back(self):
        self.action()

    def fill(self):
        add_water = int(input('Write how many ml of water do you want to add: '))
        add_milk = int(input('Write how many ml of milk do you want to add: '))
        add_beans = int(input('Write how many grams of coffee beans do you want to add: '))
        add_cups = int(input('Write how many disposable cups of coffee do you want to add: '))

        self.water += add_water
        self.milk += add_milk
        self.coffee_beans += add_beans
        self.cups += add_cups
        self.action()

    def take(self):
        print(f'I gave you ${self.money}')
        self.money -= self.money
        self.action()

    def remaining(self):
        print('The coffee machine has: ')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee_beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'${self.money} of money')
        self.action()

    def exit(self):
        quit()


CoffeeMachine()
