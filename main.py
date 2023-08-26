import folium 

try:
    ## STEP 1 starting point: create start of our main program
    if __name__ == "__main__": 
    
        #STEP 2 create variables
        ##filename and the ".html" extension.
        map_filePath = "index.html" 
        #[googlemaps>>rightclick>>copytoclipboard] NAIROBI
        nairobi = [-1.2894289419116627, 36.82331216592736]
        jkia = [-1.3303346965969862, 36.925087072124406]
        fourPoints =[-1.3410409318472776, 36.917421270589784]
        crownePlaza = [-1.3407330369286858, 36.91304988482857]
        marker_radii = 15
        #line coordinates are from jkia to fourPoints to crownePlaza
        lineCoords = [jkia, fourPoints, crownePlaza]
        #define the polyline cordinates. 1st coord == last coord to close the polygon
        # polygonCoords = [
        #     [-1.3415675090318926, 36.90547935424791],
        #     [-1.3418697280877727, 36.91608740413051],
        #     [-1.334176867689621, 36.915949994150644],
        #     [-1.3318690049040638, 36.90591906615285],
        #     [-1.3415675090318926, 36.90547935424791],
        # ]

        # polygon_lines = [
        #     [polygonCoords[i], polygonCoords[i+1]] for i in range(len(polygonCoords) -1)
        # ]
        
        #STEP 3 create folium map
        foliumMap = folium.Map(nairobi, zoom_start = 12)

        #Step 4 CREATE A leaflet circle(a marker) that takes six arguments;
        folium.vector_layers.Circle(
            location = jkia, 
            tooltip = f"This Cicle marker has radius {marker_radii}",  #f string
            #radius of the cicle marker
            radius = marker_radii,
            color = "red",
            fill = True,
            fill_color = "yellow"
            ).add_to(foliumMap)
            #add_to() method -- adds the marker to the map at the specified location
        #step 5 CREATE A leaflet CircleMarker(a marker) that takes six arguments;
        folium.CircleMarker(
            location = fourPoints,
            radius=marker_radii,
            tooltip="Four Points by Sheraton Nairobi Airport",
            color="#3186cc",
            fill=True,
            fill_color="#3186cc",
            ).add_to(foliumMap)

            #step 6 CREATE A leaflet location_Marker(a marker) that takes six arguments;
        folium.Marker(
            location=crownePlaza,
            tooltip = "Crowne Plaza Nairobi Airport",
            icon=folium.Icon(color="green"),
            ).add_to(foliumMap)

            # #step 7 add a line to folium map
        # folium.PolyLine(
        #     lineCoords,
        #     color = "blue",
        #     weight = "5",#the width of the line: does not scale larger, only readjusts
        #     opacity = 0.8, 
        # ).add_to(foliumMap)

            #step 8 adds a closed polygon to folium map
            #stores the polygon as lines that can be 
            #used to check for polygon intersection
        # for line in polygon_lines:
        #     folium.PolyLine(
        #         line, #cordinates of polygon are in polygon_lines variable
        #         color = "red",
        #         weight = "5",#the width of the line: does not scale larger, only readjusts
        #         opacity = 0.8,
        #     ).add_to(foliumMap)

    #store map to a html file: where we can see our map
    foliumMap.save(map_filePath)

    print("Program run succesfuly :), Navigate to your root directory open the 'index.html' file ")

except: 
    print("Check your python console for errors!!")