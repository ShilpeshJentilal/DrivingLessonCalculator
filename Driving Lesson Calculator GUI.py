#Shilpesh Jentilal
#Driving Lesson Calculator GUI
from tkinter import *
from tkinter import messagebox
import time

#Function which the price of each lesson
def find_cost():
    global price
    if v_cost.get()<10:
        price= 20# if lessons are less than 10 price of each lesson will cost 20
    else:
        price= 18# if lessons are more than 10 price of each lesson will cost 18
        
    global TotalCost
    TotalCost= v_cost.get()*price# calcualtes the cost
    
#new window pops up and shows total cost of lessons booked
def show_cost():
    master1=Toplevel(master)
    master1.geometry("420x400+0+0")
    master1.title("Total Cost")
    master1.configure(bg="lightblue")
    find_cost()
    #Label for showing cost and heading
    Label(master1,text="Coché", bg="lightblue", fg="black", font="gray14 35 bold").grid(row=0,column=1, sticky=E)
    Label(master1,text="Driving", bg="lightblue", fg="black", font="gray14 35 bold").grid(row=0,column=1, sticky=N)
    Label(master1,bg="lightblue",text=("£",TotalCost),fg="black",font="none 18 bold").grid(row=2,column=0,sticky=W)
    Label(master1,bg="lightblue",text=("is total cost"),fg="black",font="none 18 bold").grid(row=2,column=0,sticky=E)
    Label(master1,bg="lightblue",text="of your lessons",fg="black",font="none 18 bold").grid(row=2,column=1,sticky=E)
    #Adding a picture  
    logo1= Canvas(master1,bg="lightblue", width = 210, height = 150)      
    img1 = PhotoImage(file="Logo1.png")      
    logo1.create_image(0,0, anchor=NW, image=img)
    logo1.grid(row=0, column=0)
    #Label and Button to find out the Cost
    Label(master1,bg="lightblue",text="Thank you for using driving\ncoche lesson calculator!",fg="green",font="none 10 bold").grid(row=3,column=1)
    Label(master1,bg="lightblue",text="\n",fg="white",font="none 8 bold").grid(row=4,column=0,sticky=E)
    Button(master1,width=15, text='Get \nanother Quote\n',font="none 14 bold", command=master1.destroy,bg="green").grid(row=14, column=0, sticky=E)
    Label(master1,text="\n\n\n",font="none 16 bold",bg="lightblue").grid(row=14, column=0, sticky=E)
    Button(master1,width=15, text='\nClose\n', font="none 14 bold",command=exit1, bg="red").grid(row=14,column=1, sticky=E)

def P_less():
    if v_pyear.get()<v_year.get():
        messagebox.showinfo("Error","your year of provisional license issued is wrong!")
    else:
        show_cost()


def Number_lessons():
    if v_cost.get()==0:#if lessons not selected error will pop up
        messagebox.showinfo("Error","Please Select Number of Lessons you would like to book")
    else:
        P_less()
        
        


#===============================================================================================   
#This Validates Date ofProvisional License issued   
#Error message pops up
def PYear_len():
    if v_year.get()== "Year":
        messagebox.showinfo("Error","Please Select Year of your Provisional License issued")
    else:
        Number_lessons()

#Error message pops up        
def PDate_check():
    if v_pday.get()=="Day": # if Day or month not selected error will pop up
        messagebox.showinfo("Error","Please Select Day of your Provisional License issued")
    elif v_pmonth.get()=="Month":
        messagebox.showinfo("Error","Please Select Month of your Provisional License issued")
    else:
        PYear_len()


#================================================================================================        
#This Validats Date of Birth        
#Error message pops up
def BYear_len():
    if v_year.get()=="Year":
        messagebox.showinfo("Error","Please Select Year of your Provisional License issued")
    else:
        PDate_check()
#Error message pops up
def DOB_Check():
    if v_day.get()=="Day":# if Day or month not selected error will pop up
        messagebox.showinfo("Error","Please Select Day of your Birth")
    elif v_month.get()=="Month":
        messagebox.showinfo("Error","Please Select Month of your Birth")
    else:
        BYear_len()



#Error message pops up 
def Validation_check():
    if (len(v_fname.get()) >2 and v_fname.get().isalpha())== False:
        messagebox.showinfo("Error","Please Check your First Name(Must be Characters only!)")#if user enters number and length of first name is 2 or less, error pops up 
    elif (len(v_lname.get()) >2 and v_lname.get().isalpha())== False:
        messagebox.showinfo("Error","Please Check your Last Name")#if user enters number and length of first name is 2 or less, error pops up
    elif v_hno.get().isdigit()== False:
        messagebox.showinfo("Error","Please Check your House Number(Must be a Numbers only!)")#if user enters number and length of first name is 2 or less, error pops up
    elif len( v_address.get())<6 :
        messagebox.showinfo("Error","Please Check your Address")#if user enters number and length of first name is 2 or less, error pops up
    elif len(v_postcode.get()) !=6:
        messagebox.showinfo("Error","Please Check your Postcode (length must be 6 without spaces)")#if user enters number and length of first name is 2 or less, error pops up
    else:
        DOB_Check()

#terminates the program
def exit1():
    exit()
    


#Main
def Main():
    global master
    global img
    global logo
    global PhotoImage
    
    master = Tk()
    master.geometry("400x720+0+0")
    master.title("Driving Coché")
    master.configure(bg="lightblue")

    #Adding a picture  
    logo= Canvas(master,bg="lightblue", width = 170, height = 150)
    logo.pack()      
    img = PhotoImage(file="Logo1.png")      
    logo.create_image(0,0, anchor=NW, image=img)
    logo.grid(row=0, column=0)
    #Label of Company's Name
    Label(master,text="Coché", bg="lightblue", fg="black", font="gray14 35 bold").grid(row=0,column=1, sticky=E)
    Label(master,text="Driving", bg="lightblue", fg="black", font="gray14 35 bold").grid(row=0,column=1, sticky=N)
#globalising variables so it can be used in different functions
    global v_fname
    global v_lname
    global v_hno
    global v_address
    global v_postcode
    global v_dob
    global v_day
    global v_year
    global v_month
    global v_pday
    global v_pmonth
    global v_pyear
    global v_cost
    
    v_fname= StringVar()
    v_lname =StringVar()
    v_hno= StringVar()
    v_address = StringVar()
    v_postcode=StringVar()  
    v_day= StringVar()
    v_month=StringVar()
    v_year=StringVar()
    v_pday= StringVar()
    v_pmonth=StringVar()
    v_pyear=StringVar()
    v_cost=IntVar()

    #Label and Entry box for First name
    e1=Label(master,text="First Name :", bg="lightblue", fg="black", font="none 13 bold").grid(row=2)
    e1= Entry(master,width=30,bg="lightblue",textvariable=v_fname).grid(row=2, column=1, sticky=W)
    #Label and Entry box for Last name
    e2=Label(master,text="Last Name :", bg="lightblue", fg="black", font="none 13 bold").grid(row=3)
    e2= Entry(master,width=30,bg="lightblue",textvariable=v_lname).grid(row=3, column=1, sticky=W)
    #Label and Entry box for House number
    e3=Label(master,text="House no  :", bg="lightblue", fg="black", font="none 13 bold").grid(row=4)
    e3= Entry(master,width=30,bg="lightblue",textvariable=v_hno).grid(row=4, column=1, sticky=W)
    #Label and Entry box for First line of Address
    e4=Label(master,text="1st of Line Address:", bg="lightblue", fg="black", font="none 13 bold").grid(row=5)
    e4= Entry(master,width=30,bg="lightblue",textvariable=v_address).grid(row=5, column=1, sticky=W)
    #Label and Entry box for Postcode
    e5=Label(master,text="Postcode :", bg="lightblue", fg="black", font="none 13 bold").grid(row=6)
    e5= Entry(master,width=30,bg="lightblue",textvariable=v_postcode).grid(row=6, column=1, sticky=W)

    #Label and Dropbox for Date of Birth
    #Day
    Label(master,text="Date \nof Birth:",bg="lightblue", fg="black", font="none 13 bold").grid(row=7)
    Label(master,text="\n\n\n\nDay",bg="lightblue", fg="black", font="none 10 bold").grid(row=7)
    day=OptionMenu(master,v_day, *("01","02","03","04","05","06","07","08","09","10",11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31))
    day.config(width=5,bg="lightblue")
    v_day.set("Day")
    day.grid(row=8)
    #Month
    Label(master,text="Date \nof Birth:",bg="lightblue", fg="black", font="none 13 bold").grid(row=7)
    Label(master,text="\n\n\n\nMonth",bg="lightblue", fg="black", font="none 10 bold").grid(row=7,column=1,sticky=W)
    month=OptionMenu(master,v_month, *("01","02","03","04","05","06","07","08","09","10",11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31))
    month.config(width=5,bg="lightblue")
    v_month.set("Month")
    month.grid(row=8,column=1,sticky=W)
    #Year
    Label(master,text="Date \nof Birth:",bg="lightblue", fg="black", font="none 13 bold").grid(row=7)
    Label(master,text="\n\n\n\nYear",bg="lightblue", fg="black", font="none 10 bold").grid(row=7,column=1,sticky=E)
    Year=OptionMenu(master,v_year, *(2002,2001,2000,1999,1998,1997,1996,1995,1994,1993,1992,1991,1990,1989,1988,1987,1986,1985,1984,1983,
                                       1982,1981,1980,1979,1978,1977,1976,1975,1974,1973,1972,1971,1970,1969,1968,1967,1966,1965,1964,1963,
                                       1962,1961,1960,1959,1958,1957,1956,1955,1954,1953,1952,1951,1950,1949,1948,1947,1946,1945,1944,1943,1942,
                                       1941,1940,1939,1938,1937,1936,1935,1934,1933,1932,1931,1930))
    Year.config(width=5,bg="lightblue")
    v_year.set("Year")
    Year.grid(row=8,column=1,sticky=E)


    #==========================================================================================================================
    #Label and Dropbox for Date of Provisional License isseud
    #Day
    Label(master,text="Date of Provisional\nLicense Issued",bg="lightblue", fg="black", font="none 13 bold").grid(row=9)
    Label(master,text="\n\n\n\nDay",bg="lightblue", fg="black", font="none 10 bold").grid(row=9)
    pday=OptionMenu(master,v_pday, *("01","02","03","04","05","06","07","08","09","10",11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31))
    pday.config(width=5,bg="lightblue")
    v_pday.set("Day")
    pday.grid(row=10)
    #Month
    Label(master,text="Date of Provisional\nLicense Issued:",bg="lightblue", fg="black", font="none 13 bold").grid(row=9)
    Label(master,text="\n\n\n\nMonth",bg="lightblue", fg="black", font="none 10 bold").grid(row=9,column=1,sticky=W)
    pmonth=OptionMenu(master,v_pmonth, *("01","02","03","04","05","06","07","08","09","10",11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31))
    pmonth.config(width=5,bg="lightblue")
    v_pmonth.set("Month")
    pmonth.grid(row=10,column=1,sticky=W)
    #Year
    Label(master,text="Date of Provisional\nLicense Issued:",bg="lightblue", fg="black", font="none 13 bold").grid(row=9)
    Label(master,text="\n\n\n\nYear",bg="lightblue", fg="black", font="none 10 bold").grid(row=9,column=1,sticky=E)
    pYear=OptionMenu(master,v_pyear, *(2002,2001,2000,1999,1998,1997,1996,1995,1994,1993,1992,1991,1990,1989,1988,1987,1986,1985,1984,1983,
                                       1982,1981,1980,1979,1978,1977,1976,1975,1974,1973,1972,1971,1970,1969,1968,1967,1966,1965,1964,1963,
                                       1962,1961,1960,1959,1958,1957,1956,1955,1954,1953,1952,1951,1950,1949,1948,1947,1946,1945,1944,1943,1942,
                                       1941,1940,1939,1938,1937,1936,1935,1934,1933,1932,1931,1930))
    pYear.config(width=5,bg="lightblue")
    v_pyear.set("Year")
    pYear.grid(row=10,column=1,sticky=E)

    #Label and Entrybox for Number of lessons booked
    Label(master,text="How many lessons",bg="lightblue", fg="black", font="none 13 bold").grid(row=11,column=0)
    Label(master,text="do you want to book?",bg="lightblue", fg="black", font="none 13 bold").grid(row=11,column=1)

    cost=OptionMenu(master,v_cost, *(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30))
    cost.config(width=23,bg="lightblue")
    v_cost.set("0")
    cost.grid(row=12,column=1)

    #Label and Button to find cost and to close the window
    Button(master,width=7, text='Get \na Quote\n',font="none 14 bold", command=Validation_check,bg="green").grid(row=14, column=0,sticky=E)
    Label(master,text="\n\n\n",font="none 16 bold",bg="lightblue").grid(row=14, column=1, sticky=E)
    Button(master,width=7, text='\nClose\n', font="none 14 bold",command=exit1, bg="red").grid(row=14,column=1)

Main()
mainloop()
