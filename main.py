spaargeld = int(input("Hoeveel spaargeld heb je?"))
scooter = 1500

if scooter - spaargeld > 500:
  print("Je kunt beter een baantje gaan zoeken")
elif scooter - spaargeld <= 0:
  print("Je hebt geld genoeg om de scooter te kopen!")
else:
  print("Je hebt bijna geld genoeg, er is nog een klein beetje tekort")