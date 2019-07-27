function create_post() {
    console.log("create post is working!") // sanity check
    console.log($('#exampleFormControlInput1').val())
    console.log($('#exampleFormControlTextarea1').val())

    console.log("create post is working!") // sanity check
$.ajax({
    url : "create_post/", // the endpoint
    type : "POST", // http method
    data : { the_title : $('#exampleFormControlInput1').val() , the_content : $('#exampleFormControlTextarea1').val()}, // data sent with the post request
    // data:{
    //   title:$('exampleFormControlInput1').val(),
    //   console.log(title),
    //   body:$('exampleFormControlTextarea1').val()
    //   console.log(body)
    //
    // }
    // handle a successful response
    success : function(json) {
        // $('#post-form').val(''); // remove the value from the input
        $('#exampleFormControlInput1').val('');
        $('#exampleFormControlTextarea1').val('');


        console.log(json); // log the returned json to the console
        console.log("success"); // another sanity check
    },

    // handle a non-successful response
    error : function(xhr,errmsg,err) {
        $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
            " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
});
};


$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});
// $('#post-form').on('submit',function(e){
//   e.preventDefault();
//       $.ajax({
//         type:'POST',
//         url:'create_post/'
        // data:{
        //   title:$('exampleFormControlInput1').val(),
        //   console.log(title)
        //   body:$('exampleFormControlTextarea1').val()
        //   console.log(body)
        //
        // }
//         success:function(){
//           alert("created new post")
//         }
//       })
// }



// $("#modal-book").on("submit", "post-form", function () {
//   var form = $(this);
//   $.ajax({
//     url: form.attr("action"),
//     data: form.serialize(),
//     type: form.attr("method"),
//     dataType: 'json',
//     success: function (data) {
//       if (data.form_is_valid) {
//         alert("Book created!");  // <-- This is just a placeholder for now for testing
//       }
//       else {
//         $("#modal-book .modal-content").html(data.html_form);
//         alert("no data")
//       }
//     }
//   });
//   return false;
// });
