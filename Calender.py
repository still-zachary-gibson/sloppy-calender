#okay this is the calender thing, so what I need
#Dates
#saving
#graphical ui

from tkinter import * #is this it?
from tkinter import ttk
from tkinter import font as tkfont

import datetime

def has_a_holiday(day, month, year):
    if "_"+str(month) in holidays:
        if str(day) in holidays["_"+str(month)]:
            #print(get_all_holidays(day, month, year))
            return True
    if str(month) + "/" + str(year) in holidays:
        if str(day) in holidays[str(month) + "/" + str(year)]:
            return True
    if "|"+str(day) in holidays:
        return True

def get_all_holidays(day, month, year):
    return_ma = []

    if str(month) + "/" + str(year) in holidays:
        if str(day) in holidays[str(month) + "/" + str(year)]:
            for holdiaf in holidays[str(month) + "/" + str(year)][str(day)]:
                return_ma.append([holdiaf, 0])
    if "_"+str(month) in holidays:
        if str(day) in holidays["_"+str(month)]:
            for holdiaf in holidays["_"+str(month)][str(day)]:
                return_ma.append([holdiaf, 1])
    if "|"+str(day) in holidays:
        for holdiaf in holidays["|"+str(day)]:
            return_ma.append([holdiaf, 2])

    return return_ma

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
            theDays[i].config(style="NotADay.TFrame")
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
            theDays[i].config(style="Today.TFrame", relief=SOLID)
            if i >= 35 and cool_dates[35] != "":
                theDays[i].grid()
        else:
            theOtherThing[i].config(bg="white")
            theDays[i].config(style="Day.TFrame", relief=SOLID)
            if has_a_holiday(cool_dates[i], dater.month, dater.year):
                theOtherThing[i].config(bg="tomato")
                theDays[i].config(style="Holiday.TFrame", relief=SOLID)
            if i >= 35 and cool_dates[35] != "":
                theDays[i].grid()

#print(cool_modulo(datetime.datetime.weekday(datetime.datetime.now())+1,7)

import math

holidays = dict()

holidays["_12"] = {"25": ["Christmas"]}
holidays["12/2025"] = {"25": ["TestDay"]}
holidays["|12"] = ["The twelve"]

def backers():
    hide_it()
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
    hide_it()
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
    hide_it()
    global current_thing
    current_thing = datetime.datetime(trueDay.year,trueDay.month,trueDay.day)
    realButton.config(state=DISABLED)
    get_current_month(current_thing)

def hide_it():
    global the_last_one
    global holiday_list
    global which_true
    the_last_one = -1
    the_holiday_menu.grid_forget()
    holiday_list = []
    which_true = []
    for children in the_holiday_menu.winfo_children():
        children.destroy()

the_last_one = -1 #im putting this in a variable because OH GOODNESS GEE WILIKERS

which_true = []

'''def otherTest():
    global which_true
    for children in the_holiday_menu.winfo_children():
        if isinstance(children, Checkbutton):
            #print(which_true[str(children.cget("variable"))])
            #print(children.getvar(children.cget("variable")), bool(int(children.getvar(children.cget("variable")))))
            if which_true[str(children.cget("variable"))] != bool(int(children.getvar(children.cget("variable")))):
                if bool(int(children.getvar(children.cget("variable")))):
                    print(children.cget("text"))
                    print(holiday_list)
            which_true[str(children.cget("variable"))] = bool(int(children.getvar(children.cget("variable"))))
            '''

def okay_check(index, value, op):
    global current_thing
    global holidays
    global holiday_list
    stupid = {"Don't Repeat" : 0, "Yearly" : 1, "Monthly": 2, "Remove": 3}
    numba = index.split("_")[0]
    #print(stupid[which_true[int(numba)][0].get()],which_true[int(numba)][1])
    #print(stupid[which_true[int(index)][0].get()]) #what a stupid method just to read a darn variable
    if (stupid[which_true[int(numba)][0].get()] == which_true[int(numba)][1]): #has it actually been changed? check
        return #jobs done
    holiday = index.split("_")[1]
    my_info = -1
    for neato in range(len(holiday_list)): #get the info for it
        if (holiday_list[neato][0] == holiday):
            my_info = holiday_list[neato]
            break
    #remove it from its old position~~~
    if(my_info[1] == 2):
        for okay in range(len(holidays["|" + theOtherThing[the_last_one].cget("text")])):
            if(holidays["|" + theOtherThing[the_last_one].cget("text")][okay] == my_info[0]):
                holidays["|" + theOtherThing[the_last_one].cget("text")].pop(okay)
                break
        if len(holidays["|" + theOtherThing[the_last_one].cget("text")]) == 0:
            holidays.pop("|" + theOtherThing[the_last_one].cget("text"))
    elif my_info[1] == 1:
        for okay in range(len(holidays["_" + str(current_thing.month)][theOtherThing[the_last_one].cget("text")])):
            if holidays["_" + str(current_thing.month)][theOtherThing[the_last_one].cget("text")][okay] == my_info[0]:
                holidays["_" + str(current_thing.month)][theOtherThing[the_last_one].cget("text")].pop(okay)
                break
        if len(holidays["_" + str(current_thing.month)][theOtherThing[the_last_one].cget("text")]) == 0:
            holidays["_" + str(current_thing.month)].pop(theOtherThing[the_last_one].cget("text"))
        if len(holidays["_" + str(current_thing.month)]) == 0:
            holidays.pop("_" + str(current_thing.month))
    elif my_info[1] == 0:
        for okay in range(len(holidays[str(current_thing.month) + "/" + str(current_thing.year)][theOtherThing[the_last_one].cget("text")])):
            if holidays[str(current_thing.month) + "/" + str(current_thing.year)][theOtherThing[the_last_one].cget("text")][okay] == my_info[0]:
                holidays[str(current_thing.month) + "/" + str(current_thing.year)][theOtherThing[the_last_one].cget("text")].pop(okay)
                break
        if len(holidays[str(current_thing.month) + "/" + str(current_thing.year)][theOtherThing[the_last_one].cget("text")]) == 0:
            holidays[str(current_thing.month) + "/" + str(current_thing.year)].pop(theOtherThing[the_last_one].cget("text"))
        if len(holidays[str(current_thing.month) + "/" + str(current_thing.year)]) == 0:
            holidays.pop(str(current_thing.month) + "/" + str(current_thing.year))

    #now to readd it!
     
    if stupid[which_true[int(numba)][0].get()] == 2:
        if "|" + theOtherThing[the_last_one].cget("text") not in holidays:
            holidays.update({"|" + theOtherThing[the_last_one].cget("text") : []})
        holidays["|" + theOtherThing[the_last_one].cget("text")].append(my_info[0])
    elif stupid[which_true[int(numba)][0].get()] == 1:
        if "_" + str(current_thing.month) not in holidays:
            holidays.update({"_" + str(current_thing.month) : {}})
        if theOtherThing[the_last_one].cget("text") not in holidays["_" + str(current_thing.month)]:
            holidays["_" + str(current_thing.month)].update({theOtherThing[the_last_one].cget("text"): []})
        holidays["_" + str(current_thing.month)][theOtherThing[the_last_one].cget("text")].append(my_info[0])
    elif stupid[which_true[int(numba)][0].get()] == 0:
        if str(current_thing.month) + "/" + str(current_thing.year) not in holidays:
            holidays.update({str(current_thing.month) + "/" + str(current_thing.year): {}})
        if theOtherThing[the_last_one].cget("text") not in holidays[str(current_thing.month) + "/" + str(current_thing.year)]:
            holidays[str(current_thing.month) + "/" + str(current_thing.year)].update({theOtherThing[the_last_one].cget("text"): []})
        holidays[str(current_thing.month) + "/" + str(current_thing.year)][theOtherThing[the_last_one].cget("text")].append(my_info[0])

    which_true[int(numba)][1] = stupid[which_true[int(numba)][0].get()]

    #print(holiday_list)

    for neato in range(len(holiday_list)): #get the info for it
        if (holiday_list[neato][0] == holiday):
            holiday_list[neato][1] = stupid[which_true[int(numba)][0].get()] #alter it here
            break

    #print(holiday_list)

    #print(holidays)

    get_current_month(current_thing)

    theOtherThing[the_last_one].config(bg="light goldenrod")
    theDays[the_last_one].config(style="Selected.TFrame", relief=SOLID)

def test(event):
    global the_last_one
    global holiday_list
    global which_true
    i = int(str(event.widget).split("!")[2].split("e")[1].split(".")[0])-9

    if the_last_one != -1:
        if theOtherThing[the_last_one].cget("text") == str(current_thing.day) and current_thing.month == trueDay.month and current_thing.year == trueDay.year:
            theOtherThing[the_last_one].config(bg="light sky blue")
            theDays[the_last_one].config(style="Today.TFrame", relief=SOLID)
        else:
            theOtherThing[the_last_one].config(bg="white")
            theDays[the_last_one].config(style="Day.TFrame", relief=SOLID)
            #print(theOtherThing[the_last_one].cget("text"), current_thing.month, current_thing.year)
            if has_a_holiday(theOtherThing[the_last_one].cget("text"), current_thing.month, current_thing.year):
                theOtherThing[the_last_one].config(bg="tomato")
                theDays[the_last_one].config(style="Holiday.TFrame", relief=SOLID)
    
    #print(theOtherThing[i].cget("text"))

    
    which_true = []
    the_holiday_menu.grid_forget()
    holiday_list = []
    for children in the_holiday_menu.winfo_children():
        children.destroy()

    if theOtherThing[i].cget("text") == "" or i == the_last_one:
        if i == the_last_one:
            the_last_one = -1
        return
    
    the_holiday_menu.grid(column=9,row=0,sticky=(N))

    holiday_list = get_all_holidays(theOtherThing[i].cget("text"), current_thing.month, current_thing.year)

    Frame(the_holiday_menu, width=200, height=0, borderwidth=0).pack()
    #print(holiday_list)

    for holi in enumerate(holiday_list):
        #Label(the_holiday_menu, text=holi[0]).pack()
        #awesoem = Checkbutton(the_holiday_menu, text=holi[0],command=otherTest, variable=holi[0])
        really_cool = StringVar(root, "HEY!!!", str(holi[0]) + "_" + holi[1][0])
        which_true.append([really_cool, holi[1][1]])
        really_cool.trace_add("write", okay_check)
        awesoem = ttk.Combobox(the_holiday_menu, values=("Don't Repeat", "Yearly", "Monthly", "Remove"), textvariable=really_cool, state="readonly")
        #really_cool.set(awesoem)
        which_true[len(which_true)-1].append(awesoem)
        awesoem.current(holi[1][1])
        awesoem.pack()
        #which_true[holi[0]] = holi[1]
        #if holi[1] == True:
        #    awesoem.select()
    
    #the_holiday_menu.grid

    theOtherThing[i].config(bg="light goldenrod")
    theDays[i].config(style="Selected.TFrame", relief=SOLID)
    the_last_one = i

root = Tk()

# Okay we want a 7 by 7 Grid...
# Wait, top row has to be the month
#so 7 by 8, with the top being WIDE unlike the ones divided into 7ths

root.title("Daily Calender")

root.resizable(False, False)

#s = ttk.Style()
#s.theme_use('classic')

calender = ttk.Frame(root, padding=10)#, width=700/2+16,height=50*8+4*8)

#monthBox = ttk.Frame(calender, )

style = ttk.Style()

#print(style.theme_settings(style.theme_use(), background="black"))

#style.configure("BW.TLabel", foreground="black", background="white")
style.configure("NotADay.TFrame", background="gray67")
style.configure("Day.TFrame", background="white")
style.configure("Today.TFrame", background="light sky blue")
style.configure("Selected.TFrame", background="light goldenrod")
style.configure("Holiday.TFrame", background="tomato")

#print(style.layout('NotADay.TFrame'))

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

#root.bind('<ButtonRelease-1>', test)

okayTestBox.grid(column=0,row=0, columnspan=7)
okayTestBox.pack_propagate(False)
for i in range(7):
    theTop[i].grid(column=i,row=1, sticky=(W,N))
    theTop[i].pack_propagate(False)

for i in range(6*7):
    #testing[i].grid(column=i%7,row=math.floor(i/7)+2, sticky=(W))
    theDays[i].grid(column=i%7,row=math.floor(i/7)+2, sticky=(W))
    theDays[i].pack_propagate(False)
    theDays[i].bindtags('Click')
    theOtherThing[i].bindtags('Click')

root.bind_class('Click', "<Button-1>", test)

backButton.grid(column=0,row=9,sticky=(W))
realButton.grid(column=3,row=9)
mextButton.grid(column=6,row=9,sticky=(E))

the_holiday_menu = LabelFrame(root,text="Holiday Menu", width=200,height=50*8.4, borderwidth=4)

the_holiday_menu.grid(column=9,row=0,sticky=(N))

the_holiday_menu.grid_forget()

holiday_list = []

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

print("Did I make it?")

root.mainloop()