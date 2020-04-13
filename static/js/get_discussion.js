$(document).ready(function(){

  $('.user').click(function(){
    $('#chat-message').prop("disabled", false);
      $.ajax({
        url:'discussion/'+$(this).attr('data-user'),
        success:function(st){
          $('.chat-result').html(st)
        }
      })

  })



// toggling friends panel
$('.discussion-toggle').click(function(){
  $(this).fadeOut('slow');
  $('.users-container').addClass('show')
})
$('.close-panel').click(function(){
  $('.users-container').removeClass('show')
  $('.discussion-toggle').fadeIn('slow');
})
// end toggling friends panel
});
