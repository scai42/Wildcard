import random
import matplotlib
import matplotlib.pyplot as plt

print("WELCOME TO THE CASINO!")
print("   ____ ")
print("  /\* *\    _____ ")
print(" /* \___\  / *  /\ ")
print(" \  / * / /____/**\ ")
print("  \/___/  \*  *\  / ")
print("           \*__*\/ ")
print("today, EARN 1 dollar for each dollar placed on the 100-sided dice / wheel game. ")
def Monte_carlo_dice():
  result = random.randint(1, 100)
  if result <= 50:
      return False
  elif result == 100:
      return False
  elif 100 > result > 50:
      return True

# The Basic Bettor leverages the same amount each time
def Basic_bettor(funds,first_bet,bet_count):
  capital = funds
  bet = first_bet
# wage X and Y
  betX = []
  valueY = []
# Although computers start at ZERO (remember this!), the general population tends to start indexing at 1... 
  current_bet = 1
  while current_bet <= bet_count:
    if Monte_carlo_dice():
      capital += bet
      betX.append(current_bet)
      valueY.append(capital)
    else:
      capital -= bet
      betX.append(current_bet)
      valueY.append(capital)
    current_bet += 1
    plt.plot(betX,valueY)

funds_txt = input("Enter the number of funds you brought today: ")
init_funds = int(funds_txt)
first_txt = input("Enter amount you wish to bet per dice roll: ")
first_bet = int(first_txt)
iter_txt = input("Enter the number of bets you wish to make based on the previous two responses: ")
iterations = int(iter_txt)
while iterations < 100:
  Basic_bettor(init_funds, first_bet, iterations)
  iterations += 1

plt.ylabel('Account Value')
plt.xlabel('Bets Made')
plt.show()