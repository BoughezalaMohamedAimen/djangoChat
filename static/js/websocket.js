$(document).ready(function(){

// ------------------------CREATING THE  SOCKET  --------------------------------------------------------------
  	var targetuser;
  	var socket = new WebSocket('ws://127.0.0.1:8000/chat/ws/');
  	socket.onopen = websocket_welcome;
  	socket.onmessage = websocket_message_show;
//-----------------------------END SOCKET CREATION ---------------------------------------------------------------



// ------------------------SOCKET ON OPEN  --------------------------------------------------------------


function websocket_welcome(){
	alert("welcome to chat room")
}
//-----------------------------END SOCKET ON OPEN ---------------------------------------------------------------




// ------------------------SOCKET ON RECIVE  --------------------------------------------------------------

function websocket_message_show(e){
	message_data = JSON.parse(e.data);
  console.log(e.data)
	coding = "<h5>" + message_data.username + "</h5>" +
			 "<p class='coding'>" +  message_data.usermsg + "</p>";
	$('.chat-result').append(coding);

}

//-----------------------------END SOCKET ON RECIVE ---------------------------------------------------------------




// ------------------------ON CLICK BUTTON TO SEND MESSAGE   --------------------------------------------------------------

  	$('.send-message').click(function(e){
  		message_data = {
  			'username':targetuser,
  			'usermsg' : $('#chat-message').val(),

  		}
  		socket.send(JSON.stringify(message_data));
  		$("#chat-message").val('').change();
  	});

//-----------------------------END ON CLICK BUTTON TO SEND MESSAGE ---------------------------------------------------------------




// ------------------------SELECTING USER DESTINATION  --------------------------------------------------------------

  $('.user').click(function(){
      targetuser=$(this).attr('data-user')
      $('.user').removeClass('bg-secondary').removeClass('text-white').addClass('text-secondary')
      $(this).addClass('bg-secondary').removeClass('text-secondary').addClass('text-white')
  })
//-----------------------------END SELECTING USER DESTINATION  ---------------------------------------------------------------


});
