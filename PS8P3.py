def outdoorprice(msrp):
  tax = float(msrp) * 0.07
  disc = float(msrp) * float(perc)
  odprice = float(msrp) - float(disc) + float(tax)
  return odprice

gate = str(input("Would you like to run this program? Yes or No?: "))

while gate == 'Yes':
  make = str(input("Enter make of vehicle: "))
  model = str(input("Enter model of vehicle: "))
  ev = str(input("Is the vehicle electric? Y or N: "))
  msrp = float(input("Enter MSRP value of the vehicle: "))
  if ev == "Y" and make == 'Honda' and model == 'Accord':
    perc = 0.40
  elif make == 'Honda' and model == 'Accord':
    perc = 0.10
  elif ev == "Y" and make == "Toyota" and model == "Rav4":
    perc = 0.45
  elif make == "Toyota" and model == "Rav4":
    perc = 0.15
  elif ev == "Y":
    perc = 0.30
  else:
    perc = 0.05

  price = outdoorprice(msrp)
  print("Out the door price is:", price)
  gate = str(input("Would you like to run this program again? Yes or No?: "))

print("Have a good day")
