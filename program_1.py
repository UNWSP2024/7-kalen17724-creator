# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

monthly_rainfall = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "Demcember"]

monthly_rainfall[0]= float(input("Enter how much rain there was in January: "))
monthly_rainfall[1]= float(input("Enter how much rain there was in february: "))
monthly_rainfall[2]= float(input("Enter how much rain there was in March: "))
monthly_rainfall[3]= float(input("Enter how much rain there was in April: "))
monthly_rainfall[4]= float(input("Enter how much rain there was in May: "))
monthly_rainfall[5]= float(input("Enter how much rain there was in June: "))
monthly_rainfall[6]= float(input("Enter how much rain there was in July: "))
monthly_rainfall[7]= float(input("Enter how much rain there was in August: "))
monthly_rainfall[8]= float(input("Enter how much rain there was in September: "))
monthly_rainfall[9]= float(input("Enter how much rain there was in October: "))
monthly_rainfall[10]= float(input("Enter how much rain there was in November: "))
monthly_rainfall[11]= float(input("Enter how much rain there was in December: "))


total_rain = sum(monthly_rainfall)
average_rain = (total_rain / 12)
least_rain = min(monthly_rainfall)
most_rain = max(monthly_rainfall)

def main():
    print (total_rain)
    print (average_rain)
    print (least_rain)
    print (most_rain)
    print ('All in inches')
    

main()
