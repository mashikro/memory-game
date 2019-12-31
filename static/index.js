"use strict";

$(document).ready(() => {
    const playButton = $('#playButton');
    const instrButton = $('#instructionsButton');
    
    $('#instructions').hide();
    $('#displayed-word').hide();
    

    instrButton.on('click', () => {
      $('#instructions').show();
    });


    playButton.on('click', () => {
      $('#instructions').hide();
      $('#instructionsButton').hide();
      $('#displayed-word').show();

      $.getJSON("/play.json", (data) => {
        //write a func to show word
        console.log('is data coming in', data)

        $('#displayed-word').html(data.word);
      });

        // write a func to make word dissapear using setTimeout()

      setTimeout(() => $('#displayed-word').hide(), 3000);

    });

    console.log('Is this working????')
});
