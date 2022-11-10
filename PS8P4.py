gate = str(input("Would you like to run this program? Yes or No?: "))
totprice = 0
while gate == "Yes":
  miles = float(input("Enter miles from Chicago: "))
  def ticket(miles):
    if miles <=19 and miles >= 10:
      price = 8.00
    elif miles >= 20 and miles <= 29:
      price = 10.00
    elif miles >= 30:
      price = 12.00
    else:
      price = 5.00
    return price
  price = ticket(miles)
  print("Ticket price:", price)
  totprice = totprice + price
  gate = str(input("Would you like to run this program agian? Yes or No?: "))

print("Total ticket price:", totprice)
print("Have a good day :)")
