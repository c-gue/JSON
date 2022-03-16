#Process the JSON file named univ.json. Create 3 maps per instructions below.
#The size of the point on the map should be based on the size of total enrollment. Display only those schools 
#that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons (refer to valueLabels.csv file)
#The school name and the specific map criteria should be displayed when you hover over it.
#(For example for Map 1, when you hover over Baylor, it should display "Baylor University, 81%")
#Choose appropriate tiles for each map.
#Map 1) Graduation rate for Women is over 50%

import json

infile = open('univ.json','r')

fm_data = json.load(infile)

total_enroll,lons,lats,hover_text,school,female_grad = [],[],[],[],[],[]

for fm in fm_data:
    if fm["NCAA"]["NAIA conference number football (IC2020)"] == 104 or fm["NCAA"]["NAIA conference number football (IC2020)"] == 107 or fm["NCAA"]["NAIA conference number football (IC2020)"] == 108 or fm["NCAA"]["NAIA conference number football (IC2020)"] == 127 or fm["NCAA"]["NAIA conference number football (IC2020)"] == 130:
        if fm["Graduation rate  women (DRVGR2020)"] > 50:
            institution = fm["instnm"]
            lon = fm["Longitude location of institution (HD2020)"]
            lat = fm["Latitude location of institution (HD2020)"]
            enrollment = fm["Total  enrollment (DRVEF2020)"]
            school.append(institution)
            lons.append(lon)
            lats.append(lat)
            total_enroll.append(enrollment)


            graduation = fm["Graduation rate  women (DRVGR2020)"]
            female_grad.append(graduation)
            hover_text.append(institution+', '+str(graduation)+'%')

print(school)
print(female_grad)
print(hover_text)

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {'type':'scattergeo',
    'text':hover_text,
    'lon':lons,
    'lat':lats,
    'marker':{
        'size':[i/2500 for i in total_enroll],
        'color':total_enroll,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Total Enrollment'}
    },
    }]

my_layout = Layout(title='Graduation rate for Women over 50%')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='female_graduation.html')
