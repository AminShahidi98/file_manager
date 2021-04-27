from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os

class manager:

    def __init__(self, master):

        #self.s = ttk.Style()
        #self.s.configure('clear.TButton' , foreground='red' , background='red')
        
        self.show = Text(master , width=69 , height=27)
        self.show.place(x=15 , y = 200)
        self.show.config(background='lightblue' , foreground='darkblue' ,borderwidth=4)
        self.show.config(wrap='char')
        #self.show.config(font=('italic'))
          
        self.errorbox = Text(master, width=61, height=2)
        self.errorbox.place(x=17 , y=150)
        self.errorbox.config(wrap='word')
        self.errorbox.config(background='lightpink' , foreground='darkred' , borderwidth=4)
        self.errorbox.config(font=('bold'))

        self.frame = ttk.Frame(master , width=560 , height=140)
        self.frame.config(relief=RIDGE)
        self.frame.place(x=15 , y=2)

        self.path = ttk.Entry(self.frame, width=60)
        self.path.insert(0,'Enter your direction here...')
        self.path.place(x=7, y=7)
        self.path.config(foreground = 'blue')

        self.label = ttk.LabelFrame(self.frame , width=565 , height=70 , text='Tip')
        self.label.place(x=7 , y=95)
        
        self.help = Label(self.label ,
        text='Entered directory subsets will be shown at the blue box . Please enter your directory with \\\ separator.  ').pack()

        self.contact=ttk.Label(master , width = 93  , text='For any questions contact 09335332243 or amin7799sh@gmail.com')
        self.contact.place(x=14 , y=645)
        self.contact.config(foreground='darkblue')

        #self.sb=ttk.Scrollbar(root , orient=VERTICAL , command = self.show.yview)
        

#----------------------------------------------------------------------------------------------        
        
        self.b1=ttk.Button(self.frame, text = "         clear        ",command = self.clear).place(x=380 , y=5)
        
        self.b2=ttk.Button(self.frame, text = "         go to       ",command = self.goto).place(x=470 , y=5)
        
        self.b3=ttk.Button(self.frame, text = "             make a new folder          ",command = self.nf ).place(x=380 , y=35)
        
        self.b4=ttk.Button(self.frame, text = "              open file or folder          ",command = self.opener).place(x=380 , y=65)

        #master.bind('<Control-c>' ,self.clear)
       
#----------------------------------------------------------------------------------------------
    def clear(self):
        self.path.delete(0,END)
        self.errorbox.delete('1.0' , 'end lineend')

#----------------------------------------------------------------------------------------------
    def goto(self) :
        self.show.delete('1.0' , 'end lineend')
        self.errorbox.delete('1.0' , 'end lineend')
        if os.path.isdir(self.path.get()):
            self.errorbox.delete('1.0' , 'end lineend')
            l=os.listdir(self.path.get())
            for i in l:
                self.show.insert('end' , i + '\n')
        elif os.path.isfile(self.path.get()):
            self.errorbox.delete('1.0' , 'end lineend')
            self.errorbox.insert('end' , 'The entered text is a file!')
            messagebox.showerror(title='Invalid request!' , message='The entered text is a file!')
        else:
            self.errorbox.delete('1.0' , 'end lineend')
            self.errorbox.insert('end' , 'The entered text is not a directory!')
            messagebox.showerror(title='Invalid request!' , message='The entered text is not a directory!')
#----------------------------------------------------------------------------------------------

    def nf(self) :
        self.errorbox.delete('1.0' , 'end lineend')
        if  not os.path.isdir(self.path.get()):
            if not os.path.isfile(self.path.get()):
                self.errorbox.delete('1.0' , 'end lineend')
                if messagebox.askyesno(title='Please check this out' , message='Are you sure you want to establish a new directory\nby creating the following folder?'):

                    try:
                        os.makedirs(self.path.get())
                        messagebox.showinfo(title='Folder created' , message='folder created , a new directory established')

                    except :
                        self.errorbox.delete('1.0' , 'end lineend')
                        self.errorbox.insert('end' , 'The following request is not reachable!')
                        messagebox.showerror(title='Invalid request!' , message='The following request is not reachable!')
                    
        else:
            self.errorbox.delete('1.0' , 'end lineend')
            self.errorbox.insert('end' , 'The following directory already exists!')
            messagebox.showerror(title='Invalid request!' , message='The following directory already exists!')
#----------------------------------------------------------------------------------------------            

    def opener(self):
        self.errorbox.delete('1.0' , 'end lineend')
        if os.path.isdir(self.path.get()) or os.path.isfile(self.path.get()):

            try:
                os.startfile(self.path.get() , 'open')
                
            except:
                self.errorbox.delete('1.0' , 'end lineend')
                self.errorbox.insert('end' , 'The following request is not reachable!')
                messagebox.showerror(title='Invalid request!' , message='The following request is not reachable!')
                
        else:
            self.errorbox.delete('1.0' , 'end lineend')
            self.errorbox.insert('end' , "The following file or directory don't exist!")
            messagebox.showerror(title='Invalid request!' , message="The following file or directory don't exist!")
     
#----------------------------------------------------------------------------------------------
                
        
                    
def main():            
    
    root = Tk()
    root.geometry('592x675')
    root.title('File Manager')
    
   #----------------------------------------------------------------------------------------------                 

    root.option_add('*tearOff', False)
    menubar = Menu(root)
    root.config(menu = menubar)
    file = Menu(menubar)
    edit = Menu(menubar)

    help_ = Menu(menubar)
    menubar.add_cascade(menu = file, label = 'File')
    menubar.add_cascade(menu = edit, label = 'Edit')
    menubar.add_cascade(menu = help_, label = 'Help')

    file.add_command(label = 'New', command = lambda: print('New File'))
    file.add_separator()
    file.add_command(label = 'Open...', command = lambda: print('Opening File...'))
    file.add_command(label = 'Save', command = lambda: print('Saving File...'))
    file.entryconfig('New', accelerator = 'Ctrl+N')
    file.entryconfig('Open...', state = 'disabled')
    file.delete('Save')
    save = Menu(file)
    file.add_cascade(menu = save, label = 'Save')
    save.add_command(label = 'Save As',command = lambda: print('Saving As...'))
    save.add_command(label = 'Save All', command = lambda: print('Saving All...'))
    choice = IntVar()

    edit.add_radiobutton(label = 'One', variable = choice, value = 1)
    edit.add_radiobutton(label = 'Two', variable = choice, value = 2)
    edit.add_radiobutton(label = 'Three', variable = choice, value = 3)
    #file.post(400, 300)
            
#----------------------------------------------------------------------------------------------
                
    app = manager(root)
    #messagebox.showinfo(title='Welcome' , message='Thanks for choosing us!\nPlease at first read the readmefirst.txt uploded in my github account.')
    root.mainloop()

if __name__ == "__main__": main()

'''for any questions call 09335332243 and my student ID is 96522177'''
