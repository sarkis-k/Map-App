import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
mt_name=list(data["NAME"])
elev=list(data["ELEV"])

html = """ 
<h3>Volcano Information:</h3>
Height: %s m
"""

map = folium.Map(location=[34.1442783,-118.2535569], zoom_start=10, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="my map")



for coorX, coorY, nm, el in zip(lat,lon,mt_name, elev):
	iframe = folium.IFrame(html=html %str(el), width=200, height=100)
	fg.add_child(folium.Marker(location=[coorX,coorY], popup=folium.Popup(iframe), icon=folium.Icon(color='red')))
	
map.add_child(fg)

map.save("Map1.html")
