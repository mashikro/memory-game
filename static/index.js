"use strict";

let currentWord = null;
let currentLevel = 0;
//set up
$(document).ready(() => {
  const playButton = $("#playButton");
  const instrButton = $("#instructionsButton");

  $("#instructions").hide();
  $("#displayed-word").hide();
  $("#word-form").hide();

  instrButton.on("click", () => {
    $("#instructions").show();
  });

  playButton.on("click", () => {
    $("#instructions").hide();
    $("#instructionsButton").hide();
    getWord();
  });
  console.log("Is this working????");
});

// func makes ajax request to get word
function getWord() {
  const levelData = {
    level: currentLevel
  };

  $.getJSON("/play.json", levelData, data => {
    //write a func to show word
    console.log("is data coming in", data);

    currentWord = data.word;

    $("#displayed-word").html(data.word);

    $("#displayed-word").show();

    // timer starts after the word comes in from server
    setTimeout(() => $("#displayed-word").hide(), 3000);
    setTimeout(() => $("#word-form").show(), 3100);
  });
}

//write a func to validate user input
function validateWord() {
  console.log("Are we getting here?");
  if (document.myForm.userInput.value == currentWord) {
    alert("Correct!");
    currentLevel += 1;
    // getWord();
  } else {
    // getWord();
    alert("Incorrect!");
  }
  getWord();
  return false;
}

// t0=user clicks on play
// t1=data comes back from server, display word
//
