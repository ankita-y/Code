#Python BMI Calculator Coding Challenge
import json

BMIFile = open('BMIData.json',)
BMIData = json.load(BMIFile)
BMIMass = []
count_OverWeight = 0
bmi_category = ""
health_risk = ""

# To calculate the BMI Mass of the patients and based on BMIMass finding BMI category
for data in BMIData:
    HeightM = data['HeightCm'] * 0.01
    mass = round(data['WeightKg']/(HeightM*2),2)
    BMIMass.append(mass)
    if mass <= 18.4:
        bmi_category = "Underweight"
        health_risk = "Malnutrition risk"
    elif 18.5 <= mass <= 24.9:
        bmi_category = "Normal weight"
        health_risk = "Low risk"
    elif 25 <= mass <= 29.9:
        bmi_category = "Overweight"
        health_risk = "Enhanced risk"
        count_OverWeight += 1
    elif 30 <= mass <= 34.9:
        bmi_category = " Moderately obese"
        health_risk = "Medium risk"
        count_OverWeight += 1
    elif 35 <= mass <= 39.9:
        bmi_category = "Severely obese"
        health_risk = "High risk"
        count_OverWeight += 1
    elif mass >= 40:
        bmi_category = "Very severely obese"
        health_risk = "Very high risk"
        count_OverWeight += 1
    print("Gender: {0}\tBMI Mass: {1}\tBMI Category: {2}\tHealth Risk: {3}".format(data['Gender'],mass,bmi_category,health_risk))

print("Total number of Overweight patients:", count_OverWeight)

BMIFile.close()