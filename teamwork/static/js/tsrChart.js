// ======================================================
// analysis-chart.js
// ======================================================

//var total_students = document.getElementById("total_students").value;

//variable theMemberNames that gets element names
//that is a list of tuples (name, len(name), ...)
var theMemberNames = document.getElementById("names").value;
// var mem_percentages = document.getElementById("mem_percentages");
var chosen_tsr = document.getElementById("chosen_tsr").value;

console.log(theMemberNames);
console.log(mem_percentages);
console.log(chose_tsr);

var colors = document.getElementById("colors").value;
	// #FFB2B2 - pink
	// #B2B2FF - light blue
	// #B2D8B2 - light green
	// #D8B2D8 - light purple
	// #FFE4B2 - light orange
	// #800000 - maroonish
	// #9DEAE7 - tealish
	// #549ED6 - darkish blue
	//var colors = ["#FFB2B2", "#B2B2FF", "#B2D8B2", "#D8B2D8", "#FFE4B2", "#800000","##9DEAE7", "#549ED6"];

// analysis chart options

var analysisOptions = {

    scaleFontColor: "#FFB2B2",
    scaleFontFamily: "'Arial'",
    scaleFontSize: 12,
    scaleFontStyle: "normal",
    scaleGridLineWidth: 1,
    barShowStroke: !0,
    barStrokeWidth: 2,
    barValueSpacing: 5,
    barDatasetSpacing: 1,
    animation: !0,
    animationSteps: 60,
    animationEasing: "easeOutQuart",

}

// analysis chart data

var analysisData = [];

for (var i = 0; i < theMemberNames.length; i++) {
//loop through the members and append a dictionary to the array
//theMembers[i] should be the tuple
//the 0th element should be the name, and the 1st should be len(name)

	analysisData.append({

	label : theMemberNames[i].0,
	value : theMemberNames[i].1,
	color : colors[i]
		
	});

}

/*
    {
        label : 'IN',
		value: studs_in_pro,
		color: "#1789D4"
	},
	{
        label : 'OUT',
		value : studs_not_in_pro,
		color : "#CB4B16"
	}*/


console.log(analysisData);


//Get the context of the Doughnut Chart canvas element we want to select
var ctx = document.getElementById("barChart").getContext("2d");

// Create the Doughnut Chart
var theAnalysisChart = new Chart(ctx).Bar(analysisData, analysisOptions);
