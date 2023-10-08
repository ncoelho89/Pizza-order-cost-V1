print("Thank you for choosing Pyzzon Pizza!")
size = input("What size pizza do you want? S, M, or L\n")
add_pepperoni = input("Do you want to add pepperoni for an extra cost? Y or N\n")
extra_cheese = input("Do you want extra cheese for an additional cost? Y or N\n")

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S"
    bill += 2
  else:
      bill += 3
    
if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is ${bill})








