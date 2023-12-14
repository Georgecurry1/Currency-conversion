#this will be a test for general functionality of the idea. lets start off with a menu in cmd
#define constant conversion ammounts (got these rates from google)
PesoValue = 0.058
EuroValue = 1.09
YenValue = 0.0070
CanadianDollarValue = 0.74

#define functions
def conversionToPesos(amount):
    return amount / PesoValue

def conversionToEuro(amount):
    return amount / EuroValue
    
def conversionToYen(amount):
    return amount / YenValue
    
def conversionToCanadianDollar(amount):
    return amount / CanadianDollarValue 

    
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
    
if menuChoice == 1: #Peso
        print("Please type how many dollars you want to convert. Please no commas or spaces.")
        amount = int(input())
        Converted_amount = conversionToPesos(amount)
        print("Your "+ str(amount)+ " dollar(s) are equal to "+ str(Converted_amount) + " Pesos!")
        
    
if menuChoice == 2: #Euro
        print("Please type how many dollars you want to convert. Please no commas or spaces.")
        amount = int(input())
        Converted_amount = conversionToEuro(amount)
        print("Your "+ str(amount)+ " dollar(s) are equal to "+ str(Converted_amount) + " Euros!")
        
    
if menuChoice == 3: #Yen
        print("Please type how many dollars you want to convert. Please no commas or spaces.")
        amount = int(input())
        Converted_amount = conversionToYen(amount)
        print("Your "+ str(amount)+ " dollar(s) are equal to "+ str(Converted_amount) + " Yen!")
        
    
if menuChoice == 4: #Canadian Dollars
        print("Please type how many dollars you want to convert. Please no commas or spaces.")
        amount = int(input())
        Converted_amount = conversionToCanadianDollar(amount)
        print("Your "+ str(amount)+ " dollar(s) are equal to "+ str(Converted_amount) + " Canadian Dollars!")
        