from tkinter import *
import datetime
def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    min = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime("%p")
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")

    lab_hr.config(text = hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_ampm.config(text=am)
    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)

    lab_hr.after(200,date_time)

clock = Tk()
clock.title('digital clock')
clock.geometry('1000x500')
clock.config(bg='light blue')
#for display of time
#hours
lab_hr = Label(clock,text = "00",font = ('Arial',55,"italic"),bg='light pink',fg='white')
lab_hr.place(x=120,y=50,height=110,width=100)
lab_hr_txt = Label(clock,text = "Hour",font = ('Arial',20,"italic"),bg='light pink',fg='white')
lab_hr_txt.place(x=120,y=190,height=40,width=100)
#min
lab_min = Label(clock,text = "00",font = ('Arial',55,"italic"),bg='light pink',fg='white')
lab_min.place(x=340,y=45,height=110,width=100)
lab_min_txt = Label(clock,text = "Min.",font = ('Arial',20,"italic"),bg='light pink',fg='white')
lab_min_txt.place(x=340,y=190,height=40,width=100)
#sec
lab_sec = Label(clock,text = "00",font = ('Arial',55,"italic"),bg='light pink',fg='white')
lab_sec.place(x=560,y=45,height=110,width=100)
lab_sec_txt = Label(clock,text = "Sec.",font = ('Arial',20,"italic"),bg='light pink',fg='white')
lab_sec_txt.place(x=560,y=190,height=40,width=100)
#ampm
lab_ampm = Label(clock,text = "00",font = ('Arial',55,"italic"),bg='light pink',fg='white')
lab_ampm.place(x=780,y=45,height=110,width=100)
lab_ampm_txt = Label(clock,text = "AM/PM",font = ('Arial',20,"italic"),bg='light pink',fg='white')
lab_ampm_txt.place(x=780,y=190,height=40,width=100)
#for display of date
#date
lab_date = Label(clock,text = "00",font = ('Arial',55,"italic"),bg='light pink',fg='white')
lab_date.place(x=120,y=270,height=110,width=100)
lab_date_txt = Label(clock,text = "Date",font = ('Arial',20,"italic"),bg='light pink',fg='white')
lab_date_txt.place(x=120,y=410,height=40,width=100)
#month
lab_month = Label(clock,text = "00",font = ('Arial',55,"italic"),bg='light pink',fg='white')
lab_month.place(x=340,y=270,height=110,width=100)
lab_month_txt = Label(clock,text = "Month",font = ('Arial',20,"italic"),bg='light pink',fg='white')
lab_month_txt.place(x=340,y=410,height=40,width=100)
#year
lab_year = Label(clock,text = "00",font = ('Arial',55,"italic"),bg='light pink',fg='white')
lab_year.place(x=560,y=270,height=110,width=100)
lab_year_txt = Label(clock,text = "Year",font = ('Arial',20,"italic"),bg='light pink',fg='white')
lab_year_txt.place(x=560,y=410,height=40,width=100)
#day
lab_day = Label(clock,text = "00",font = ('Arial',35,"italic"),bg='light pink',fg='white')
lab_day.place(x=780,y=270,height=110,width=100)
lab_day_txt = Label(clock,text = "Day",font = ('Arial',20,"italic"),bg='light pink',fg='white')
lab_day_txt.place(x=780,y=410,height=40,width=100)

date_time()
clock.mainloop()