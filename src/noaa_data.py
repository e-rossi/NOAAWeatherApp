import urllib.request
import xml.etree.ElementTree as ET
import gui

# data dict
weather_data = {
    "observation_time": "",
    "weather": "",
    "temp_f": "",
    "temp_c": "",
    "dewpoint_f": "",
    "dewpoint_c": "",
    "relative_humidity": "",
    "wind_string": "",
    "visibility_mi": "",
    "pressure_string": "",
    "pressure_in": "",
    "location": ""
}

def get_weather_data(station_id='KLAX'):
    url = f'http://www.weather.gov/xml/current_obs/{station_id}.xml'
    request = urllib.request.urlopen(url)
    content = request.read().decode()
    xml_root = ET.fromstring(content)
    for data_point in weather_data.keys():
        weather_data[data_point] = xml_root.find(data_point).text

def populate_gui_from_dict():
    gui.city.set(weather_data['location'])
    gui.updated.set(weather_data['observation_time'].replace('Last Updated on ', ''))
    gui.weather.set(weather_data['weather'])
    gui.temperature.set('{} \xb0F ({} \xb0C)'.format(weather_data['temp_f'], weather_data['temp_c']))
    gui.dewpoint.set('{} \xb0F ({} \xb0C)'.format(weather_data['dewpoint_f'], weather_data['dewpoint_c']))
    gui.rel_humi.set(weather_data['relative_humidity'] + '%')
    gui.wind.set(weather_data['wind_string'])
    gui.visibility.set(weather_data['visibility_mi'] + ' miles')
    gui.msl_pressure.set(weather_data['pressure_string'])
    gui.altimeter.set(weather_data['pressure_in'] + ' in Hg')

def _get_station():
    station = gui.selected_station.get()
    get_weather_data(station)
    populate_gui_from_dict()

