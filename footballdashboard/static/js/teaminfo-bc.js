
let data = null
var cur_year = []
function teamInfo(s_id){
    let conf = ''
    let div = ''
    let loc = ''
    let team_name = ''
    let leag = ''
    let demo_info = d3.select("#sample-metadata");
    for (let i=0;i<cur_year.length;i++) {
        test_name = cur_year[i]['team_name']
        if(test_name == s_id){
            conf = cur_year[i]['conference']
            div = cur_year[i]['division']
            loc = cur_year[i]['team_location']
            team_name = cur_year[i]['team_name']
            leag = cur_year[i]['leagabrv']
        }
    }

    demo_info.html("");
    demo_info.append('h6').text(`conference: ${conf}`);
    demo_info.append('h6').text(`division: ${div}`);
    demo_info.append('h6').text(`location: ${loc}`);
    demo_info.append('h6').text(`name: ${team_name}`);
    demo_info.append('h6').text(`league: ${leag}`);
};

function optionChanged(s_id) {
    teamInfo(s_id);

}

function updateDashboard(){
    for (let i=0;i<data.length;i++) {
        let test_year = data[i]['leag_year']
        if(test_year == 2021){
            cur_year.push(data[i])
        }
    }
    console.log(cur_year)
    let subjdropdownMenu = d3.select("#selDataset")
    for(let i=0; i<cur_year.length;i++){
        let s_id = cur_year[i]['team_name']
        subjdropdownMenu.append('option').text(s_id).property('value',s_id);

    }
    let init_id = subjdropdownMenu.property("value");

    teamInfo(init_id);
};

function init() {
    d3.json("/teamdata").then(function (tmp_data){
        data = tmp_data
        console.log(data);
        updateDashboard();
    })
    

}

init();