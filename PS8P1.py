def salefc(sales, fcp):
  forecast = float(sales)*(1 + float(fcp))
  return forecast

gate = str(input('Run program? "Yes" or "No": '))
while gate == 'Yes':
  lastname = str(input("Enter last name: "))
  month = str(input("Enter the month (First three letters): "))
  sales = float(input("Enter this month's sales: "))
  if month == 'Jan' or month == 'Feb' or month == 'Mar':
    fcp = 0.10
  elif month == 'Apr' or month == 'May' or month == 'Jun':
    fcp = 0.15
  elif month == 'Jul' or month == 'Aug' or month == 'Sep':
    fcp = 0.20
  elif month == 'Oct' or month == 'Nov' or month == 'Dec':
    fcp = 0.25

  saleforecast = salefc(sales, fcp)
  print("Next month's sales:", saleforecast)
  gate = str(input('Run program again? "Yes" or "No": '))


print("Have a good day")
