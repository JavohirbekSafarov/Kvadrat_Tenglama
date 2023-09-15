import math

a = float(input("Koefitsentni kiriting a: "))
b = float(input("Koefitsentni kiriting b: "))
c = float(input("Koefitsentni kiriting c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"X1 = {x1}, X2 = {x2}")
elif discriminant == 0:
    x = -b / (2 * a)
    print(f"yagona ildiz: {x}")
else:
    realPart = -b / (2*a)
    imaginaryPart = math.sqrt(-discriminant) / (2*a)
    print(f"Complex ildizlar: {realPart} + {imaginaryPart}i va {realPart} - {imaginaryPart}i")
