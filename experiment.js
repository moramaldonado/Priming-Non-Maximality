var shuffleSequence = seq("agreement",
                          "instr",
                          "practique",
                         "quest");

var showProgressBar = false;

var pageTitle= "Expe2";

var defaults = [
    "Question", {hasCorrect: true},
    "Message", {hideProgressBar: true},
    "Sentence", {hideProgressBar: true, transfer: 500},
    "Form", {hideProgressBar: true,continueOnReturn: true,saveReactionTime: true},
    "PictureAccept", {presentAsScale: true,hideProgressBar: true},
    "SubHtmlFlash", {presentAsScale: true, presentHorizontally: false, as: ["True", "False"]}
  ];


var items = [
    ['agreement', "Form3", {html: {include: 'agreement_FR.html'}}],
    ['instr',"Message", {html: {include: 'instructions.html'}}],
    ['practique', "Sentence", {html: '<center>HOLA</center>'},
     "SubHtmlFlash", {html:"<center> <img src='http://cogexpe.scicog.fr/PSIM/0_haut_carre_Control.png' border='2'></center>", q:"Les carres sont en bas.", hasCorrect:1}],
    ['quest', "Form3", {html:{include: 'questionary.html'}}]];
