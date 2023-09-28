def bmi(weight: int, height: float) -> str:
    bmi = weight / height ** 2
    print(bmi)
    return 'Underweight' if bmi <= 18.5 else 'Normal' if bmi <= 25.0 else 'Overweight' if bmi <= 30.0 else "Obese"


print(bmi(50, 1.82))
print(bmi(80, 1.79))
print(bmi(80, 1.65))
print(bmi(120, 1.95))
