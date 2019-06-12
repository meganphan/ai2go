// (function ($) {
//     "use strict";
//     var check;

//     $('#home').hide();

//     //post message and info to AWS for processing
//     $('#submit').click(e => {
//         e.preventDefault();
//             $.ajax({
//                 url: '',
//                 method: 'POST',
//                 statusCode: 200,
//                 crossDomain: true,
//                 dataType: 'json',
//                 contentType: 'application/json',
//                 data: JSON.stringify({
//                     name: $('#name').val(),
//                     email: $('#email').val(),
//                     message: $('#message').val()
//                 }), //you have to stringify this!!!
//                 success: function (data) {
//                     $('#name').val('');
//                     $('#email').val('');
//                     $('#message').val('');
//                     $('#more').text('Thank you ' + data.name + ' for being interested in our project!')
//                 }
//             });
//     });
// })(jQuery);