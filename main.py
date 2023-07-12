print("Welcome to the Quidditch Statistics Calculator\n")
print("Enter the teams, scores, and time to make it work.  It's like magic!\n")
win_team = input("What is the name of the team that caught the snitch?\n")
lose_team = input("What is the name of the other team?\n")
print("")
win_score = int(input("What is the final score of the team who caught the snitch?\n"))
lose_score = int(input("What is the final score of the other team?\n"))
print("")
game_time = int(input("How long did the game last in minutes?\n"))
print("")
goals_win_team = (win_score - 150)/10.0
win_gpm = '{:.2f}'.format(goals_win_team/game_time)

goals_lose_team = lose_score/10.0
lose_gpm = '{:.2f}'.format(goals_lose_team/game_time)

print(win_team, "Team Statistics")
print("Goals: ", goals_win_team)
print("Snitch:  1")
print("Goals per Minute:", win_gpm)
print("")
print(lose_team, "Team Statistics")
print("Goals: ", goals_lose_team)
print("Snitch:  0")
print("Goals per Minute:", lose_gpm)