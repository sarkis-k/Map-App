import folium
import pandas as pd


def color_producer(elevation):
	if elevation<1000:
		return "green"
	elif 1000<= elevation<2500:
		return "orange"
	else:
		return "red"

data = pd.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
mt_name=list(data["NAME"])
elev=list(data["ELEV"])



#basic html
# html = """
# <h3>Volcano Information:</h3>
# Height: %s m
# """

#advanced html
# html="""
# Volcano name:<br>
# <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
# Height: %s m
# """

map = folium.Map(location=[34.1442783,-118.2535569], zoom_start=5, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="my map")


#for basic and advanced html popup
# for coorX, coorY, nm, el in zip(lat,lon,mt_name, elev):
# 	iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=100)
# 	fg.add_child(folium.Marker(location=[coorX,coorY], popup=folium.Popup(iframe), icon=folium.Icon(color='red')))
#icon=folium.Icon(color=(lambda el: "red" if el>2000 else "green")

for coorX, coorY, nm, el in zip(lat,lon,mt_name, elev):
	fg.add_child(folium.Marker(location=[coorX,coorY], popup=str(el)+" m",  icon=folium.Icon(color=color_producer(el)) ))

	
map.add_child(fg)

map.save("Map1.html")
