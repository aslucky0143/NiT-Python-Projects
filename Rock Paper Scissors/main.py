import random as r
i=0
choices = ["Rock","Paper","Scissor"]
computer =r.choice(choices)
n=int(input("Enter number of rounds"))
while i<n:

  #Round Iteration
  print("\n\nRound",i+1,":")

  #player input
  player = int(input("Enter your choice:\n1 Rock\n2 Paper\n3 Scissors\nEnter your choice:"))
  while player!=1 and player!=2 and player!=3:
    print("\nIncorrect input\nTry Again\n")
    player = int(input("Enter your choice:\n1 Rock\n2 Paper\n3 Scissors\nEnter your choice:"))

  #Data assigment
  if player==1:
    player="Rock"
  elif player==2:
    player="Paper"
  elif player==3:
    player="Scissor"

  #data presentation
  print("\n\nComputer:",computer,"\nPlayer",player,"\n\n")

  #Result Anouncement
  if player==computer:
    print("It's a Draw\n")
  elif player=="Rock":
    if computer=="Paper":
      print("Computer wins\n")
    else:
      print("Player wins\n")
  elif player=="Paper":
    if computer=="Scissor":
      print("Computer wins\n")
    else:
      print("Player wins\n")
  elif player=="Scissor":
    if computer=="Rock":
      print("Computer wins\n")
    else:
      print("Player wins\n")
  i+=1
