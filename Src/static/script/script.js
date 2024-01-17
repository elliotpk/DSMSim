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

