#PHONE NUMBER LOCATION TRACKING USING PYTHON 

# >> Do Pip install phonenumbers. Because it is an external library that contains some modules python files
#Import phonenumber
#Get the timezone of the parse phonenumber and timezone is functionality inside phonenumber.
#Import Timezone
#Carrier i.e phone number network. So import carrier and use it to perform a function
#Use geocoder for region ie name of your country
#Since you are building an app, check if the phone number is valid >>> True
#delete a number from it and it will give False
#For if valid it gives all info, else it request for correct number for incomplete number
# >> Do pip install geopy or pip show geopy
#import Nominatim from geopy.geocoders for Longitude and Latitude of the location
# >> Do pip install timezonefinder
#Import TimezoneFinder from timezonefinder
# >> Do pip install Pytz
#import datetime 
#import pytz
#Create a new file gui.py to run my tkinter
# >>import tkinter     Note * means import everything in tkinter bcos it has many functionalities
# >>create root
# >>create root.mainloop
#Icon images and functions
#Label functions



#Import Packages
from tkinter import*
import phonenumbers
from phonenumbers import timezone, carrier, geocoder
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime 
import datetime
import pytz 

#GUI WINDOW and Global variables Declaraction
root = Tk()  
root.title("Phone Number Tracker") #App Name
root.geometry("365x584+300+20")  #App size
root.resizable(False,False)  #If you want to resize it; then use True, True
entry_widget_text = "input sample:"

#Fuctions to evaluate result

def Track():
   entry_number = entry.get()
   phoneNumber = phonenumbers.parse(entry_number) #parse differentiate the phone number from the country code.
   valid = phonenumbers.is_valid_number(phoneNumber) #To check the validity of the phone number

   if valid == True: 
     
#Phone timezone
     time_zone = timezone.time_zones_for_number(phoneNumber)
     Zone.config(text=time_zone)

#Operators (Networks like MTN, 9Mobile e.t.c)
     Carrier = carrier.name_for_number(phoneNumber,'en') #'en' means English Language
     sim.config(text=Carrier)

#Country
     Region = geocoder.description_for_number(phoneNumber, 'en')
     Country.config(text=Region)


#LOngitude and Latitude
     Locator = Nominatim(user_agent= "myGoecoder")
     location = Locator.geocode(Region)
     lng = location.longitude
     lat = location.latitude
     print(location.longitude, location.latitude)
     longitude.config(text=lng)
     latitude.config(text=lat)

#Time showing on the phone
     timezonefinder = TimezoneFinder()
     query_points = [ (14.3465435, 20.7866678),...]
     time_zone_finder = timezonefinder.timezone_at(lng =location.longitude, lat = location.latitude)
     print(time_zone_finder)
     date_time_local = datetime.datetime.now()
     date_time_utc = datetime.datetime.now(pytz.utc)
     for timeZone in pytz.all_timezones:
        print(timeZone)
     timeZone= date_time_local.strftime("%I:%M:%S %p  (%Y/%m/%d)")
     clock.config(text=timeZone)

#Request of correct number for wrong number entry
   else: 
     not_valid = "please enter correct phoneNumber"
     print("please enter correct phoneNumber")
     response_message.config(text=not_valid)
     response_window.deiconify()

def on_entry_click():  
#"""Function to handle when the user clicks on the input field.""""   
     if entry_number.get() == entry_widget_text:

#Clears input field and set the text colour to black 
        entry_number.delete(0, END)
        entry_number.config(fg="black")

#Hide the response window
def hide_response():
     response_window.withdraw()     
        
#Warning Massage Widget response
response_window = Toplevel(root)  
response_window.geometry("300x200+320+150")

#Size and Position window setting
response_message = Message(response_window,text="", width=250, font=("Helvetica", 14), fg="white", bg= "red")
response_message.place(relx=0.5, rely=0.5, anchor="center")
hide_button = Button(response_window, text="OK", command=hide_response)
hide_button.place(relx=0.5, rely=0.8, anchor="center")
response_window.withdraw() #Hide the response window initially


#Icon Image
icon = PhotoImage(file = "logo image.png")
root.iconphoto(False, icon)
 
#Logo Image
logo = PhotoImage(file="logo image.png" )
Label(root,image=logo).place(x=240,y=70)

#Search Top Image
SearchTop = PhotoImage(file="search png.png")
Label(root,image=SearchTop).place(x=20,y=190)

#Heading
heading= Label(root,text="TRACK NUMBER",font=("arial",15,"bold"))
heading.place(x=90,y=119)

#BottomBox Image
Box = PhotoImage(file="bottom png.png")
Label(root,image=Box).place(x=-2,y=355)

#Entry
entry=StringVar()
entry_number=Entry(root,textvariable=entry,width=17,justify="center",bd=0,font=("arial",20))
entry_number.place(x=50,y=220)

#Search Button Image
search_image = PhotoImage(file="search.png")
search = Button(root,image=search_image,borderwidth=0,cursor="hand2",bd=0,command=Track)
search.place(x=35,y=300)

#Label Informations

Country = Label(root,text="country:",bg="#57adff", fg="black", font=("arial",10,"bold"))
Country.place(x=50,y=400)

sim = Label(root,text="SIM:", bg="#57adff",fg="black",font=("arial",10,"bold"))
sim.place(x=200,y=400)

Zone = Label(root,text="TimeZone:", bg="#57adff",fg="black",font=("arial",10,"bold"))
Zone.place(x=50,y=450)

clock = Label(root,text="clock:",bg="#57adff", fg="black", font=("arial",10,"bold"))
clock.place(x=200,y=450)

longitude = Label(root,text="Longitude:",bg="#57adff", fg="black", font=("arial",10,"bold"))
longitude.place(x=50,y=500)

latitude = Label(root,text="Latitude:",bg="#57adff", fg="black", font=("arial",10,"bold"))
latitude.place(x=200,y=500)



#Start GUI, Result visualization and Display
root.mainloop()  