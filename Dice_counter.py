#Roll the dice regularity counter
import random
serie=[]
print("This program will simulate n dice-rolls of n faces and return the percentage of a chosen streak of equal results.")
print("Avoid entering 0 or letteral values.")
print()
while True:
  rolls=int(input("Insert the number of dice-rolls: "))
  faces=int(input("How many faces has the dice?"))
  sequence=int(input("Insert the dimension of the streak of equal numbers you want to check: "))
  print()
  for i in range(rolls):
    a=random.randint(1,faces)
    serie.append(a)
  print("Rolls list:",serie)
  print()
  i=0
  counter=0
  bingo=0
  while i<rolls-1:
    if serie[i]==serie[i+1]:
      counter+=1
      i+=1
    else:
      i+=1
    if counter==sequence-1:
      bingo+=1
      counter=0
  print("There are:",bingo,"series of",sequence,"numbers.")
  print("The percentage of the streak is",bingo*100//rolls,"%.")
  print()
  a=input("Type 'end' to exit or 'again' to reload the program.")
  if a=="end":
    break
  else:
    continue
