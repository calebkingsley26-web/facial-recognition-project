from tkinter import *

application =Tk()

application.geometry('1020x630+0+0')

#prevent from maximing
application.resizable(False,False)
application.title('My Retaturant - Invoicing system')
application.config(bg='burlywood')

#top Panel
top_panel = Frame(application,bd=1,relief=FLAT)
top_panel.pack(side=TOP)

#title Panel
title_tag = Label(top_panel,text = 'Invoicing System', fg='azure4',font=('Dosis',58),bg='burlywood',width=27)
title_tag.grid(row=0,column=0)


#left panel
left_panel = Frame(application,bd=1,relief=FLAT)
left_panel.pack(side=LEFT)

#cost_panel
cost_panel = Frame(application,bd=1,relief=FLAT)
cost_panel.pack(side=BOTTOM)


#food Panel
food_panel = LabelFrame(left_panel,text= 'Food',font=('Dosis',19,'bold'),bd=1,relief=FLAT,fg='azure4')

food_panel.pack(side=LEFT)

foodx_panel = LabelFrame(left_panel,text= 'Food',font=('Dosis',19,'bold'),bd=1,relief=FLAT,fg='azure4')

food_panel.pack(side=LEFT)

application.mainloop()



