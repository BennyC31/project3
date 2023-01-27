var myMap = L.map("map", {
    center: [
        37.09, -95.71
    ],
    zoom: 5
});

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap)

d3.json("/locdata").then(function (tmp_data) {
    data = tmp_data[1]
    // data1 = sum_data
    console.log(data);
    createMarkers(data);
})


function createMarkers(teamLocs) {
    console.log('in create markers:')
    for (var i = 0; i < teamLocs.length; i++) {
        lon = teamLocs[i]['lon']
        lat = teamLocs[i]['lat']
        loc = teamLocs[i]['football_location']
        state_abrv = teamLocs[i]['state_code']
        team_loc = teamLocs[i]['team_location']
        team_name = teamLocs[i]['team_name']
        conf = teamLocs[i]['conference']
        div = teamLocs[i]['division']
        tot_w = teamLocs[i]['w']
        tot_l = teamLocs[i]['l']
        tot_t = teamLocs[i]['t']
        tot_pf = teamLocs[i]['pf']
        tot_pa = teamLocs[i]['pa']
        if (team_name == 'Jets') {
            // lat = 40.735657;
            // lon = -74.17236;
            lat = 40.835657;
            lon = -74.27236;
        }
        if (team_name == 'Chargers') {
            // lat = 34.05369;
            // lon = -118.24277;
            lat = 34.15369;
            lon = -118.34277;
        }


        var color = 'blue'
        if (conf == 'American') {
            color = 'red'
        }

        L.circle([lat, lon], 25000, { color: color, opacity: .5 }).addTo(myMap).bindPopup(
            `<h3>${team_name}</h3><hr>
            <h5>team location: ${team_loc}</h5>
            <h5>football location: ${loc}</h5>
            <h5>state: ${state_abrv}</h5>
            <h5>conference: ${conf}</h5>
            <h5>division: ${div}</h5><hr>
            <h5>10 Year Summary</h5>
            <h6>W: ${tot_w} L: ${tot_l} T: ${tot_t} PF: ${tot_pf} PA: ${tot_pa}</h6>`);
    }
    // Create a legend to display information about our map.
    var info = L.control({
        position: "topright"
    });

    // When the layer control is added, insert a div with the class of "legend".
    info.onAdd = function () {
        var div = L.DomUtil.create("div", "legend");
        return div;
    };
    // Add the info legend to the map.
    info.addTo(myMap);

    updateLegend();
}

function updateLegend() {
    document.querySelector(".legend").innerHTML = [
        "<p><strong>2012 - 2021</strong></p>",
        "<h6 class='American'>American Conference</h6>",
        "<h6 class='National'>National Conference</h6>"
    ].join("");
}