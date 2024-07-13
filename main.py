# Program to calculate the user's Body Mass Index (BMI) https://en.wikipedia.org/wiki/Body_mass_index

def main():
    measurement = 0

    while measurement != 1 and measurement != 2:
        measurement = int(input('What is your preferred method of measurement? Type 1 for metric or 2 for imperial.\n'))
        if measurement == 1:
            height = input("How tall are you? (in meters) e.g. 1.65\n")
            weight = input("How much do you weight (in kilograms) e.g. 72\n")

            bmi = round(float(weight) / float(height) ** 2, 2)

            if bmi < 18.5:
                print("Your BMI is " + str(bmi) + ", you are underweight.")
            elif bmi < 25:
                print("Your BMI is " + str(bmi) + ", you have a normal weight.")
            elif bmi < 30:
                print("Your BMI is " + str(bmi) + ", you are slightly overweight.")
            elif bmi < 35:
                print("Your BMI is " + str(bmi) + ", you are obese.")
            elif bmi >= 35:
                print("Your BMI is " + str(bmi) + ", you are clinically obese.")

        elif measurement == 2:
            height = input("How tall are you? (in inches, 1ft = 12 inches) ex: 66\n")
            weight = input("How much do you weight (in pounds) ex: 180\n")

            bmi = round((float(weight) / float(height) ** 2) * 703, 2)

            if bmi < 18.5:
                print("Your BMI is " + str(bmi) + ", you are underweight.")
            elif bmi < 25:
                print("Your BMI is " + str(bmi) + ", you have a normal weight.")
            elif bmi < 30:
                print("Your BMI is " + str(bmi) + ", you are slightly overweight.")
            elif bmi < 35:
                print("Your BMI is " + str(bmi) + ", you are obese.")
            elif bmi >= 35:
                print("Your BMI is " + str(bmi) + ", you are clinically obese.")

        else:
            print(f'"{measurement}"is an incorrect value. Must be "1" or "2".')


if __name__ == '__main__':
    main()
