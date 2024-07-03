from fractions import Fraction

# Function to add two fractions
def add_fractions(frac1, frac2):
    # Add the fractions directly using the Fraction class
    result_frac = frac1 + frac2
    return result_frac

# Taking input from the user
num1 = int(input("Enter the numerator for the first fraction: "))
denom1 = int(input("Enter the denominator for the first fraction: "))
num2 = int(input("Enter the numerator for the second fraction: "))
denom2 = int(input("Enter the denominator for the second fraction: "))

# Creating Fraction instances
fraction1 = Fraction(num1, denom1)
fraction2 = Fraction(num2, denom2)

# Adding fractions
result_fraction = add_fractions(fraction1, fraction2)

# Displaying the result
print("Result of adding fractions:", result_fraction)
