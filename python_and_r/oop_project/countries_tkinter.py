from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from countries_oop import Country, OECD, Compare_Countries

#create tkinter mainframe and root
root = Tk()
root.title("OECD Population Data Overview")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#initialise variables 
countries_list = StringVar()
years = IntVar()
list_of_countries = OECD().list_countries()




#create function calls
def show_charts():
  idx = country_listbox.curselection()
  selected = [country_listbox.get(i) for i in idx]
  

  data = Compare_Countries(selected).compare_population_over_time()

  


#create input components
ttk.Label(mainframe, text="Select up to 5 countries from the list").grid(column=0, row=1, sticky=N)
country_listbox = Listbox(mainframe, height=10, selectmode="multiple", selectbackground="lightgreen")
country_listbox.grid(column=1, row=1, sticky=E)

ttk.Button(mainframe, text="Show Charts", command=show_charts).grid(column=1, row=2)


for i, country in enumerate(list_of_countries):
  country_listbox.insert(i, country)


root.mainloop()

