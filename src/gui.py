import tkinter as tk
from tkinter import Menu
from tkinter import ttk
import noaa_data

def _quit():
    win.quit()
    win.destroy()
    exit()

win = tk.Tk()
win.title('Weather App')

# creates a menu
menu_bar = Menu()
win.config(menu=menu_bar)

# creates menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=_quit)
menu_bar.add_cascade(label='File', menu=file_menu)

# adds another menu to the menubar
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label='About')
menu_bar.add_cascade(label='Help', menu=help_menu)

# Creates a container frame to hold all other widgets
weather_conditions_frame = ttk.LabelFrame(text='Current Weather Conditions ')

# using the tkinter grid layout manager
weather_conditions_frame.grid(column=0, row=0, padx=8, pady=4)

# repositioning the weather_conditions_frame to the next row below
weather_conditions_frame.grid_configure(column=0, row=1, padx=8, pady=4)

# creating new label frame 
weather_station_frame = ttk.LabelFrame(text='Latest Observation for: ')
weather_station_frame.grid(column=0, row=0, padx=8, pady=4)

# placing label and combobox into new frame
ttk.Label(weather_station_frame, text='Weather Station ID: ').grid(column=0, row=0, sticky='w')

# creating new combobox
station = tk.StringVar()
selected_station = ttk.Combobox(weather_station_frame, width=5, textvariable=station)
selected_station['values'] = ('KLAX', 'KNYC', 'KDEN')
selected_station.grid(column=1, row=0)
selected_station.current(0)  # highlights first city

city = tk.StringVar()
ttk.Label(weather_station_frame, textvariable=city).grid(column=0, row=1, columnspan=3)
# ---------------------------------------------------------------------------------------------------------------

# Adding labels and Textbox entry widgets
ENTRY_WIDTH = 20
# ---------------------------------------------------------------------------------------------------------------
ttk.Label(weather_conditions_frame, text='Last Updated: ').grid(column=0, row=1, sticky='e')
updated = tk.StringVar()
updated_entry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=updated, state='readonly')
updated_entry.grid(column=1, row=1, sticky='w')
# ---------------------------------------------------------------------------------------------------------------
ttk.Label(weather_conditions_frame, text='Weather: ').grid(column=0, row=2, sticky='e')
weather = tk.StringVar()
weather_entry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=weather, state='readonly')
weather_entry.grid(column=1, row=2, sticky='w')
# ---------------------------------------------------------------------------------------------------------------
ttk.Label(weather_conditions_frame, text='Temperature: ').grid(column=0, row=3, sticky='e')
temperature = tk.StringVar()
temperature_entry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=temperature, state='readonly')
temperature_entry.grid(column=1, row=3, sticky='w')
# ---------------------------------------------------------------------------------------------------------------
ttk.Label(weather_conditions_frame, text='Dewpoint: ').grid(column=0, row=4, sticky='e')
dewpoint = tk.StringVar()
dewpoint_entry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=dewpoint, state='readonly')
dewpoint_entry.grid(column=1, row=4, sticky='w')
# ---------------------------------------------------------------------------------------------------------------
ttk.Label(weather_conditions_frame, text='Relative Humidity: ').grid(column=0, row=5, sticky='e')
rel_humi = tk.StringVar()
rel_humi_entry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=rel_humi, state='readonly')
rel_humi_entry.grid(column=1, row=5, sticky='w')
# ---------------------------------------------------------------------------------------------------------------
ttk.Label(weather_conditions_frame, text='Wind: ').grid(column=0, row=6, sticky='e')
wind = tk.StringVar()
wind_entry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=wind, state='readonly')
wind_entry.grid(column=1, row=6, sticky='w')
# ---------------------------------------------------------------------------------------------------------------
ttk.Label(weather_conditions_frame, text='Visibility: ').grid(column=0, row=7, sticky='e')
visibility = tk.StringVar()
visibility_entry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=visibility, state='readonly')
visibility_entry.grid(column=1, row=7, sticky='w')
# ---------------------------------------------------------------------------------------------------------------
ttk.Label(weather_conditions_frame, text='MSL Pressure: ').grid(column=0, row=8, sticky='e')
msl_pressure = tk.StringVar()
msl_pressure_entry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=msl_pressure, state='readonly')
msl_pressure_entry.grid(column=1, row=8, sticky='w')
# ---------------------------------------------------------------------------------------------------------------
ttk.Label(weather_conditions_frame, text='Altimeter: ').grid(column=0, row=9, sticky='e')
altimeter = tk.StringVar()
altimeter_entry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=altimeter, state='readonly')
altimeter_entry.grid(column=1, row=9, sticky='w')
# ---------------------------------------------------------------------------------------------------------------
# Adding space between the fields
for child in weather_conditions_frame.winfo_children():
    child.grid_configure(padx=4, pady=3)
# ---------------------------------------------------------------------------------------------------------------

get_weather_btn = ttk.Button(weather_station_frame, text='Get Weather', command=noaa_data._get_station).grid(column=2, row=0)
