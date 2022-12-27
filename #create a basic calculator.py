
#list league of legends ranks starting from Bronze 4 to Diamond 1, each rank starts at 0lp and ends at 100 lp this is constant for all ranks, once user reachers 100 lp they will be promoted to the next rank and start at 0 lp again and so on until they reach their desired rank and 100 lp in that rank
#list of ranks
ranks = ["Bronze 4", "Bronze 3", "Bronze 2", "Bronze 1", "Silver 4", "Silver 3", "Silver 2", "Silver 1", "Gold 4", "Gold 3", "Gold 2", "Gold 1", "Plat 4", "Plat 3", "Plat 2", "Plat 1", "Diamond 4", "Diamond 3", "Diamond 2", "Diamond 1"]
#list of lp
lp = [0, 100]
#ask user for their current rank and lp
current_rank = input("What is your current rank? ")
current_lp = int(input("What is your current lp? "))
#ask user for their desired rank and lp
desired_rank = input("What is your desired rank? ")
desired_lp = int(input("What is your desired lp? "))
#ask user for their win rate in percentage and convert it to a decimal number for calculations later on in the program 
win_rate = float(input("What is your win rate in percentage? ")) / 100 
#ask the user for their average LP gains per win and average LP losses per loss as a wholenumber 
average_lp_gains = int(input("What is your average LP gains per win? "))
average_lp_losses = int(input("What is your average LP losses per loss? "))
#calculate the number of games needed to play to reach desired rank and lp 
games_needed = ((ranks.index(desired_rank) - ranks.index(current_rank)) * 100 + (desired_lp - current_lp)) / (average_lp_gains * win_rate + average_lp_losses * (1 - win_rate))
#calculate the number of wins needed to reach desired rank and lp
wins_needed = games_needed * win_rate
#calculate the number of losses needed to reach desired rank and lp
losses_needed = games_needed * (1 - win_rate)
#calculate the number of days needed to reach desired rank and lp
days_needed = games_needed / 10
#print to the user number of games needed to reach desired rank and lp
print("You need to play " + str(games_needed) + " games to reach your desired rank and lp.")    



