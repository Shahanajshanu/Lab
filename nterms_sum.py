n = int(input("Enter the no.of terms: "))
x = int(input("Enter the values of x: "))
sum = 1
for i in range(2, n+1):
    sum = sum + ((x**i)/ i)
print("The sum of series", round(sum, 2))