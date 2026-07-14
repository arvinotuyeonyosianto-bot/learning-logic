# --- GAME KDA CALCULATOR ---

# 1. Take user input
print("=== GAME PERFORMANCE CALCULATOR ===")
player_name = input("Enter Player name: ")

# 2.  input Player KDA and Level
kill = int(input("Enter total Kills: "))
death = int(input("Enter total Deaths: "))
assist = int(input("Enter total Assists: "))
level = int(input("Enter player level: "))

# 3. Logic and Math formula
# if the death is 0 set it to 1 to avoid zerodivision error in math
if death == 0:
    death = 1

kda_score = (kill + assist) / death
performan = (kda_score * level)

# 4. Display the result
print("=== STATS RESULT ===")
print("Player Name :", player_name)
print("Your Total KDA Score is:", kda_score)
print("Your Performan is:", performan)