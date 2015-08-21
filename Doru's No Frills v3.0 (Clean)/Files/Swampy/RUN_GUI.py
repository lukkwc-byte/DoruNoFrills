from Gui import *
g = Gui()
g.title('Bourbun Chicken')

def make_button():
    g.bu(text='No, Press me!', command=make_label)
def make_label():
    for i in range(1000):
        g.la(text='Good job!')
    
button = g.bu(text='Press Me!', command=make_button)
g.mainloop()

