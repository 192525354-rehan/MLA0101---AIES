
age = int(input("Enter age: "))
bmi = float(input("Enter BMI: "))
condition = input("Enter health condition (normal/diabetes): ").lower()

print("\nRecommended Diet Plan:")

if age < 18:
    print("Consult a qualified dietitian for an age-appropriate diet.")

elif condition == "diabetes":
    print("Diet: Balanced meals with high-fiber foods.")
    print("Avoid sugary drinks and limit refined carbohydrates.")

elif bmi >= 25:
    print("Diet: Balanced meals with vegetables and whole grains.")
    print("Include suitable portions of protein and healthy fats.")

else:
    print("Diet: Balanced diet with fruits, vegetables, grains and protein.")

print("Drink water regularly and maintain regular meal timings.")
