var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold the chart
var svg = d3.select(".chart")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

// Append an SVG group
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Initial Params
var chosenXAxis = "Happiness_score";

// function used for updating x-scale var upon click on axis label
function xScale(Merged, chosenXAxis) {
  // create scales
  var xLinearScale = d3.scaleLinear()
    .domain([d3.min(Merged, d => d[chosenXAxis]),
      d3.max(Merged, d => d[chosenXAxis])
    ])
    .range([0, width]);

  return xLinearScale;

}

// function used for updating xAxis var upon click on axis label
function renderAxes(newXScale, xAxis) {
  var bottomAxis = d3.axisBottom(newXScale);

  xAxis.transition()
    .duration(1500)
    .call(bottomAxis);

  return xAxis;
}

// function used for updating circles group with a transition to new circles
function renderCircles(circlesGroup, newXScale, chosenXAxis) {

  circlesGroup.transition()
    .duration(1500)
    .attr("cx", d => newXScale(d[chosenXAxis]));

  return circlesGroup;
}

// function used for updating circles group with new tooltip
function updateToolTip(chosenXAxis, circlesGroup) {

  var label;

  if (chosenXAxis === "Happiness_score") {
    label = "Happiness Score:";
  }
  else {
    label = "Social Support:";
  }

  var toolTip = d3.tip()
    .attr("class", "tooltip")
    .offset([80, -60])
    .html(function(d) {
      return (`${d.country}<br>${label} ${d[chosenXAxis]}`);
    });

  circlesGroup.call(toolTip);

  circlesGroup.on("mouseover", function(data) {
    toolTip.show(data);
  })
   
    .on("mouseout", function(data, index) {
      toolTip.hide(data);
    });

  return circlesGroup;
}

// Retrieve data from the CSV file and execute everything below
d3.csv("data/Merged.csv").then(function(Merged, err) {
  if (err) throw err;

  Merged.forEach(function(data) {
    data.Happiness_score = +data.Happiness_score;
    data.life_expectancy = +data.life_expectancy;
    data.Social_support = +data.Social_support;
  });

  var xLinearScale = xScale(Merged, chosenXAxis);

  // Create y scale function
  var yLinearScale = d3.scaleLinear()
    .domain([50, d3.max(Merged, d => d.life_expectancy)])
    .range([height, 0]);

  // Create initial axis functions
  var bottomAxis = d3.axisBottom(xLinearScale);
  var leftAxis = d3.axisLeft(yLinearScale);

  // append x axis
  var xAxis = chartGroup.append("g")
    .classed("x-axis", true)
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis);

  // append y axis
  chartGroup.append("g")
    .call(leftAxis);

  // append initial circles
  var circlesGroup = chartGroup.selectAll("circle")
    .data(Merged)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d[chosenXAxis]))
    .attr("cy", d => yLinearScale(d.life_expectancy))
    .attr("r", 10)
    .attr("fill", "pink")
    .attr("opacity", ".5");

  // Create group for two x-axis labels
  var labelsGroup = chartGroup.append("g")
    .attr("transform", `translate(${width / 2}, ${height + 20})`);

  var HappinessScoreLabel = labelsGroup.append("text")
    .attr("x", 0)
    .attr("y", 20)
    .attr("value", "Happiness_score") // value to grab for event listener
    .classed("active", true)
    .text("Happiness Score");

  var SocialSupportLabel = labelsGroup.append("text")
    .attr("x", 0)
    .attr("y", 40)
    .attr("value", "Social_support") // value to grab for event listener
    .classed("inactive", true)
    .text("Social Support");

  // append y axis
  chartGroup.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .classed("axis-text", true)
    .text("Life Expectancy");

  // updateToolTip function 
  var circlesGroup = updateToolTip(chosenXAxis, circlesGroup);

  // x axis labels event listener
  labelsGroup.selectAll("text")
    .on("click", function() {
      // get value of selection
      var value = d3.select(this).attr("value");
      if (value !== chosenXAxis) {

        // replaces chosenXAxis with value
        chosenXAxis = value;

        // updates x scale for new data
        xLinearScale = xScale(Merged, chosenXAxis);

        // updates x axis with transition
        xAxis = renderAxes(xLinearScale, xAxis);

        // updates circles with new x values
        circlesGroup = renderCircles(circlesGroup, xLinearScale, chosenXAxis);

        // updates tooltips with new info
        circlesGroup = updateToolTip(chosenXAxis, circlesGroup);

        // changes classes to change bold text
        if (chosenXAxis === "Social_support") {
          SocialSupportLabel
            .classed("active", true)
            .classed("inactive", false);
          HappinessScoreLabel
            .classed("active", false)
            .classed("inactive", true);
        }
        else {
          SocialSupportLabel
            .classed("active", false)
            .classed("inactive", true);
          HappinessScoreLabel
            .classed("active", true)
            .classed("inactive", false);
        }
      }
    });
}).catch(function(error) {
  console.log(error);
});
