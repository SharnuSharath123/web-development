n = int(input("Enter a year : "))
#for i in range(10, 10):
if n % 400 == 0 or (n % 4 == 0 and n % 100!= 0):
    print("Leap year")
else:
    print("Not a leap year")

def is_leap(year):
    leap = False
    if year % 4 == 0 or (year % 400 == 0 and year % 100 != 0):
        leap=True
        print("True")
    else:
        leap=False
        print("False")
        
    return leap

year = int(input("Enter a year : "))