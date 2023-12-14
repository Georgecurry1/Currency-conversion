#this will be a test for general functionality of the idea. lets start off with a menu in cmd
#define constant conversion ammounts (got these rates from google)
PesoValue = 0.058
EuroValue = 1.09
YenValue = 0.0070
CanadianDollarValue = 0.74

#define functions
def conversionToPesos(amount):
    return amount * PesoValue

def conversionToEuro(amount):
    return amount * EuroValue
    
def conversionToYen(amount):
    return amount * YenValue
    
def conversionToCanadianDollar(amount):
    return amount * CanadianDollarValue 

    
#program start
print("!***Currency Conversion***!\n")
print("This will default as USD for base comparsion\n")
print("Chose which currency you want to convert to; Press the corrosponding key")

print("1. Pesos\n")
print("2. Euro\n")
print("3. Yen\n")
print("4. Canadian dollar\n")

menuChoice = int(input())

while menuChoice < 0 or menuChoice > 4:
    print("Invalid entry, please try again")
    menuChoice = int(input())
    
    if menuChoice == 1:
        print("Please type how many dollars you want to convert. Please no commas or spaces.")
        amount = int(input())
        conversionToPesos(amount)
        