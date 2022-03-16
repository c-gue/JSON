#Process the JSON file named univ.json. Create 3 maps per instructions below.
#The size of the point on the map should be based on the size of total enrollment. Display only those schools 
#that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons (refer to valueLabels.csv file)
#The school name and the specific map criteria should be displayed when you hover over it.
#(For example for Map 1, when you hover over Baylor, it should display "Baylor University, 81%")
#Choose appropriate tiles for each map.
# #Map 3) Total price for in-state students living off campus over $50,000

import json

infile = open('univ.json','r')

fm_data = json.load(infile)

total_enroll,lons,lats,hover_text,school,off_campus = [],[],[],[],[],[]

for fm in fm_data:
    if fm["NCAA"]["NAIA conference number football (IC2020)"] == 104 or fm["NCAA"]["NAIA conference number football (IC2020)"] == 107 or fm["NCAA"]["NAIA conference number football (IC2020)"] == 108 or fm["NCAA"]["NAIA conference number football (IC2020)"] == 127 or fm["NCAA"]["NAIA conference number football (IC2020)"] == 130:
        if fm["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] != None:
            if fm["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] > 50000:
                institution = fm["instnm"]
                lon = fm["Longitude location of institution (HD2020)"]
                lat = fm["Latitude location of institution (HD2020)"]
                enrollment = fm["Total  enrollment (DRVEF2020)"]
                school.append(institution)
                lons.append(lon)
                lats.append(lat)
                total_enroll.append(enrollment)


                total_price = fm["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]
                off_campus.append(total_price)
                hover_text.append(institution+', '+'$'+str(total_price))

print(school)
print(off_campus)
print(hover_text)

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {'type':'scattergeo',
    'text':hover_text,
    'lon':lons,
    'lat':lats,
    'marker':{
        'size':[i/1000 for i in total_enroll],
        'color':total_enroll,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Total Enrollment'}
    },
    }]

my_layout = Layout(title='Total price for in-state students living off campus over $50,000')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='off_campus_price.html')
