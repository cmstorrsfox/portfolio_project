from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from countries_oop import Country, OECD, Compare_Countries
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

#create tkinter mainframe and root
root = Tk()

root.title("OECD Population Data Overview")
root.attributes("-fullscreen", True)
notebook = ttk.Notebook(root)
notebook.grid(column=0, row=0, sticky=(N,W,E,S))
one_country_frame = ttk.Frame(notebook, padding="3 3 12 12")
one_country_frame.grid(column=0, row=0, sticky=(N,W,E,S))
compare_country_frame = ttk.Frame(notebook, padding="3 3 12 12")
compare_country_frame.grid(column=0, row=0, sticky=(N,W,E,S))



#initialise variables 
countries_list = StringVar()
compare_func = StringVar()
one_country_func = StringVar()
year = IntVar()
min_year = IntVar()
max_year = IntVar()
year_step = IntVar()
as_line = BooleanVar()
by_sex = BooleanVar()
list_of_countries = OECD().list_countries()




#create function calls for compare frame
def show_compare_charts():
  #get input
  idx = country_listbox.curselection()
  selected = [country_listbox.get(i) for i in idx]

  if compare_func.get() == "Compare populations over time":
    fig = Compare_Countries(selected).compare_population_over_time()
  elif compare_func.get() == "Compare populations by year":
    fig = Compare_Countries(selected).compare_population_by_year(year.get())
  
  canvas = FigureCanvasTkAgg(fig, compare_country_frame)
  canvas.draw()
  canvas.get_tk_widget().grid(column=3, row=0, rowspan=10, sticky=(N,E,S,W), padx=20, pady=20)


def toggle_compare_combobox(event):
  if compare_country_combobox.get() == "Compare populations over time":
    year_selector.state(statespec=["disabled"])
  elif compare_country_combobox.get() == "Compare populations by year":
    year_selector.state(statespec=["!disabled"])


#create function calls for one country frame
def show_country_charts():
  #get input
  idx = country_listbox_2.curselection()
  selected = country_listbox_2.get(idx)


  if one_country_func.get() == "Plot population over time":
    fig = Country(selected).chart_pop_growth(years=(min_year.get(), max_year.get(), year_step.get()), as_line=as_line.get(), by_sex=by_sex.get())
  elif one_country_func.get() == "Plot population by age group over time":
    fig = Country(selected).line_growth(years=(min_year.get(), max_year.get(), year_step.get()))
  elif one_country_func.get() == "Plot expected growth over time":
    fig = Country(selected).growth_trend(max_year=max_year.get())

  canvas = FigureCanvasTkAgg(fig, one_country_frame)
  canvas.draw()
  canvas.get_tk_widget().grid(column=7, row=0, rowspan=10, sticky=(N,E,S,W), padx=20, pady=20)


def toggle_combobox(event):
  if one_country_combobox.get() == "Plot population over time":
    by_sex_check.state(statespec=["!disabled"])
    as_line_check.state(statespec=["!disabled"])
    max_year_label.configure(text="Max Year") 
  
  elif one_country_combobox.get() == "Plot population by age group over time":
    by_sex_check.state(statespec=["disabled"])
    as_line_check.state(statespec=["disabled"])
    max_year_label.configure(text="Max Year") 

  elif one_country_combobox.get() == "Plot expected growth over time":
    max_year_selector.configure(to=3000)
    max_year_label.configure(text="Projection to:") 
    max_year.set(2050)
    by_sex_check.state(statespec=["disabled"])
    as_line_check.state(statespec=["disabled"])
    min_year_selector.state(statespec=["disabled"])
    step_selector.state(statespec=["disabled"])





#create input components for compare countries frame
ttk.Label(compare_country_frame, text="Select the output from the options below:").grid(column=0, row=0, columnspan=2, sticky=(E,W), pady=8)
compare_country_combobox = ttk.Combobox(compare_country_frame, values=["Compare populations over time", "Compare populations by year"], textvariable=compare_func, state="readonly")
compare_country_combobox.grid(column=0, row=1, columnspan=2, sticky=(W,E), pady=8, padx=4)
year_selector_label = ttk.Label(compare_country_frame, text="Select year to compare:").grid(column=0, row=2, sticky=W, pady=8, padx=4)
year_selector = ttk.Spinbox(compare_country_frame, from_=1960, to=2020, textvariable=year)
year_selector.grid(column=1, row=2, sticky=W, pady=8, padx=4)
ttk.Label(compare_country_frame, text="Select up to 5 countries from the list below:").grid(column=0, columnspan=2, row=4, sticky=(E,W), pady=8)
country_listbox = Listbox(compare_country_frame, height=10, selectmode="multiple", selectbackground="lightgreen")
country_listbox.grid(column=0, row=5, columnspan=2, sticky=(E,W), pady=8)
ttk.Button(compare_country_frame, text="Show Comparison Charts", command=show_compare_charts).grid(column=0, row=6, columnspan=2, sticky=(W,E),pady=8)

#create input components for one country frame
ttk.Label(one_country_frame, text="Select the output from the options below:").grid(column=0, row=0, columnspan=2, sticky=(E,W), pady=8)
one_country_combobox = ttk.Combobox(one_country_frame, values=["Plot population over time", "Plot population by age group over time", "Plot expected growth over time"], textvariable=one_country_func, state="readonly")
one_country_combobox.grid(column=0, row=1, columnspan=2, sticky=(E,W), pady=8)

by_sex_check = ttk.Checkbutton(one_country_frame, text="Plot by Sex", onvalue=True, variable=by_sex)
by_sex_check.grid(column=0, row=2, sticky=W, padx=4)
as_line_check = ttk.Checkbutton(one_country_frame, text="Plot as Line Chart", onvalue=True, variable=as_line)
as_line_check.grid(column=1, row=2, sticky=W, padx=4)

min_year_label = ttk.Label(one_country_frame, text="Min Year").grid(column=0, row=3, sticky=W, padx=4)
min_year_selector = ttk.Spinbox(one_country_frame, from_=1960, to=2020, textvariable=min_year)
min_year_selector.grid(column=1, row=3, sticky=W, padx=4)
max_year_label = ttk.Label(one_country_frame, text="Max Year").grid(column=0, row=4, sticky=W, padx=4)
max_year_selector = ttk.Spinbox(one_country_frame, from_=1960, to=2020, textvariable=max_year)
max_year_selector.grid(column=1, row=4, sticky=W, padx=4)
step_year_label = ttk.Label(one_country_frame, text="X Axis Step").grid(column=0, row=5, sticky=W, padx=4)
step_selector = ttk.Spinbox(one_country_frame, from_=1, to=60, textvariable=year_step)
step_selector.grid(column=1, row=5, sticky=W, padx=4)

ttk.Label(one_country_frame, text="Choose one country from the list below:")
country_listbox_2 = Listbox(one_country_frame, height=10, selectmode="browse", selectbackground="lightgreen")
country_listbox_2.grid(column=0, row=6, columnspan=2, sticky=(E,W), pady=8)
ttk.Button(one_country_frame, text="Show Country Charts", command=show_country_charts).grid(column=0, row=7, columnspan=2, sticky=(W,E),pady=8)


for i, country in enumerate(list_of_countries):
  country_listbox.insert(i, country)
  country_listbox_2.insert(i, country)

#binding for compare countries 
compare_country_combobox.bind("<<ComboboxSelected>>", toggle_compare_combobox)

#binding for onee country
one_country_combobox.bind("<<ComboboxSelected>>", toggle_combobox)

#binding to escape fullscreen
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
root.bind("<F11>", lambda event: root.attributes("-fullscreen", False))


#add frames to notebook
notebook.add(one_country_frame, text="One Country")
notebook.add(compare_country_frame, text="Compare Countries")

#set default values - compare
compare_country_combobox.current(newindex=0)
year_selector.set(1960)
year_selector.state(statespec=["disabled"])

#set default values - one country
one_country_combobox.current(newindex=0)
min_year.set(1960)
max_year.set(2020)
year_step.set(5)
by_sex.set(False)
as_line.set(False)





#create app
root.mainloop()

