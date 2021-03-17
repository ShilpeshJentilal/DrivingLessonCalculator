#Shilpesh Jentilal
#Calculator for Driving Lessons
import subprocess
import time

#________Welcome Message_________#

print("===Welcome to My Driving Lesson Calculator===") # welcome message is displayedfirst when you run the program
print("In order to find out the cost of lessons. Please provide the following required information below.")


#________This will ask for Firt name_________#

while True:
    fname= input("Enter your First Name:")
    if (len(fname) >2 and fname.isalpha())==False:
        print("Error- Must be letter")
        subprocess.call("pythonW helpfirstname.py")#will ask for first name if the input is numbers or length is less than 2
    else:
        print("")
        break

#________This will ask for Last name_________#
while True:
    Lastname= input("Enter your Surname:")#variable for Lastbane
    if (len(Lastname) >2 and Lastname.isalpha())==False:
        print("Error- Must be Letters")
        subprocess.call("pythonW helpfirstname.py")#will ask for Last name if the input is numbmers or length is less than 2
    else:
        print("Your Full name is",fname.title(), Lastname.title(),"\n")#print First name and Lastname
        break

#________This will ask for House number_________#
while True:
    try:
        housenumber=int(input("Enter your House Number:"))
    except ValueError:
        print("Error- Must be a Number")
        subprocess.call("pythonW helpfirstname.py")#will ask for house number if the input length is not numbers
    else:
        print("")
        break
    
#________This will ask for Address_________#
while True:
    Address= input("Enter your first line of Address:")
    if len(Address) <6:
        print("Error- Length must be 6 or more")
        subprocess.call("pythonW helpfirstname.py")#will ask for Address if the input length is less than 6
    else:
        print("")
        break
#________This will ask for Postcode_________#
while True:
    Postcode= input("Enter Postcode:")
    if len(Postcode)!=6:
        print("Length must be 6 and without any spaces")
        subprocess.call("pythonW helpfirstname.py")#will ask for Postcode if the input length is not equal to 6
    else:
        print("your full address is",housenumber,Address.title(),Postcode.upper()) #prints Full address with postcode
        break


#________This will ask for Date of Birth_________#
print("Please Enter your Date of Birth")
while True:
    try:
        Day= int(input("Day(dd):"))
    except ValueError:
        print("must be a number")
        continue
    else:
        if Day in range (1,31):
            if Day>1:
                print("")
                break
            else:
                print("")
                break
        else:
            print("must be between 1 and 31")
            continue
while True:
    try:
        Month= int(input("Month(mm):"))
    except ValueError:
        print("must be a number")
        continue
    else:
        if Month in range (1,13):
            if Month>1:
                print("")
                break
            else:
                print("")
                break
        else:
            print("must be between 1 and 12")
            continue
while True:
    try:
        Year= int(input("Year(yyyy):"))
    except ValueError:
        print("must be a number")
        continue
    else:
        if Year in range (1000,2003):
            if Year>1000:
                print("")
                break
            else:
                print("")
                break
        else:
            print("must be over 18")
            continue
Age=(2020-Year)

#________This will ask for date of provisional driving license issued________#
print("Please Enter your Date of Provisional Driving License issued")
while True:
    try:
        pDay= int(input("Day(dd):"))
    except ValueError:
        print("must be a number")
        continue
    else:
        if pDay in range (1,31):
            if pDay>1:
                print("")
                break
            else:
                print("")
                break
        else:
            print("must be between 1 and 31")
            continue
while True:
    try:
        pMonth= int(input("Month(mm):"))
    except ValueError:
        print("must be a number")
        continue
    else:
        if pMonth in range (1,13):
            if pMonth>1:
                print("")
                break
            else:
                print("")
                break
        else:
            print("must be between 1 and 12")
            continue
while True:
    try:
        pYear= int(input("Year(yyyy):"))
    except ValueError:
        print("must be a number")
        continue
    else:
        if pYear in range (1000,2021):
            if pYear>1000:
                print("")
                break
            else:
                print("")
                break
        else:
            print("You still living in 2020")
            continue
        

    
#________This will ask for number of lessons and will display cost of lessons booked_________#
while True:
    try:
        lessons = int(input("How many lessons are you booking?")) #ask for how many lesson they want to book
    except ValueError: #catch no data entry
        print ("please type a number") #displays this if input is not a number
        continue
    else:
        if lessons in range (1,31):
            if lessons <10:
                price=20 #if less than 10 lessons are booked, then the cost of each lesson will be 20
                break
            else:
                price=18#if more than 10 lessons are booked, then the cost of each lesson will be 18
                break
        else:
            print("please enter a number between 1 and 31")#displays this if input is not in range of 1 to 31
            continue

print("Generating a Quote for you. Please Wait.")
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")
time.sleep(1)
#________This Display full information provided from customer________#

print("==============================================================")
print("Customer Information")
print("Name:",fname.title(), Lastname.title())
print("Full Address:",housenumber,Address.title(),Postcode.upper())
print("Date of Provisional Driving License issued:",pDay,"/",pMonth,"/",pYear)
print("DOB:",Day,"/",Month,"/",Year)
print("Age:",Age)
print ("Your lessons will cost","£",lessons*price) #displays total cost of lessons booked


#_______This will diplay at the end_______#
print ("Thank your for using our booking system \n")
time.sleep(10)


