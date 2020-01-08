"use strict";

let currentWord = null;

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

    $.getJSON("/play.json", data => {
      //write a func to show word
      console.log("is data coming in", data);

      currentWord = data.word;

      $("#displayed-word").html(data.word);

      $("#displayed-word").show();

      // timer starts after the word comes in from server
      setTimeout(() => $("#displayed-word").hide(), 3000);
      setTimeout(() => $("#word-form").show(), 3500);
    });
  });
  console.log("Is this working????");
});

//write a func to validate user input
function validateWord() {
  console.log("Are we getting here?");
  if (document.myForm.userInput.value == currentWord) {
    alert("Correct!");
    // document.myForm.Name.focus() ;
  } else alert("Incorrect!");

  return false;
}

// t0=user clicks on play
// t1=data comes back from server, display word
//
