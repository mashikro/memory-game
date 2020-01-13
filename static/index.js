"use strict";

let currentWord = null;
let currentLevel = 0;
let wrongGuesses = 0;

function clearTextArea() {
  $("#textArea").val("");
}
//set up
$(document).ready(() => {
  const playButton = $("#playButton");
  const instrButton = $("#instructionsButton");

  $("#instructions").hide();
  $("#displayed-word").hide();
  $("#word-form").hide();

  instrButton.on("click", () => {
    $("#instructions").fadeIn();
  });

  playButton.on("click", () => {
    $("#instructions").hide();
    $("#instructionsButton").fadeOut();
    $("#playButton").fadeOut(); // <--- this is not working
    getWord();
  });
  // console.log("Is this working????");
});

// func makes ajax request to get word
function getWord() {
  const levelData = {
    level: currentLevel
  };

  $.getJSON("/play.json", levelData, data => {
    //write a func to show word
    // console.log("is data coming in", data);

    currentWord = data.word;

    $("#displayed-word").html(data.word);

    $("#displayed-word").fadeIn();

    // timer starts after the word comes in from server
    setTimeout(function() {
      $("#displayed-word").hide();
    }, 3000);

    setTimeout(function() {
      $("#word-form").show();
      $("#textArea").focus();
    }, 3100);
  });
}

function endGame() {
  alert("End of Game!");
  // $("#instructions").hide();
  $("#instructionsButton").show();
  $("#playButton").show();
  $("#word-form").hide();
  currentLevel = 0;
  wrongGuesses = 0;
}

const checkState = () => {
  if (currentLevel == 12 || wrongGuesses == 3) {
    console.log("does this work??");
    endGame();
  } else {
    getWord();
    clearTextArea();
  }
};
//write a func to validate user input
function validateWord() {
  // console.log("Are we getting here?");
  $("#word-form").hide();
  if (document.myForm.userInput.value == currentWord) {
    const displayLevel = +currentLevel + +1;
    alert("Correct! You passed level: " + displayLevel);
    currentLevel += 1;
  } else {
    alert("Incorrect! Try again");
    wrongGuesses += 1;
  }
  checkState();
  return false;
}

// t0=user clicks on play
// t1=data comes back from server, display word
//
