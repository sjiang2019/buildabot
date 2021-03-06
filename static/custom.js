
$(document).ready(function(){
    $('select').formSelect();
});

function submit_message(message, character, personality, emotion) {

    $.post( "/send_message", {
        message: message,
        character: character,
        personality: personality,
        emotion: emotion
    }, handle_response);
    
    function handle_response(data) {
      // append the bot repsonse to the div
      $('.chat-container').append(`
            <div class="chat-message col-md-5 bot-message">
                ${data.message}
            </div>
      `)
      // remove the loading indicator
      $( "#loading" ).remove();
      let messages = document.getElementById('messages');
        messages.scrollTop = messages.scrollHeight;
    }
}

$('#target').on('submit', function(e){
    e.preventDefault();
    const input_message = $('#message').val()
    const character = $('#character').val()
    const personality = $('#personality').val()
    const emotion = $('#emotion').val()
    // return if the user does not enter any text
    if (!input_message) {
      return
    }
    
    $('.chat-container').append(`
        <div class="chat-message col-md-5 offset-md-7 human-message">
            ${input_message}
        </div>
    `)

    // loading 
    $('.chat-container').append(`
        <div class="chat-message text-center col-md-2 offset-md-10 bot-message" id="loading">
            <b>...</b>
        </div>
    `)
    
    // clear the text input 
    $('#message').val('')
    
    // send the message
    submit_message(input_message, character, personality, emotion)
});
