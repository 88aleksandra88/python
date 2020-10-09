#We will store the two teams in a list, check if they have the same length, then display the rounds left based on the length.

team_1 = ["Mia","Lisa","Lenny"]
team_2 = ["Bonjo","harley","Ava"]
size_1 = len(team_1)
size_2 = len(team_2)

if size_1 != size_2:
  print("Teams must have the same size!")
else:
  print("Game on!")

/#rounds left
if size_1 == 3:
  print("Rounds left: 3")
elif size_1 == 2:
  print("Rounds left: 2")
else:
  print("Final round!")