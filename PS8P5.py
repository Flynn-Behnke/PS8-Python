gate = str(input("Would you like to run this program? Yes or No?: "))

totmvalue = 0
totavalue = 0
while gate == "Yes":
  mvalue = float(input("Enter market value: "))
  county = str(input("Enter county: "))
  def avalue(mvalue):
    if county == "Cook":
      avp = 0.9
    elif county == "DuPage":
      avp = 0.8
    elif county == "McHenry":
      avp = 0.75
    elif county == "Kane":
      avp = 0.6
    else:
      avp = 0.7
    avalue = mvalue * avp
    return avalue
  avalue = avalue(mvalue)
  totmvalue = totmvalue + mvalue
  totavalue = totavalue + avalue
  print("Market value:", mvalue)
  print("Assessed value:", avalue)
  gate = str(input("Would you like to run this program again? Yes or No? "))


print("Total market values:", totmvalue)
print("Total assesed values:", totavalue)
print("Have a good day :)")
