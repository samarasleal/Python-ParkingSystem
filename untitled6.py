#from tkinter import *
#
#top = Tk()
#cont1 = Frame(top, pady =10, bg="navy")
#cont1.pack()
#
#mb=  Menubutton(cont1, text="condiments", bg="navy")
#menu  =  Menu ( mb, tearoff = 0, bg="navy")
#menu.entryconfig(0,bg='navy')
#mb.menu = menu
#mb["menu"]  =  mb.menu
#mb.menu.entryconfig(1, bg='navy')
#
#
#mb.menu.config(bg="black")
#    
#mayoVar  = IntVar()
#ketchVar = IntVar()
#
#mb.menu.add_checkbutton ( label="mayo",
#                          variable=mayoVar )
#mb.menu.add_checkbutton ( label="ketchup",
#                          variable=ketchVar )
#
#mb.pack()
#
#
#variable = StringVar(top)
#variable.set("...") # default value
#
#w = OptionMenu(top, variable, "one", "two", "three")
#w.config(bg="navy")
#w.pack()
#
#
#top.mainloop()
#
#import datetime
#s = '05/08/2017 08:12:23'
#t = '20/08/2017 08:13:23'
#
#s2 = '2017-07-04 14:10:11.910398'
#
#date1 = int(datetime.datetime.strptime(s, '%d/%m/%Y %H:%M:%S').strftime("%s"))
#date2 = int(datetime.datetime.strptime(t, '%d/%m/%Y %H:%M:%S').strftime("%s"))
#date3 = int(datetime.datetime.strptime(s2, '%d/%m/%Y %H:%M:%S').strftime("%s"))
#
#difdate = date2 - date1
#
#print(difdate)
#
## Datas
#e =datetime.datetime(2017,8,5,6,42,5)
#s= datetime.datetime(2017,9,5,17,28,5)
#res = s-e
#res.days
#
## horas
#hoje =datetime.datetime(2017,8,12,6,42,5)
#s= datetime.datetime(2017,8,12,17,28,5)
#res = s-hoje
#
#tempo_s = res.seconds
#a = tempo_s % 60
#tempo_m = tempo_s / 60
#b = tempo_m % 60
#c = int(tempo_m / 60)
#print( c,'horas',b, 'minutos e',a,'segundos')
#
## string <-> time
#e =datetime.datetime.now()
#e
#s = e.strftime('%Y-%m-%d %H:%M:%S')
#s
#e2 = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
#e2
#                
#def teste(data):
#    print(data)
#    print(type(data))
#teste(hoje)

from tkinter import *

class ExampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        t = SimpleTable(self, 10,2)
        t.pack(side="top", fill="x")
        #t.set(0,0,"Hello, world")

class SimpleTable(Frame):
    def __init__(self, parent, rows=10, columns=2):
        # use black background so it "peeks through" to 
        # form grid lines
        Frame.__init__(self, parent, background="black")
        vagasOcupadas = [[1,"um"],[2,"dois"]]
        for linha in range(len(vagasOcupadas)):
            for coluna in range(len(vagasOcupadas[linha])):
                label = Label(self, text="%s" % (vagasOcupadas[linha][coluna]), 
                                 borderwidth=0, width=10)
                label.grid(row=linha, column=coluna, sticky="nsew", padx=1, pady=1)




#    def set(self, row, column, value):
#        widget = self._widgets[row][column]
#        widget.configure(text=value)

if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()