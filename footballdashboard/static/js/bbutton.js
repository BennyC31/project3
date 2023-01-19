const samples_url = "https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json";

let data = null
function barChart(s_id){
    let samples = data.samples;
    let bar_data = samples.filter(s => s.id == s_id);
    let sample_id = bar_data[0];
    let sample_values = sample_id.sample_values;
    let otu_ids = sample_id.otu_ids;
    let otu_labels = sample_id.otu_labels;

    let hbardata = [{
        x: sample_values.slice(0,10).reverse(),
        y: otu_ids.slice(0,10).map(otu_id => `OTU ${otu_id}`).reverse(),
        type: 'bar',
        text: otu_labels.reverse(),
        orientation: 'h'

    }];
    let layout = {
        height: 400,
        width: 300
    };
    Plotly.newPlot("bar",hbardata,layout);
};

function bubbleChart(s_id){
    let samples = data.samples;
    let bubble_data = samples.filter(s => s.id == s_id);
    let sample_id = bubble_data[0];
    let sample_values = sample_id.sample_values;
    let otu_ids = sample_id.otu_ids;
    let otu_labels = sample_id.otu_labels;

    let bubbledata = [{
        x: otu_ids,
        y: sample_values,
        mode: 'markers',
        text: otu_labels,
        marker: {
            size: sample_values,
            color: otu_ids,
            colorscale: 'Earth'
        }

    }];
    let layout = {
        height: 600,
        width: 1000,
        xaxis: {title: "OTU ID"}
    };
    Plotly.newPlot("bubble",bubbledata,layout);
};



function gaugeChart(s_id){
    let demo_meta_data = data.metadata;
    let meta_data = demo_meta_data.filter(m => m.id == s_id)[0];
    let wfreq = meta_data.wfreq;

    let gaugedata = [{
        domain: { x: [0, 1], y: [0, 1] },
        value: wfreq,
        title: { text: "Belly Button Washing Frequency" },
        type: "indicator",
        mode: "gauge+number",
    }];
    let layout = {
        height: 500,
        width: 500,
        margin: {t: 0, b: 0}
    };
    Plotly.newPlot("gauge",gaugedata,layout);
};

function demoInfo(s_id){
    let demo_meta_data = data.metadata;
    let meta_data = demo_meta_data.filter(m => m.id == s_id)[0];
    let demo_info = d3.select("#sample-metadata");
    let id = meta_data.id;
    let ethnicity = meta_data.ethnicity;
    let gender = meta_data.gender;
    let age = meta_data.age;
    let location = meta_data.location;
    let bbtype = meta_data.bbtype;
    let wfreq = meta_data.wfreq;
    demo_info.html("");
    demo_info.append('h6').text(`id: ${id}`);
    demo_info.append('h6').text(`ethnicity: ${ethnicity}`);
    demo_info.append('h6').text(`gender: ${gender}`);
    demo_info.append('h6').text(`age: ${age}`);
    demo_info.append('h6').text(`location: ${location}`);
    demo_info.append('h6').text(`bbtype: ${bbtype}`);
    demo_info.append('h6').text(`wfreq: ${wfreq}`);
};

function optionChanged(s_id) {
    barChart(s_id);
    bubbleChart(s_id);
    demoInfo(s_id);
    gaugeChart(s_id);

}

function updateDashboard(){
    let names = data.names;
    let subjdropdownMenu = d3.select("#selDataset")
    let dataset = subjdropdownMenu.property("value");
    dataset = names;
    for(let i=0; i<names.length;i++){
        let s_id = names[i]
        subjdropdownMenu.append('option').text(s_id).property('value',s_id);

    }
    let init_id = subjdropdownMenu.property("value");
    barChart(init_id);
    bubbleChart(init_id);
    demoInfo(init_id);
    gaugeChart(init_id);
};

function init() {
    d3.json(samples_url).then(function (tmp_data){
        data = tmp_data
        updateDashboard();
    })
}

init();
