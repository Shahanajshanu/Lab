def cel_far():
    celsius = float(input("Enter a temperature in celsius: "))
    fahrenheit = 9.0 / 5.0 * celsius + 32
    print("Temperature: ", celsius, "Celsius: ", fahrenheit, "F")

def far_cel():
    fahrenheit = float(input("Enter a temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    print("Temperature: ", fahrenheit, "Fahrenheit: ", celsius, "C")

print("Menu\n"
      "1. Celsius to Fahrenheit\n"
      "2. Fahrenheit to Celsius\n"
)

x = float(input("Enter whether 1st option or 2nd: "))
if x == 1:
    cel_far()
elif x == 2:
    far_cel()    