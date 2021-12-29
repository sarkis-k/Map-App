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

fgv = folium.FeatureGroup(name="Volcanoes")


#for basic and advanced html popup
# for coorX, coorY, nm, el in zip(lat,lon,mt_name, elev):
# 	iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=100)
# 	fg.add_child(folium.Marker(location=[coorX,coorY], popup=folium.Popup(iframe), icon=folium.Icon(color='red')))
#icon=folium.Icon(color=(lambda el: "red" if el>2000 else "green")

for coorX, coorY, nm, el in zip(lat,lon,mt_name, elev):
	fgv.add_child(folium.CircleMarker(
		location=[coorX,coorY], 
		radius=6,
		popup=str(el)+" m",
		fill_color=color_producer(el),
		color="gray",
		fill_opacity=0.7 ))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
	style_function=lambda x: {"fillColor":"yellow" if x["properties"]["POP2005"]<10000000 else "green" if 10000000 <=x["properties"]["POP2005"]<100000000 else "blue"}))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
