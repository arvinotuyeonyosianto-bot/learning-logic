#Villager Trading System Simulation
print("==== Villager Trade Simulation ====")
#input player name
customer_name = input("Player Name: ")
#input amount of items
diamond_count = int(input("Amount of Diamond: "))
sword_count = int(input("Amount of Sword: "))
#input fixed price variables
currency = "Emelard"
diamond_price = 1
sword_price = 24
#net total calculation process
total_diamond_cost = diamond_count * diamond_price
total_sword_cost = sword_count * sword_price
subtotal = total_diamond_cost + total_sword_cost
#tax calculation process (float concept)
tax_amount = subtotal * 0.1
final_bill = tax_amount + subtotal
#Reciept
print("\n==== Receipt ====")
print("Diamond: ", total_diamond_cost, currency)
print("Sword: ", total_sword_cost, currency)
print("Subtotal: ", subtotal, currency)
print("Villager Tax: 10%")
print("Total: ", final_bill, currency)