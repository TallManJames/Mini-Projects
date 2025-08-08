
shoppingCart = []

discountCode = "Kappy"
discountPercentOff = 10
discountMultiplier = 1 - (discountPercentOff/100)

regionalTax = 1.07

orangeCost = 5.99
appleCost = 4.97
bananaCost = 4.49
mangoCost = 6.49

print("Hello, welcome to the fruit store!")
print("P.S - Numerical Values Only\nAdditionally, we only have 100 items of each type of fruit.")

check = 0
while check == 0:
    print("\nHow many oranges would you like today?")
    orangeAmount = float(input())
    if (orangeAmount%1 != 0) or (orangeAmount<0) or (orangeAmount>100):
        print("Error, please enter valid number.")
    else:
        check += 1
        totalOrangeCost = orangeCost*orangeAmount
        shoppingCart.insert(0,totalOrangeCost)

while check == 1:
    print("\nHow many apples would you like today?")
    appleAmount = float(input())
    if (appleAmount%1 != 0) or (appleAmount<0) or (appleAmount>100):
        print("Error, please enter valid number.")
    else:
        check += 1
        totalAppleCost = appleCost*appleAmount
        shoppingCart.insert(1,totalAppleCost)

while check == 2:
    print("\nHow many bananas would you like today?")
    bananaAmount = float(input())
    if (bananaAmount%1 != 0) or (bananaAmount<0) or (bananaAmount>100):
        print("Error, please enter valid number.")
    else:
        check += 1
        totalBananaCost = bananaCost*bananaAmount
        shoppingCart.insert(2,totalBananaCost)

while check == 3:
    print("\nHow many mangos would you like today?")
    mangoAmount = float(input())
    if (mangoAmount%1 != 0) or (mangoAmount<0) or (mangoAmount>100):
        print("Error, please enter valid number.")
    else:
        check += 1
        totalMangoCost = mangoCost*mangoAmount
        shoppingCart.insert(3,totalMangoCost)

cartSubtotal = sum(shoppingCart)

discountStatus = False

print("\nDo you know the discout code? Answer yes or no")
discountCheck = input().lower()
if discountCheck == "yes":
    print("\nGreat! Guess the code below:")
    discountGuess = input()
    if discountGuess == discountCode:
        discountStatus = True
        print(f"\nCorrect! That is a {discountPercentOff}% off your purchase!")
    else:
        print("\nSorry, that is incorrect.")
else:
    if discountCheck == "no":
        print("\nOkay, then let's move on.")

if discountStatus == True:
    cartTotal = (cartSubtotal*discountMultiplier)*regionalTax
else:
    cartTotal = cartSubtotal*regionalTax

finalCost = round(cartTotal,2)

print(f"\nAlright! That brings your final total to ${finalCost}!")



print("\nAre you able to afford this???")
moneyCheck = input().lower()
q=0
while q < 1:
    if moneyCheck == "no":
        print("Mane, GET YO BROKE ASS OUTTA HERE!!!")
    else:
        if moneyCheck == "yes":
            q += 1
            print("\nGood... pay here:")