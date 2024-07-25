from tkinter import (Button, 
                     Radiobutton, 
                     Label, 
                     StringVar , 
                     TOP,
                     Tk,
                     LEFT,
                     BooleanVar,
                     PhotoImage,
                     messagebox)
from farsi import Fa
import webbrowser

class Main(Tk):
    def __init__(self, geometry, title, bg, icon):
        
        Tk.__init__(self)
        self.geometry(geometry)
        self.title(title)
        self.resizable(False, False)
        self.config(bg=bg)
        self.iconbitmap(icon)
        self.photo = PhotoImage(file = r"images\github2.png")

    def create_lables_buttons_radios(self):
        lb_info = Label(self,
                    text='Welcome to Strange App',
                    font=('arial', 18, 'bold'),
                    pady=15,
                    background='#508D4E',
                    foreground='black')
        lb_info.pack()


        # Radio buttons
        values = {"فارسی" : "fa", 
                "English (soon)" : "en"} 
        
        v = StringVar(self, "fa") 

        for (text, value) in values.items(): 
            Radiobutton(self, text = text, variable = v, bg='#508D4E', fg='black', activebackground='darkgreen',font=('arial', 12, 'bold'),
                value = value).pack(side = TOP, ipady = 5) 

        # buttons
        b_submit = Button(self,
                        text="Submit",
                        font=('arial', 12, 'bold'),
                        activebackground='darkgreen',
                        activeforeground='white',
                        fg='black',
                        bg='#80AF81',
                        command=lambda:self.select_lang(v, v1),
                        width=10)
        b_submit.place(x=197, y=200)

        b_github = Button(self,
                        text=" Give me ⭐",
                        font=('arial', 12, 'bold'),
                        activebackground='darkgreen',
                        activeforeground='white',
                        fg='black',
                        cursor='star',
                        image=self.photo,
                        compound=LEFT,
                        bg='#80AF81',
                        command=self.link_github)
        b_github.place(x=30, y=200)

        v1 = BooleanVar(value=False) 

        Radiobutton(self, text = "Don't show me again", variable = v1, bg='#508D4E', fg='black', activebackground='darkgreen',font=('arial', 12, 'bold'),
                value = True, command=lambda:self.dont_show(v1)).place(x=30, y=250)

    def link_github(self):
        webbrowser.open('https://github.com/Saman148/Strange-App')  #repostory url

    def dont_show(self, show):
        value = show.get()
        if value:
            with open(r'txt\show.txt', 'w') as f:
                f.write('True')
            
    def select_lang(self, lang, a):
        lang_value = lang.get()
        with open(r'txt\lang.txt', 'w') as f:
            f.write(lang_value)

        if lang_value == 'fa': #farsi language
                self.destroy()
                obj1 = Fa('900x500', 
                            'Strange App Farsi',
                            '#508D4E',
                            'images/main-logo.ico')
                obj1.create_lables_buttons_frame()
                obj1.mainloop()     
        if lang_value == 'en': #english language
            messagebox.showinfo('language', 'English comming soon')    #open english file

if __name__ == "__main__":
    
    with open(r'txt\show.txt', 'r') as f:
        show = f.read()
    with open(r'txt\lang.txt', 'r') as f:
        lang = f.read()

    if show == 'True':
        if lang == 'fa':
            obj2 = Fa('900x500', 
                            'Strange App Farsi',
                            '#508D4E',
                            'images/main-logo.ico')
            obj2.create_lables_buttons_frame()
            obj2.mainloop()        #open farsi file
        elif lang == 'en':
            pass   #open english file
    else:
        obj1 = Main('500x300',
                    "Strange App",
                    '#508D4E',
                    "images/main-logo.ico")
        obj1.create_lables_buttons_radios()
        obj1.mainloop()
