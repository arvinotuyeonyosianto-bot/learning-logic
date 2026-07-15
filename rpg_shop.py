print('==== WELCOME TO RPG GAME SHOP ====')
item='healing potion'
price=5.50
early_stock=100
customer=input('Hello Adventurer! Please Enter Your Name!: ')
print(f'\nGreetings, {customer.title()}!')
print(f'\n{item}: ${price}')
print(f'Stock: {early_stock}')
amount=int(input('How many potion do you want?: '))
total_cost=amount * price
remaining_stock=early_stock - amount
bonus_tokens=total_cost // 10
print('==== SHOP RECEIPT ====')
print('\nName: ', customer.title())
print('Items: ', item.title())
print('Total Cost: ', round(total_cost,2))
print('Remaining Stock: ', remaining_stock)
print('Bonus Tokens: ', bonus_tokens)
msg='\nthanks for shopping at rpg shop! see you later brave adventurer!'
print(msg.upper())