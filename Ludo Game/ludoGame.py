import random as r
i=1
playerSum,computerSum=0,0

#Number of rounds of game
rounds=int(input("Enter the number of rounds:"))

typeOfGame = int(input("Enter the Game type:\n1 Total Result\n2 Instant Result\nEnter your choice:"))
#if the input is not with in given range
while typeOfGame!=1 and typeOfGame!=2:
  print("\nIncorrect input\nTry Again")
  typeOfGame = int(input("Enter the Game type:\n1 Total Result\n2 Instant Result\nEnter your choice:"))

while i<=rounds:
  
  #Round Iterator
  print("\nRound",i,":")
  player = int(input("Enter a number between 1 and 6:"))
  computer = r.randint(1,6)
  if player<=6 and player>=1:

    #Total Result Game
    if typeOfGame==1:
      playerSum+=player
      computerSum+=computer
      
      
    #Instant Result Game
    else:
      if computer > player:
        print("Computer wins") #if computer wins
      elif computer < player:
        print("Player wins") #if player wins
      else :
        print("it's a Draw")#if both are same
    
    i+=1#if player enter within range it will move to next round

  else:
    print("\nIncorrect input\nTry Again")

#Total Result Game
if typeOfGame==1:
  if playerSum>computerSum:
    print("Player wins")
  elif playerSum<computerSum:
    print("Computer wins")
  else:
    print("It's a Draw")