"use strict";

$(document).ready(() => {
    const playButton = $('#playButton');
    const instrButton = $('#instructionsButton');
    
    $('#instructions').hide();
    $('#displayed-word').hide();

// when you press play hide instructions
// show the rest 

    playButton.on('click', () => {
      $('#instructions').hide();
      $('#instructionsButton').hide();
      $('#displayed-word').show();

      $.getJSON("/play.json", (data) => {
        //write a func to show word
        console.log('is data coming in', data)

        $('#displayed-word').html(data.word);
      });

    });

    instrButton.on('click', () => {
      $('#instructions').show();
    });

    console.log('Is this working????')
});
