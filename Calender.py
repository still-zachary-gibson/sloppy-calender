#okay this is the calender thing, so what I need
#Dates
#saving
#graphical ui

from tkinter import * #is this it?
from tkinter import ttk
from tkinter import font as tkfont

import datetime

def cool_modulo(n,d):
    if(n % d >= 0):
        return n % d
    else:
        return d + (n % d)

def get_current_month(dater):
    the_day = (dater.day)
    the_monthr = dater.month
    first_day = datetime.datetime(dater.year, dater.month, 1)
    month_list = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    the_month.set(month_list[the_monthr-1] + " " + str(dater.year))
    cool_dates = []
    for i in range((datetime.datetime.weekday(first_day)+1)%7):
        cool_dates.append("")
    last_date = 1
    we_good = True
    while we_good:
        try: 
            testvar = (datetime.datetime(dater.year, dater.month, last_date))
            last_date += 1
        except ValueError:
            last_date -= 1
            we_good = False
    for i in range(last_date):
        cool_dates.append(str(i+1))
    while (len(cool_dates)) < 6*7:
        cool_dates.append("")
    for i in range(len(cool_dates)):
        theOtherThing[i].config(text=cool_dates[i])
        if cool_dates[i] == "":
            theOtherThing[i].config(bg="gray67")
            theDays[i].config(style="WD.TFrame")
            if i > 35: 
                if cool_dates[35] == "":
                    theDays[i].grid_remove()
                else:
                    theDays[i].grid()
            elif i == 35:
                theOtherThing[i].config(bg=str(style.lookup("TFrame", "background", default="", state=())))
                theDays[i].config(style="invis.TFrame", relief=FLAT)
        elif cool_dates[i] == str(the_day) and dater.month == trueDay.month and dater.year == trueDay.year:
            theOtherThing[i].config(bg="light sky blue")
            theDays[i].config(style="WEDsa.TFrame", relief=SOLID)
            if i >= 35 and cool_dates[35] != "":
                theDays[i].grid()
        else:
            theOtherThing[i].config(bg="white")
            theDays[i].config(style="WED.TFrame", relief=SOLID)
            if i >= 35 and cool_dates[35] != "":
                theDays[i].grid()

#print(cool_modulo(datetime.datetime.weekday(datetime.datetime.now())+1,7)

import math

def backers():
    global current_thing
    fake_time = [current_thing.year,current_thing.month-1]

    if fake_time[1] == 0:
        fake_time[1] = 12
        fake_time[0] -= 1
    
    if fake_time[0] == trueDay.year and fake_time[1] == trueDay.month:
        current_thing = datetime.datetime(trueDay.year,trueDay.month,trueDay.day)
        realButton.config(state=DISABLED)
    else:
        current_thing = datetime.datetime(fake_time[0],fake_time[1],1)
        realButton.config(state=NORMAL)
    get_current_month(current_thing)

def mexters():
    global current_thing
    fake_time = [current_thing.year,current_thing.month+1]

    if fake_time[1] == 13:
        fake_time[1] = 1
        fake_time[0] += 1
    
    if fake_time[0] == trueDay.year and fake_time[1] == trueDay.month:
        current_thing = datetime.datetime(trueDay.year,trueDay.month,trueDay.day)
        realButton.config(state=DISABLED)
    else:
        current_thing = datetime.datetime(fake_time[0],fake_time[1],1)
        realButton.config(state=NORMAL)
    get_current_month(current_thing)

def reset():
    global current_thing
    current_thing = datetime.datetime(trueDay.year,trueDay.month,trueDay.day)
    realButton.config(state=DISABLED)
    get_current_month(current_thing)

root = Tk()

# Okay we want a 7 by 7 Grid...
# Wait, top row has to be the month
#so 7 by 8, with the top being WIDE unlike the ones divided into 7ths

root.title("Daily Calender")

#s = ttk.Style()
#s.theme_use('classic')

calender = ttk.Frame(root, padding=10)#, width=700/2+16,height=50*8+4*8)

#monthBox = ttk.Frame(calender, )

style = ttk.Style()

#print(style.theme_settings(style.theme_use(), background="black"))

style.configure("BW.TLabel", foreground="black", background="white")
style.configure("WD.TFrame", background="gray67")
style.configure("WED.TFrame", background="white")
style.configure("WEDsa.TFrame", background="light sky blue")

#print(style.layout('WD.TFrame'))

style.configure("invis.TFrame", background=str(style.lookup("TFrame", "background", default="", state=())))

the_month = StringVar()
the_month.set("September")

okayTestBox = ttk.Frame(calender, borderwidth=2, width=700/2, height=50, relief=SOLID)
theActualMonth = Label(okayTestBox,textvariable=the_month, font=("TkDefaultFont",30)).pack(anchor=CENTER)

theTop = []
#print(tk.font)
#fonst = tkfont.Font(family="Consolas", size=50, weight="normal")

#default_font = tkfont.nametofont("TkDefaultFont")
#default_font.configure(size=25)

daysOfWeek = ("S","M","T","W","T","F","S")
for i in range(7):
    theTop.append(ttk.Frame(calender, width=50,height=50, borderwidth=2, relief=SOLID))
    Label(theTop[i], text=daysOfWeek[i],font=("TkDefaultFont",25)).pack(anchor=CENTER) #This was hell :D

theDays = []
theOtherThing = []

testing = []

#default_font.configure(size=2)

for i in range(6*7):
    #testing.append(ttk.Frame(calender, width=50,height=50, borderwidth=2, relief=SOLID, style="BW.TLabel"))
    theDays.append(ttk.Frame(calender, width=50,height=50, borderwidth=2, relief=SOLID, style="WB.TFrame"))
    theOtherThing.append(Label(theDays[i], text=str(i+1),font=("TkDefaultFont",13)))
    theOtherThing[i].pack(anchor=CENTER)

backButton = Button(calender, text="<BACK", command=backers)
mextButton = Button(calender, text="NEXT>", command=mexters)
realButton = Button(calender, text="REAL", command=reset, state=DISABLED)

#they just make up crap
#AND THEN ANOTHER SORUCE SOLVES THE ISSUE COME ON DUDE

calender.grid(column=0, row=0)
calender.grid_rowconfigure(1,minsize=60)
calender.grid_rowconfigure(8,minsize=20)

okayTestBox.grid(column=0,row=0, columnspan=7)
okayTestBox.pack_propagate(False)
for i in range(7):
    theTop[i].grid(column=i,row=1, sticky=(W,N))
    theTop[i].pack_propagate(False)

for i in range(6*7):
    #testing[i].grid(column=i%7,row=math.floor(i/7)+2, sticky=(W))
    theDays[i].grid(column=i%7,row=math.floor(i/7)+2, sticky=(W))
    theDays[i].pack_propagate(False)


backButton.grid(column=0,row=9,sticky=(W))
realButton.grid(column=3,row=9)
mextButton.grid(column=6,row=9,sticky=(E))

trueDay = datetime.datetime.now()

current_thing = datetime.datetime(trueDay.year,trueDay.month,trueDay.day)

#print(current_thing.month)

get_current_month(current_thing)

#background_color = style.lookup("TFrame", "background", default="", state=())

#print(f"The background color of the TFrame is: {background_color}")

#print(root)

'''
ttk.Label(calender, text="The Month Goes Here").grid(column=0, row=0, rowspan=7, sticky=(N))
'''

root.mainloop()