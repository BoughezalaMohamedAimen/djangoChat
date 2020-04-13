
$(document).ready(function(){
const socketurl='ws://127.0.0.1:8000/chat/ws/';
const cleardiscuss='/chat/clear/message/'

// ------------------------CREATING THE  SOCKET  --------------------------------------------------------------
  	var targetuser;
  	var socket = new WebSocket(socketurl);
  	socket.onopen = websocket_welcome;
  	socket.onmessage = websocket_message_show;
//-----------------------------END SOCKET CREATION ---------------------------------------------------------------



// ------------------------SOCKET ON OPEN  --------------------------------------------------------------


function websocket_welcome(){
	// alert("welcome to chat room")
}
//-----------------------------END SOCKET ON OPEN ---------------------------------------------------------------




// ------------------------SOCKET ON RECIVE  --------------------------------------------------------------

function websocket_message_show(e){
	message_data = JSON.parse(e.data);
  console.log(e.data)
	coding = "<b class='discus-user'>" + message_data.username + "</b>" +
			 "<p><span class='user-message'>" +  message_data.usermsg + "</span></p>";

  if(!message_data.userid)
  $('.chat-result').append(coding);

  if(parseInt(message_data.userid)==parseInt(targetuser)){
    $('.chat-result').append(coding);
    clearuser($('.user[data-user='+message_data.userid+']'))
  }
  else
    add_message_notification(message_data.userid);

    $(".chat-result").animate({ scrollTop: $('.chat-result').prop("scrollHeight")}, 500);


}

//-----------------------------END SOCKET ON RECIVE ---------------------------------------------------------------




// ------------------------ON CLICK BUTTON TO SEND MESSAGE   --------------------------------------------------------------



    $('.message-form').submit(function(e){
      e.preventDefault()
      if ($('#chat-message').val() != ""){

         message_data = {
           'username':targetuser,
           'usermsg' : $('#chat-message').val(),
         }
         socket.send(JSON.stringify(message_data));
         $("#chat-message").val('').change();
         $('#chat-message').focus()
      }
    });

//-----------------------------END ON CLICK BUTTON TO SEND MESSAGE ---------------------------------------------------------------




// ------------------------SELECTING USER DESTINATION  --------------------------------------------------------------

  $('.user').click(function(){
      targetuser=$(this).attr('data-user')
      $('.user').removeClass('selected-user')
      $(this).addClass('selected-user')
      if($(this).find('.message-count').length > 0)
      clearuser($(this))
      $('#chat-message').focus()


  })
//-----------------------------END SELECTING USER DESTINATION  ---------------------------------------------------------------



function clearuser(usr){
  $.get({
    url:cleardiscuss+''+targetuser,
    success:function(st){
      usr.find('.message-count').remove()
      $(".chat-result").animate({ scrollTop: $('.chat-result').prop("scrollHeight")}, 500);
    }
  })
}
});


function add_message_notification(userid){
  var usr=$('.user[data-user='+userid+']')
  var usrmessages=usr.find('.message-count')

  if (usrmessages.length>0)
    usrmessages.html(parseInt(usrmessages.html())+1);
  else
    usr.append('<span class="message-count px-1">1</span>');
}
