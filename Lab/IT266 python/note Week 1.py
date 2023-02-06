# import math

# def manipData(ls):
#     for i in range(len(ls)):
#         if ls[i] % 2 == 1:
#             print(math.pow(ls[i],2))
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# manipData(a)

# def CelsiusConvertToFahrenheit(Celsius):
#     Fahrenheit = Celsius * 1.8 + 35
#     return Fahrenheit



# def main():
#     Celsius = int(input("Enter Celsius To Fahrenheit : "))
#     Fahrenheit = CelsiusConvertToFahrenheit(Celsius)
#     print(f"Celsius : {Celsius} °C To Fahrenheit : {Fahrenheit} °F" )
    
# if __name__ == "__main__":
#     main()

    
# def bmi(Height,Weight):
#     bmi = (Weight / (Height*Height))
#     if bmi < 18.5:
#         return bmi, "น้ำหนักต่ำกว่าเกณฑ์"
#     elif bmi <= 22.9:
#         return bmi, "สมส่วน"
#     elif bmi <= 24.9:
#         return bmi, "น้ำหนักเกิน"
#     elif bmi <= 29.9:
#         return bmi, "โรคอ้วน"
#     else:
#         return bmi, "โรคอ้วนอันตราย"
    
# def main():
#     Height = float(input("Enter Height(m) : "))
#     Weight = float(input("Enter Weight(kg) : "))
#     resultBMI , ms = bmi(Height,Weight)
#     print(f"BMI = {'{:.2f}'.format(resultBMI)} ,{ms}")
    
# if __name__ == "__main__":
#     main()
    

# def bmi(Height,Weight):
#     bmi = (Weight / (Height*Height))
#     if bmi < 18.5:
#         return bmi, "น้ำหนักต่ำกว่าเกณฑ์"
#     elif bmi <= 22.9:
#         return bmi, "สมส่วน"
#     elif bmi <= 24.9:
#         return bmi, "น้ำหนักเกิน"
#     elif bmi <= 29.9:
#         return bmi, "โรคอ้วน"
#     else:
#         return bmi, "โรคอ้วนอันตราย"
    
# def main():
#     Height = float(input("Enter Height(m) : "))
#     Weight = float(input("Enter Weight(kg) : "))
#     resultBMI , ms = bmi(Height,Weight)
#     print(f"BMI = {'{:.2f}'.format(resultBMI)} ,{ms}")
    
# if __name__ == "__main__":
#     main()

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a[0] = "2"
# print(a)
#<------------------------------------->

# Richter = float(input("Enter Richter : "))
# if Richter < 1:
#    print("Nothing")
# elif Richter >= 1.0 and Richter < 2.0:
#     print("Microearthquakes not felt or rarely felt")
# elif Richter >= 2.0 and Richter < 4.0:
#     print("Very rarely causes damage")
# elif Richter >= 4.0 and Richter < 5.0:
#     print("Damage done to weak buildings")
# elif Richter >= 5.0 and Richter < 6.0:
#     print("Cause damage to the poorly constructed building")
# elif Richter >= 6.0 and Richter < 7.0:
#     print("Causes damage to well-built structures")
# elif Richter >= 7.0 and Richter < 8.0:
#     print("Causes damage to most buildings")
# elif Richter >= 8.0 and Richter < 9.0:
#     print("Causes major destruction")
# else:
#     print("Causes unbelievable damage"

# n = int(input("Enter n Value : "))
# i = 1
# sum_a = 0
# sum_b = 0
# while i <= n:
#     sum_a = i + (1/n)
#     sum_b = i + (n**i/1)
#     i = i + 1
# print(f"sum_a : {sum_a}")
# print(f"sum_b : {sum_b}")

# start = int(input("Enter Number One : "))
# stop = int(input("Enter Number Two : "))
# all_up = 0
# for i in range(start, stop+1):
#     if start % 2 != 0:
#         all_up = all_up + start
#     start = start + 1
# print(all_up)
    
    

# number = int(input("Enter a number "))
# if number >= 0 :
#     print(f"The number entered by the user is a positive number")
  
# พิระมิ
# i = int(input("Enter Number : "))
# for x in range(1,i+1):
#   for y in range(x):
#     print ("*",end="")
#   print()
  
# number = int(input("Enter a number up to which you want to find the average"))
# i = 0
# sum = 0
# count = 0
# while i < number:
#     i = i + 1
#     sum = sum + i
#     count = count + 1
# average = sum / count
# print(f"The average of {number} natural numbers is {average}")  
  
  
# i = 1
# while i < 10:
#     print(f"Current value of i is {i}")
#     i = i + 1

  
    
# fruit_type = input("Enter the Fruit Type : ")
# if fruit_type == "Oranges":
#     print('Oranges are $0.59 a pound')
# elif fruit_type == "Apples":
#     print('Apples are $0.32 a pound')
# elif fruit_type == "Apples":
#     print('Apples are $0.32 a pound')
# elif fruit_type == "Apples":
#     print('Apples are $0.32 a pound')
    
    
# score = float(input("Enter your score")) 
# if score < 0 or score > 1:
#     print('wrong Input')
# elif score >= 0.9:
#     print('Your Grade is "A" ')
# elif score >= 0.8:
#     print('Your Grade is "B" ')
# elif score >= 0.7:
#     print('Your Grade is "C" ')
# elif score >= 0.6:
#     print('Your Grade is "D" ')
# else:
#     print('Your Grade is "F" ')
    
# print('Thank you')


# number_1 = int(input("Enter the first number : "))
# number_2 = int(input("Enter the second number : "))
# if number_1 > number_2:
#     print(f"{number_1} is greater than {number_2}")
# else:
#     print(f"{number_2} is greater than {number_1}")
    
# weight = int(input("How many pounds does your suitcase weigh? "))
# if weight > 50:
#     print(f"There is a $25 surcharge for heavy luggage")
#     print(f"Thank you")
    
# number = int(input("Enter a number : "))
# if number % 2 == 0:
#     print(f"{number} is Even number")
# else:
#     print(f"{number} is Odd number")