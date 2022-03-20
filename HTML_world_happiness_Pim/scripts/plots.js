// Initializes the page with a default plot
function init() {
  data = [{
    x: ["Finland","Denmark","Norway","Iceland","Netherlands","Switzerland","Sweden","New Zealand","Canada","Austria"],
    y: [7.769,7.6,7.554,7.494,7.488,7.48,7.343,7.307,7.278,7.246],
    type: "bar" }];



  Plotly.newPlot("plot", data);
}




// Call updatePlotly() when a change takes place to the DOM
d3.selectAll("#selDataset").on("change", updatePlotly);

// This function is called when a dropdown menu item is selected
function updatePlotly() {
  // Use D3 to select the dropdown menu
  var dropdownMenu = d3.select("#selDataset");
  // Assign the value of the dropdown menu option to a variable
  var dataset = dropdownMenu.property("value");

  // Initialize x and y arrays


  var data = [];
  
 

  if (dataset === 'dataset1') {

         

    data = {
      x: ["Finland","Denmark","Norway","Iceland","Netherlands","Switzerland","Sweden","New Zealand","Canada","Austria"],
      y: [7.769,7.6,7.554,7.494,7.488,7.48,7.343,7.307,7.278,7.246],
      type: "bar"
    };


  }
  

  
  else if (dataset === 'dataset2') {

    
    
    data = {
      x:["Finland","Denmark","Norway","Iceland","Netherlands","Switzerland","Sweden","New Zealand","Canada","Austria"],
      y: [81.9,80.9,82.4,83,82.3,83.8,82.8,82.3,82.4,81.5],
      type: "bar"
    };

  

    
  }
  

  else if (dataset === 'dataset3'){

        // Create our first trace
        var GDP = {
          x: ["Finland","Denmark","Norway","Iceland","Netherlands","Switzerland","Sweden","New Zealand","Canada","Austria"],
          y: [1.34, 1.383, 1.488, 1.38, 1.396, 1.452, 1.387, 1.303, 1.365, 1.376],
          type: "scatter"
        };

        // Create our second trace
        var Social_support = {
          x: ["Finland","Denmark","Norway","Iceland","Netherlands","Switzerland","Sweden","New Zealand","Canada","Austria"],
          y: [1.587,1.573,1.582,1.624,1.522,1.526,1.487,1.557,1.505,1.475],
          type: "scatter"
        };

        // Create our third trace
        var Freedom = {
          x: ["Finland","Denmark","Norway","Iceland","Netherlands","Switzerland","Sweden","New Zealand","Canada","Austria"],
          y: [0.596,0.592,0.603,0.591,0.557,0.572,0.574,0.585,0.584,0.532],
          type: "scatter"
        };



        // The data array consists of both traces
        data = [GDP, Social_support, Freedom];

        // Note that we omitted the layout object this time
        // This will use default parameters for the layout
        Plotly.newPlot("plot", data);
        
        
  }

  //Plotly.newPlot("plot", data, layout);
  // Note the extra brackets around 'x' and 'y'
  //Plotly.restyle("plot", "x", [x]);
  //Plotly.restyle("plot", "y", [y]);
  //Plotly.restyle("plot", "data", [data]);
  //Plotly.restyle("plot", "y", [y]);
  //Plotly.restyle("plot", "layout", [layout]);
  //Plotly.restyle("plot", "x", [data.x]);
  //Plotly.restyle("plot", "y", [data.y]);
  //Plotly.restyle("plot", "type", [data.type]);
  Plotly.restyle("plot", "x", [data.x]);
  Plotly.restyle("plot", "y", [data.y]);
  Plotly.restyle("plot", "type", [data.type]);
  
  if (dataset === 'dataset1'){
  Plotly.deleteTraces("plot", [1,2]);
  }

  if (dataset === 'dataset2'){
    Plotly.deleteTraces("plot", [1,2]);
    }

}

init();

