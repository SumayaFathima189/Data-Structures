#Armstrong: sum of cubes of digits = number itself
#Takes a 3-digit number from the user
number = int(input("Enter the number-"))
nofdigits = len(str(number))
temp = number
resultnumber = 0

# Example: 153 → 1³ + 5³ + 3³ = 153 
while temp>0:
    digit = temp%10 #extracts the last digit from number
    resultnumber += digit**nofdigits #number is raised by the number of digits
    temp//=10 #excutes until temp=0

#Checks if it’s an Armstrong number    
if number == resultnumber:
    print("It is a ArmStrong Number")
else:    
    print("It is not a ArmStrong Number")