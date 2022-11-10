def paintneeded(l, w, h,):
  sqfeet = (2*float(l)*float(w))+(2*float(w)*float(h))+(2*float(l)*float(h))
  galofpaint = sqfeet / 50
  return galofpaint
  
gate = str(input('Would you like to run this program? Yes or No?: '))
while gate == 'Yes':
  l = float(input("Enter length of room in feet: "))
  w = float(input("Enter width of room in feet: "))
  h = float(input("Enter height of room in feet: "))

  paint = paintneeded(l, w, h)
  print(paint, "gallons of paint needed")
  gate = str(input("Would you like to run this program again? Yes or No?: "))

print("Have a good day :)")
