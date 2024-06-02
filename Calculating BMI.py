print(f'''
_________________________________________
************** WELCOME  TO **************
   Body Mass Index Calculating Program
-----------------------------------------
''')
n=input("Enter your name:")
age=float(input("Enter your age in year:"))
gen=input("Enter you gender(press F for female and M for male and T for other):")
if gen.upper()== 'F':
   print(f"Welcome Miss {n} !!")
elif gen.upper()== 'M':
   print(f"Welcome Mr {n} !!")
else:
   print(f"Invalid input for gender. Please restart.")

print(f"Enter your body blood pressure in mmHg:")
sys=float(input("Systolic pressure:"))
dias=float(input("Diastolic pressure:"))

temp=float(input("Enter your body temperature:"))
ut=input("Enter the unit of your body temperature(press C for celsius and F for fahrenheit):")
if ut.upper()== 'C':
   t = temp*33.8
elif ut.upper()== 'F':
   t = temp*1
else:
   print(f"Invalid input for temperature unit. Please restart.")

sug=float(input("Enter your blood suger test in mg/dl:"))

uw=input("Enter the unit of weight(press L for lbs and K for kg:")
w=float(input("Enter your weight:"))
if uw.upper()== 'L':
   w_result = w*0.45
elif uw.upper()== 'K':
   w_result = w*1
else:
   print(f"Invalid input for weight unit. Please restart.")


uh=input("Enter the unit of hight(press F for foot and I for inch):")
h=float(input("Enter your hight:"))
if uh.upper()== 'F':
   h_result = h*0.3048
elif uh.upper()== 'I':
   h_result = h*0.0254
else:
   print(f"Invalid input for hight unit. Please restart.")

bmi = w_result/(h_result**2)


print("-----YOUR MEDICAL REPORT IS READY-----")

print(f"\nYour Body Mass Index is: {float(bmi)} kg/m^2")
print(f"Your BMI report is:")
if bmi<18.5:
   print(f"You are Under weight.")
elif 18.4<=bmi<=24.5:
   print(f"Normal.")
elif 25<=bmi<=29.9:
   print(f"You are over weight")
elif 30<=bmi<=34.9:
   print(f"Obesity Class I.")
elif 35<=bmi<=39.9:
   print(f"Obesity ClassII")
elif bmi>=40:
   print(f"Extreme Obesity")

print(f"Blood Pressure Report:")
if  sys>= 140 or dias>=90:
   print(f"You have a high blood pressure.")
elif  sys<=90 or dias<=60:
   print(f"You have a low pressure.")
else:
   print(f"You have a normal blood pressure.")

print(f"Temperature Report:")
if t>107:
   print(f"You have Hyperpyrexia.")
elif t > 99:
   print(f"You are Febrile.")
elif 98<=t<=99:
   print(f"You have a normal temperature.")
elif t<98:
   print(f"You are Subnormal.")
else:
   print(f"You have Hypothermia.")

print(f"Diabetic Report:")
if 1<=sug<=99:
   print(f"Normal.")
elif 100<=sug<=125:
   print(f"Prediabetes.")
elif sug<=126:
   print(f"Diabetes.")
else:
   print(f"Invalid input.")