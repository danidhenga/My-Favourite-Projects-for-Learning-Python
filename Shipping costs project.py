#SHIPPING PROJECT - FIND THE CHEAPEST METHOD FOR A GIVEN PRICE!
"""
Sal's Shipping

Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages. In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package. They have ground shipping, which is a small flat charge plus a rate based on the weight of your package. Premium ground shipping, which is a much higher flat charge, but you aren’t charged for weight. They recently also implemented drone shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Here are the prices:

Ground Shipping
Weight of Package 	Price per Pound 	Flat Charge
2 lb or less 	$1.50 	$20.00
Over 2 lb but less than or equal to 6 lb 	$3.00 	$20.00
Over 6 lb but less than or equal to 10 lb 	$4.00 	$20.00
Over 10 lb 	$4.75 	$20.00




Drone Shipping
Weight of Package 	Price per Pound 	Flat Charge
2 lb or less 	$4.50 	$0.00
Over 2 lb but less than or equal to 6 lb 	$9.00 	$0.00
Over 6 lb but less than or equal to 10 lb 	$12.00 	$0.00
Over 10 lb 	$14.25 	$0.00




Premium Ground Shipping

Flat charge: $125.00

Write a program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.
"""

def ground_shipping(weight):
  if 22.5 > weight >= 10:
    return weight * 4.75 + 20
  elif 10 > weight >= 6:
    return weight * 4.00 + 20
  elif 6 > weight >= 2:
    return weight * 3.00 + 20
  elif weight < 2:
    return weight * 1.50 + 20
  else:
    return 125

def drone_shipping(weight):
  if weight >= 10:
    return weight * 14.25
  elif weight >= 6:
    return weight * 12.00
  elif weight >= 2:
    return weight * 9.00
  else:
    return weight * 4.50

def print_cheaper_method(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)

  if ground < drone:
    method = "ground ('premium' if total is more than $125)"
    cost = ground
  else:
    method = "drone"
    cost = drone

  print(
    "The cheapest option costs $%.2f with %s shipping. "
  % (cost, method))

print_cheaper_method(4.8)
print_cheaper_method(41.5)
