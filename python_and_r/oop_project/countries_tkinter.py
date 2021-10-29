from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from countries_oop import Country, OECD, Compare_Countries

#create tkinter mainframe and root
root = Tk()

root.title("OECD Population Data Overview")
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
year_range = BooleanVar()
list_of_countries = OECD().list_countries()




#create function calls for compare frame
def show_compare_charts():
  #get input
  idx = country_listbox.curselection()
  selected = [country_listbox.get(i) for i in idx]

  if compare_func.get() == "over_time":
    Compare_Countries(selected).compare_population_over_time()
  elif compare_func.get() == "by_year":
    Compare_Countries(selected).compare_population_by_year(year.get())


def toggle_pop_over_time(event):
  if pop_over_time_radio.state(statespec=["selected"]):
    year_selector.grid_remove()
  
def toggle_pop_by_year(event):
  if pop_by_year_radio.state(statespec=["selected"]):
    year_selector.set(1960)
    year_selector.grid(column=2, row=1, sticky=W, pady=8)


#create function calls for one country frame
def show_country_charts():
  #get input
  idx = country_listbox_2.curselection()
  selected = country_listbox_2.get(idx)
  print(one_country_func.get())


  if one_country_func.get() == "over_time":
    Country(selected).chart_pop_growth(years=(min_year.get(), max_year.get(), year_step.get()), as_line=as_line, by_sex=by_sex)
  elif one_country_func.get() == "by_age":
    Country(selected).line_growth(years=(min_year.get(), max_year.get(), year_step.get()))
  elif one_country_func.get() == "expected_growth":
    Country(selected).growth_trend(max_year=max_year.get())

def toggle_pop_over_time_2(event):
  if pop_over_time_radio_2.state(statespec=["selected"]):
    by_sex_check.grid(column=0, row=2, sticky=W)
    as_line_check.grid(column=1, row=2, sticky=W)
    min_year_selector.grid(column=2, row=2, sticky=W)
    max_year_selector.grid(column=3, row=2, sticky=W)
    step_selector.grid(column=4, row=2, sticky=W)
    min_year.set(1960)
    max_year.set(2020)
    year_step.set(5)
    by_sex.set(False)
    as_line.set(False)
  
def toggle_pop_by_age(event):
  if pop_by_age_radio.state(statespec=["selected"]):
    min_year_selector.grid(column=2, row=2, sticky=W)
    max_year_selector.grid(column=3, row=2, sticky=W)
    step_selector.grid(column=4, row=2, sticky=W)
    min_year.set(1960)
    max_year.set(2020)
    year_step.set(5)
    by_sex_check.grid_remove()
    as_line_check.grid_remove()

def toggle_pop_growth_trend(event):
  if pop_growth_trend_radio.state(statespec=["selected"]):
    max_year_selector.configure(to=3000)    
    max_year_selector.grid(column=3, row=2, sticky=W)
    max_year.set(2050)
    by_sex_check.grid_remove()
    as_line_check.grid_remove()
    min_year_selector.grid_remove()
    step_selector.grid_remove()





#create input components for compare countries frame
ttk.Label(compare_country_frame, text="Select the output from the options below:").grid(column=0, row=0, columnspan=3, sticky=(E,W), pady=8)
pop_over_time_radio = ttk.Radiobutton(compare_country_frame, text="compare populations over time", value="over_time", variable=compare_func)
pop_over_time_radio.grid(column=0, row=1, sticky=W,pady=8, padx=4)
pop_by_year_radio = ttk.Radiobutton(compare_country_frame, text="compare populations by year", value="by_year", variable=compare_func)
pop_by_year_radio.grid(column=1, row=1, sticky=W, pady=8, padx=4)
year_selector = ttk.Spinbox(compare_country_frame, from_=1960, to=2020, textvariable=year)
ttk.Label(compare_country_frame, text="Select up to 5 countries from the list below:").grid(column=0, columnspan=3, row=2, sticky=(E,W), pady=8)
country_listbox = Listbox(compare_country_frame, height=10, selectmode="multiple", selectbackground="lightgreen")
country_listbox.grid(column=0, row=3, columnspan=3, sticky=(E,W), pady=8)
ttk.Button(compare_country_frame, text="Show Comparison Charts", command=show_compare_charts).grid(column=0, row=4, columnspan=3, sticky=(W,E),pady=8)

#create input components for one country frame
ttk.Label(one_country_frame, text="Select the output from the options below:").grid(column=0, row=0, columnspan=3, sticky=(E,W), pady=8)

pop_over_time_radio_2 = ttk.Radiobutton(one_country_frame, text="plot population over time", value="over_time", variable=one_country_func)
pop_over_time_radio_2.grid(column=0, row=1, sticky=W, pady=8, padx=4)
pop_by_age_radio = ttk.Radiobutton(one_country_frame, text="plot population by age group over time", value="by_age", variable=one_country_func)
pop_by_age_radio.grid(column=1, row=1, sticky=W, pady=8, padx=4)
pop_growth_trend_radio = ttk.Radiobutton(one_country_frame, text="plot expected growth in population", value="expected_growth", variable=one_country_func)
pop_growth_trend_radio.grid(column=2, row=1, sticky=W, pady=8, padx=4)

by_sex_check = ttk.Checkbutton(one_country_frame, text="Plot by Sex", onvalue=True, variable=by_sex)
as_line_check = ttk.Checkbutton(one_country_frame, text="Plot as Line Chart", onvalue=True, variable=as_line)
min_year_selector = ttk.Spinbox(one_country_frame, from_=1960, to=2020, textvariable=min_year)
max_year_selector = ttk.Spinbox(one_country_frame, from_=1960, to=2020, textvariable=max_year)
step_selector = ttk.Spinbox(one_country_frame, from_=1, to=60, textvariable=year_step)

ttk.Label(one_country_frame, text="Choose one country from the list below:")
country_listbox_2 = Listbox(one_country_frame, height=10, selectmode="browse", selectbackground="lightgreen")
country_listbox_2.grid(column=0, row=3, columnspan=3, sticky=(E,W), pady=8)
ttk.Button(one_country_frame, text="Show Country Charts", command=show_country_charts).grid(column=0, row=4, columnspan=3, sticky=(W,E),pady=8)

for i, country in enumerate(list_of_countries):
  country_listbox.insert(i, country)
  country_listbox_2.insert(i, country)

#binding for compare countries 
pop_by_year_radio.bind("<Button-1>", toggle_pop_by_year)
pop_over_time_radio.bind("<Button-1>", toggle_pop_over_time)

#binding for onee country
pop_over_time_radio_2.bind("<Button-1>", toggle_pop_over_time_2)
pop_by_age_radio.bind("<Button-1>", toggle_pop_by_age)
pop_growth_trend_radio.bind("<Button-1>", toggle_pop_growth_trend)


#add frames to notebook
notebook.add(one_country_frame, text="One Country")
notebook.add(compare_country_frame, text="Compare Countries")

#create app
root.mainloop()

