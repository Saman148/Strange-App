from tkinter import *
from tkinter import messagebox
import webbrowser
from pynput.keyboard import Listener, KeyCode
import spammer 
from pynput.mouse import Button as buttonMouse
from pynput.mouse import Controller
import autoClicker

class Fa(Tk):
    def __init__(self, geometry, title, bg, icon):
        
        Tk.__init__(self)
        self.geometry(geometry)
        self.title(title)
        self.resizable(False, False)
        self.config(bg=bg)
        self.iconbitmap(icon)
        self.photo_github = PhotoImage(file = r"images\github2.png")
        self.photo_click = PhotoImage(file = r"images\click.png")
        self.photo_sms = PhotoImage(file = r"images\sms.png")
        self.photo_logo = PhotoImage(file = r"images\sms.png")
        self.photo_sms = PhotoImage(file = r"images\sms.png")

        self.photo_git64 = PhotoImage(file = r"images\github64.png")
        self.photo_sms64 = PhotoImage(file = r"images\sms64.png")
        self.photo_auto64 = PhotoImage(file = r"images\auto64.png")
        

    def create_lables_buttons_frame(self):
        

        b_spammer = Button(self,
                        text="اسپمر " ,
                        font=('arial', 12, 'bold'),
                        activebackground='darkgreen',
                        activeforeground='white',
                        fg='black',
                        image=self.photo_sms,
                        compound=RIGHT,
                        bg='#80AF81',
                        command=lambda: self.b_page_spammer(fr_main),
                        width=202)
        b_spammer.place(x=5, y=10)

        b_autoClicker = Button(self,
                        text="اتو کیلیکر ",
                        font=('arial', 12, 'bold'),
                        activebackground='darkgreen',
                        activeforeground='white',
                        fg='black',
                        image=self.photo_click,
                        compound=RIGHT,
                        bg='#80AF81',
                        command=lambda:self.b_page_autoClicker(fr_main),
                        width=202)
        b_autoClicker.place(x=5, y=55)

        b_github = Button(self,
                        text=" ستاره یادت نره ",
                        font=('arial', 12, 'bold'),
                        activebackground='darkgreen',
                        activeforeground='white',
                        fg='black',
                        bg='#80AF81',
                        image=self.photo_github,
                        compound=RIGHT,
                        command=self.b_github,
                        width=202)
        b_github.place(x=5, y=100)

        fr_main = LabelFrame(self, 
                             text='صفحه اصلی',
                        bd=5, 
                        width=675, 
                        fg='black',
                        height=490,
                        bg='#D6EFD8')
        fr_main.place(x=220, y=5)

        lb_wel2 = Label(fr_main,
                    text='Starage App',
                    font=('arial', 18, 'bold'),
                    pady=15,
                    background='#D6EFD8',
                    foreground='black')
        lb_wel2.place(x=310, y=80)

        lb_wel = Label(fr_main,
                    text='خیلی خوش اومدی',
                    font=('arial', 18, 'bold'),
                    pady=15,
                    background='#D6EFD8',
                    foreground='black')
        lb_wel.place(x=300, y=190)

        lb_info = Label(fr_main,
                    text='⭐ یادت نره حتما ستاره رو بدی ❤ ',
                    font=('arial', 18, 'bold'),
                    pady=15,
                    background='#D6EFD8',
                    foreground='black')
        lb_info.place(x=220, y=240)

        lb_photosms = Label(fr_main,
                    font=('arial', 18, 'bold'),
                    pady=15,
                    background='#D6EFD8',
                    image=self.photo_sms64,
                    foreground='black')
        lb_photosms.place(x=250, y=300)

        lb_photogit = Label(fr_main,
                    font=('arial', 18, 'bold'),
                    pady=15,
                    image=self.photo_git64,
                    background='#D6EFD8',
                    foreground='black')
        lb_photogit.place(x=350, y=300)

        lb_photoauto = Label(fr_main,
                    font=('arial', 18, 'bold'),
                    pady=15,
                    image=self.photo_auto64,
                    background='#D6EFD8',
                    foreground='black')
        lb_photoauto.place(x=450, y=300)

        lb_saman = Label(fr_main,
                         text=' github.com/Saman148',
                    font=('arial', 18, 'bold'),
                    image=self.photo_github,
                    compound=LEFT,
                    background='#D6EFD8',
                    foreground='black')
        lb_saman.place(x=230, y=390)

        lb_saman2 = Label(self,
                         text=' github.com/Saman148',
                    font=('arial', 12, 'bold'),
                    image=self.photo_github,
                    compound=LEFT,
                    background='#508D4E',
                    foreground='black')
        lb_saman2.place(x=0, y=450)

    def b_github(self):
        webbrowser.open('https://github.com/Saman148/Strange-App')

    def clear(self, frame):
        for i in frame.winfo_children() :
            i.destroy()

    def b_page_spammer(self, frame):
        self.clear(frame)

        lb_namePage = Label(frame,
                            text=' صفحه اسپمر',
                    font=('arial', 12, 'bold'),
                    pady=15,
                    image=self.photo_sms,
                    compound=LEFT,
                    background='#D6EFD8',
                    foreground='black')
        lb_namePage.place(x=550, y=1)

        lb_name = Label(frame,
                            text='اسم (نام فرد)',
                    font=('arial', 18, 'bold'),
                    pady=15,
                    background='#D6EFD8',
                    foreground='black')
        lb_name.place(x=530, y=70)

        e_name = Entry(frame,
                    font=('arial', 18, 'bold'),
                    justify='right',
                    background='lightgreen',
                    foreground='black')
        e_name.place(x=220, y=90)

        lb_s = Label(frame,
                            text='زمان برای ارسال هر یک پیام (ثانیه)',
                    font=('arial', 18, 'bold'),
                    pady=15,
                    background='#D6EFD8',
                    foreground='black')
        lb_s.place(x=345, y=130)

        e_s = Entry(frame,
                    font=('arial', 18, 'bold'),
                    justify='right',
                    width=6,
                    background='lightgreen',
                    foreground='black')
        e_s.place(x=220, y=150)

        lb_start = Label(frame,
                            text='زمان برای شروع برنامه (ثانیه)',
                    font=('arial', 18, 'bold'),
                    pady=15,
                    background='#D6EFD8',
                    foreground='black')
        lb_start.place(x=385, y=190)

        e_start = Entry(frame,
                    font=('arial', 18, 'bold'),
                    justify='right',
                    width=6,
                    background='lightgreen',
                    foreground='black')
        e_start.place(x=220, y=208)

        bt_submit = Button(frame,
                          text= 'شروع',
                    command=lambda:self.b_spammer(e_name, e_start, e_s),
                    width=6,
                    font=('arial', 18, 'bold'),
                    activebackground='darkgreen',
                    activeforeground='white',
                    fg='black',
                    bg='lightgreen')
        bt_submit.place(x=290, y=300)

    def b_page_autoClicker(self, frame):


        self.clear(frame)

        lb_namePage = Label(frame,
                            text=' صفحه اتوکیلیکر',
                    font=('arial', 12, 'bold'),
                    pady=15,
                    image=self.photo_click,
                    compound=LEFT,
                    background='#D6EFD8',
                    foreground='black')
        lb_namePage.place(x=530, y=1)

        lb_stopStart = Label(frame,
                            text='خاموش و روشن کردن (دکمه)',
                    font=('arial', 18, 'bold'),
                    pady=15,
                    background='#D6EFD8',
                    foreground='black')
        lb_stopStart.place(x=380, y=70)

        e_stopStart = Entry(frame,
                    font=('arial', 18, 'bold'),
                    justify='right',
                    background='lightgreen',
                    width=6,
                    
                    foreground='black')
        e_stopStart.place(x=220, y=90)
        e_stopStart.insert(END, 'a')

        lb_stop = Label(frame,
                            text='خاموش کردن اتوکیلیکر (دکمه)',
                    font=('arial', 18, 'bold'),
                    pady=15,
                    background='#D6EFD8',
                    foreground='black')
        lb_stop.place(x=375, y=130)

        e_stop = Entry(frame,
                    font=('arial', 18, 'bold'),
                    justify='right',
                    width=6,
                    background='lightgreen',
                    foreground='black')
        e_stop.place(x=220, y=150)
        e_stop.insert(END, 'b')

        bt_submit = Button(frame,
                          text= 'شروع',
                    width=6,
                    command= lambda:self.b_autoClicker(e_stopStart, e_stop),
                    font=('arial', 18, 'bold'),
                    activebackground='darkgreen',
                    activeforeground='white',
                    fg='black',
                    bg='lightgreen')
        bt_submit.place(x=290, y=300)

    def b_spammer(self, name, timeS, timeM):
         try:
            namePerson = name.get()
            timeStart = int(timeS.get())
            timeMessage = int(timeM.get())
            
            objSpammer  = spammer.Spammer('fa',
                                        namePerson,
                                        timeStart,
                                        timeMessage)
            objSpammer.start()
         except:
             messagebox.showerror('خطا', 'خطا در وارد کردن اطلاعات')

    def b_autoClicker(self, startStop, Stop):
        try:
            startStopKey = startStop.get()
            StopKey = Stop.get()

            delay = 0.001
            button = buttonMouse.right
            start_stop_key = KeyCode(char=startStopKey)
            stop_key = KeyCode(char=StopKey)

            mouse = Controller()
            click_thread = autoClicker.ClickMouse(delay, button)
            click_thread.start()
        except:
            messagebox.showerror('خطا', 'خطا در وارد کردن اطلاعات')

        def on_press(key):


            if key == start_stop_key:
                if click_thread.running:
                    click_thread.stop_clicking()
                else:
                    click_thread.start_clicking()


            elif key == stop_key:
                click_thread.exit()
                listener.stop()


        with Listener(on_press=on_press) as listener:
            listener.join()


if __name__ == "__main__":
    obj1 = Fa('900x500', 
            'Strange App Farsi',
            '#508D4E',
            'images/main-logo.ico')
    obj1.create_lables_buttons_frame()
    obj1.mainloop()
