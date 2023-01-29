
let data = null
let y_data = null
var cur_year = []
function teamInfo(s_id) {
    let conf = ''
    let div = ''
    let loc = ''
    let team_name = ''
    let leag = ''
    let team_info = d3.select("#sample-metadata");
    for (let i = 0; i < data.length; i++) {
        test_name = data[i]['team_name']
        if (test_name == s_id) {
            conf = data[i]['conference']
            div = data[i]['division']
            loc = data[i]['team_location']
            team_name = data[i]['team_name']
            leag = 'NFL'
        }
    }

    team_info.html("");
    team_info.append('h6').text(`conference: ${conf}`);
    team_info.append('h6').text(`division: ${div}`);
    team_info.append('h6').text(`location: ${loc}`);
    team_info.append('h6').text(`name: ${team_name}`);
    team_info.append('h6').text(`league: ${leag}`);
};

function optionChanged(s_id) {
    let team_id = get_team_id(s_id);
    console.log(team_id);
    teamInfo(s_id);
    barChart(team_id)
    gaugeChart(team_id);
}

function get_team_id(team_name) {
    team_id = 'NFLTeam1'
    for (let i = 0; i < data.length; i++) {
        if (team_name == data[i]['team_name']) {
            team_id = data[i]['team_id']
        }
    }
    return team_id
};

function updateDashboard() {
    let subjdropdownMenu = d3.select("#selDataset")
    for (let i = 0; i < data.length; i++) {
        let s_id = data[i]['team_name']
        subjdropdownMenu.append('option').text(s_id).property('value', s_id);

    }
    let init_id = subjdropdownMenu.property("value");
    let team_id = get_team_id(init_id);
    console.log(team_id);
    teamInfo(init_id);
    barChart(team_id);
    gaugeChart(team_id);
    bubbleChart();

};
function bubbleChart() {
    let stats = data;
    let teams = []
    let pfs = []
    let pas = []
    for (var i = 0; i < stats.length; i++) {
        teams.push(stats[i]['team_name']);
        pfs.push(stats[i]['pf']);
        pas.push(stats[i]['pa']);
    };

    var trace1 = {
        x: teams,
        y: pfs,
        mode: 'markers',
        type: 'scatter',
        name: 'PF',
        marker: { size: 12 }
    };

    var trace2 = {
        x: teams,
        y: pas,
        mode: 'markers',
        type: 'scatter',
        name: 'PA',
        marker: { size: 12, color: 'rgb(255, 0, 0)' }
    };

    var bar_data = [trace1, trace2];

    var layout = {
        xaxis: {
            range: [-1, 32]
        },
        yaxis: {
            range: [0, 6000]
        },
        title: 'Total Points For and Against'
    };
    var config = {responsive: true}

    Plotly.newPlot('bubble', bar_data, layout, config);
}

function gaugeChart(team_id) {
    let stats = data;
    let ws = 0;
    for (var i = 0; i < stats.length; i++) {
        if (team_id == stats[i]['team_id']) {
            ws = stats[i]['w']
            break;
        }
    }
    gaugedata = [
        {
            type: "indicator",
            mode: "number+gauge",
            value: ws,
            delta: { reference: 80 },
            domain: { x: [0.25, 1], y: [0.7, 0.9] },
            title: { text: "Total Wins" },
            gauge: {
                shape: "bullet",
                axis: { range: [null, 160] },
                threshold: {
                    line: { color: "yellow", width: 2 },
                    thickness: 0.75,
                    value: 80.5
                },
                steps: [
                    { range: [0, 80], color: "red" },
                    { range: [81, 160], color: "green" }
                ],
                bar: { color: "black" }
            }
        }
    ];
    let layout = {
        // autosize: true,
        height: 100,
        width: 400,
        margin: { t: 0, r: 0, l: 25, b: 0 }
    };
    var config = {responsive: true}

    Plotly.newPlot("gauge", gaugedata, layout, config);
};

function barChart(team_id) {
    let stats = y_data;
    let w = []
    let l = []
    let t = []
    let years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
    for (var i = 0; i < stats.length; i++) {
        if (team_id == stats[i]['team_id']) {
            w.push(stats[i]['w'])
            l.push(stats[i]['l'])
            t.push(stats[i]['t'])
        }
    }
    var trace1 = {
        x: years,
        y: w,
        type: 'bar',
        name: 'Wins',
        marker: {
            color: 'rgb(49,130,189)',
            opacity: 0.7,
        }
    };

    var trace2 = {
        x: years,
        y: l,
        type: 'bar',
        name: 'Losses',
        marker: {
            color: 'rgb(255, 0, 0)',
            opacity: 0.5
        }
    };

    var trace3 = {
        x: years,
        y: t,
        type: 'bar',
        name: 'Ties',
        marker: {
            color: 'rgb(255, 153, 0)',
            opacity: 0.5
        }
    };
    var bar_data = [trace1, trace2, trace3];

    var layout = {
        // title: 'Win/Loss/Tie',
        // autosize: true,
        // height: 400,
        // width: 400,
        xaxis: {
            tickangle: -45
        },
        barmode: 'group'
    };
    var config = {responsive: true}

    Plotly.newPlot('bar', bar_data, layout, config);

}
function init() {
    d3.json("/locdata").then(function (tmp_data) {
        y_data = tmp_data[2]
        data = tmp_data[1]
        // console.log(data);
        updateDashboard();
    })
}

init();