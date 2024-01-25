
function changeClass0(){
    var element = document.querySelector("#nr0");
    element.classList.replace("options", "selected");
    var button = document.querySelector("#button0");
    button.classList.replace("options", "selected");

    var element2 = document.querySelector("#nr1");
    element2.classList.replace("selected", "options");
    var button1 = document.querySelector("#button1");
    button1.classList.replace("selected", "options");

    var element3 = document.querySelector("#nr2");
    element3.classList.replace("selected", "options");
    var button2 = document.querySelector("#button2");
    button2.classList.replace("selected", "options");
}

function changeClass1(){
    var element = document.querySelector("#nr1");
    element.classList.replace("options", "selected");
    var button1 = document.querySelector("#button1");
    button1.classList.replace("options", "selected");

    var element2 = document.querySelector("#nr0");
    element2.classList.replace("selected", "options");
    var button = document.querySelector("#button0");
    button.classList.replace("selected", "options");

    var element3 = document.querySelector("#nr2");
    element3.classList.replace("selected", "options");
    var button2 = document.querySelector("#button2");
    button2.classList.replace("selected", "options");
}

function changeClass2(){
    var element = document.querySelector("#nr2");
    element.classList.replace("options", "selected");
    var button2 = document.querySelector("#button2");
    button2.classList.replace("options", "selected");

    var element2 = document.querySelector("#nr0");
    element2.classList.replace("selected", "options");
    var button = document.querySelector("#button0");
    button.classList.replace("selected", "options");

    var element3 = document.querySelector("#nr1");
    element3.classList.replace("selected", "options");
    var button1 = document.querySelector("#button1");
    button1.classList.replace("selected", "options");
    
}

//start coordinates for the map //its coordinates for stockholm
var start = { lat: 59.326038, lng:17.8172531};

let directionsService, directionsRenderer

//initialize the Google Map
function initMap(){
    
var mapOptions = {
    center: start,
    zoom: 4,
};

map = new google.maps.Map(document.getElementById('googleMap'), mapOptions);

directionsService = new google.maps.DirectionsService()
directionsRenderer = new google.maps.DirectionsRenderer()
directionsRenderer.setMap(map)

calcRoute();
}

//Make a route and then display it on the map
function calcRoute(){
  var source ="Linköping";
  var destination = "Stockholm";

  let req = {
    origin: source,
    destination: destination,
    travelMode: "DRIVING",
  };
  directionsService.route(req,function(result,status){
    if(status == "OK"){
        directionsRenderer.setDirections(result)
    }
  })
}

function sort(){
  selectElement = document.querySelector('#checkbox');
  output = selectElement.value;
  // console.log(output);
}