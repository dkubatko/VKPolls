from Tkinter import *
from get_poll import start_app
from multiprocessing import Process
import os
import Tkinter
import warnings


warnings.filterwarnings("ignore")
os.system("mode con cols=48 lines=13")
print 'Enter the data in the window and press <Submit>'

global link
global w
global h
global font
global rgb

def to_list(s):
   new_s = s[1:-1]
   li = new_s.split(',')
   lis = []
   for elem in li:
      lis.append(int(elem))
   return tuple(lis)


app = Tk()
app.title("VKPolls")
app.geometry("430x270")
Label(app, text="Enter the post link: ").grid(row = 0, column = 0, columnspan = 2, padx = (0, 49))

link = Entry(app, width = 40, justify='center')
link.grid(row = 1, column = 0, columnspan = 2, padx = (0, 49), pady = (0, 10))
link.insert(END, "https://vk.com/wall-39130902_1562384")

Label(app, text="Width:").grid(row=2, column = 0)
Label(app, text="Height (per row):").grid(row=2, column = 1)
w = Entry(app, width = 20, justify='center')
w.grid(row = 3, column = 0, padx = 10, pady = (0, 10))
w.insert(END, "300")

h = Entry(app, width = 20, justify='center')
h.grid(row = 3, column = 1, padx = 60, pady = (0, 10))
h.insert(END, "70")

Label(app, text="Font:").grid(row=4, column = 0)
Label(app, text="Color (RGB + A):").grid(row=4, column = 1)

font = Entry(app, width = 20, justify='center')
font.grid(row = 5, column = 0, padx = 10, pady = (0, 10))
font.insert(END, "25")

rgb = Entry(app, width = 20, justify='center')
rgb.grid(row = 5, column = 1, padx = 60, pady = (0, 10))
rgb.insert(END, "(255, 255, 255)")

Label(app, text="Border thickness:").grid(row=6, column = 0)
Label(app, text="BG color: (RGB + A):").grid(row=6, column = 1)

b_thick = Entry(app, width = 20, justify='center')
b_thick.grid(row = 7, column = 0, padx = 10)
b_thick.insert(END, "0")

b_rgb = Entry(app, width = 20, justify='center')
b_rgb.grid(row = 7, column = 1, padx = 60)
b_rgb.insert(END, "(0,0,0,127)")

def press():
   
  # try:
      data = to_list(rgb.get())
      a1, a2, a3, a4, a5, a6, a7 = int(w.get()), int(h.get()), to_list(rgb.get()), int(font.get()),link.get(), to_list(b_rgb.get()), int(b_thick.get())

      if (link.get() == ''):
         raise ValueError('Value in the field <link> is wrong')
      
      app.destroy()

      

      #try:
      t1 = Process(target = start_app(a1, a2, a3, a4,
             a5, a6, a7))
      t1.start()
      #except:
         #print "Link is not working!"
         #a = raw_input()
   #except:
     # Label(app, text="Wrong input!", fg='red').grid(row=10, columnspan = 2, padx = (0, 49))
      
   
   
b = Button(app, text = "Submit", command = press, width = 10)
b.grid(row=8, columnspan = 2, padx = (0, 50), pady = (30, 0))

app.mainloop()


