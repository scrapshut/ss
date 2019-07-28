$('button').on('click',function(event){
  event.preventDefault();
  var element=$(this);
$.ajax({

  url: $(this).attr("data-href"),
  type:'GET',
  success:function(response){
    // $('#lik').html(response);
    // console.log(response);
    // alert(response.message);
    // alert('Company likes count is now ' + response.likes_count);
    // document.getElementById('like-count').innerHTML = response.like_count;
    // $('#like_count').html(response.likes_count);
    // $('#lik').html(response.likes_count);
    element.html(response.likes_count)


    // element.html(' ' + response)
  }
});
});
