$(document).on('click', '#start-coach', function(){
    $.ajax({
        url:'/begin',
        method:'POST',
        data: 'begin',
        success: function(response){
            console.log('Response returned:', response)
            var message = response.choices[0].message.content;
            console.log('Message to be displayed:', message)
            $('#chat-response').html('<div><p class="bg-grey response-system">' + message + '</p></div>');
        },
        error: function(jqXHR, textStatus, errorThrown){
            console.log('Error')
        }
    })
})

$(document).on('click', '#user-go', function(){

    var data = $('#user-input').val();
    $('#chat-response').append('<div><p class="float-right response-user">'+ data + '</p><div>');


    $.ajax({
        url:'/process',
        method:'POST',
        data: { data },
        success: function(response){
            console.log('Response returned:', response)
            var message = response.choices[0].message.content;
            console.log('Message to be displayed:', message)
            $('#chat-response').append('<div><p class="response-system bg-grey">'+ message + '</p><div>');
        },
        error: function(jqXHR, textStatus, errorThrown){
            console.log('Error', errorThrown)
        }
    })
})