var shuffleSequence = seq("agreement",
                          "instr",
                          "practice",
                          "quest",
                          "sr",
                         "code")

var showProgressBar = false;

var pageTitle= "Experiment_Linguistics";

function generateRandomNumber(){
    var num = Math.floor(Math.random()*58+40);
    var myArray = ['R', 'S', 'X', 'U','V'];   
    var rand = myArray[Math.floor(Math.random() * myArray.length)];
    var myArray2 = ['I', 'O', 'E', 'U'];   
    var rand2 = myArray2[Math.floor(Math.random() * myArray2.length)];
    var myArray3 = ['Y', 'Z', 'W'];   
    var rand3 = myArray3[Math.floor(Math.random() * myArray3.length)];
    var num2 = Math.floor(Math.random()*6+1);

    var n = String(rand)+String(num)+String(rand3)+String(num2)+String(rand2);

return n;
}

var manualSendResults = true;
var defaults = [
    "Question", {hasCorrect: true},
    "Message", {hideProgressBar: true},
    "Sentence", {hideProgressBar: true, transfer: 2000},
    "Form", {hideProgressBar: true,continueOnReturn: true,saveReactionTime: true},
    "NewForm", {hideProgressBar: true,continueOnReturn: true,saveReactionTime: true},
    "PictureAccept", {presentAsScale: true,hideProgressBar: true},
    "SubHtmlFlash", {presentAsScale: true, presentHorizontally: false, as: ["True", "False"]},
    "Code", {hideProgressBar: true,transfer: null}];


var items = [
    ['agreement', "NewForm", {html: {include: 'agreement_EN.html'}}], 
    ['instr',"NewMessage", {html: {include: 'instructions.html'}}],
    ['practice', "Sentence", {html: '<center>Between four and ten dots are below the line.</center>'},
     "SubHtmlFlash", {html:"<center> <img src='https://dl.dropboxusercontent.com/u/13340774/Images/False_A_dots_blue_square_below_.png' border='2'></center>", q:"Between four and ten dots are below the line.", hasCorrect:1}],
    ["quest", "NewForm", {html:{include: 'questionary.html'}}],
    ["sr", "__SendResults__", { }],
    ["code", "Code", {html: "<h2> Code </h2><br>" + generateRandomNumber()}],    
    
    
];
