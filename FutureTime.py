#FutureTime.py
#Name: Erick Andres
#Date:01/02/2026
#Assignment:Lab 2
#Purpose: The purpose of this lab is to write a program that asks the user for hours and minutes and displays the future time in HH:MM format.

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 8) % 24
  currentMinute = now.minute 

  #Ask user for hours
  hours= int(input("What's your time in hours? :"))
  #Ask user for minutes
  minutes= int(input("What's your time in minutes? :"))
  

  #Calculate the time after the user-supplied time has passed
  #Do not use any if statements in calculating the time.
  futureMinute = (currentMinute + minutes ) % 60 
  extraHour = (currentMinute + minutes ) // 60
  futureHour =(currentHour +hours + extraHour) % 24
  

  #Output the future time in standard format "HH:MM"
  print(f"Future time is {futureHour}:{futureMinute:02d}")

if __name__ == '__main__':
  main()
