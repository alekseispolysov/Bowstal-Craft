//alert("this web is my own, hhahahhahahahahahhahaha");


// $("#ElementToScrollIntoView").scrollintoview();
// animate({scrollTop: $(".article-system").offset().top}, 1000)

//window.HTMLElement.prototype.scrollIntoView = function() {};


$(document).ready(function()
{
let smooth = true;
let height = 0;
let all_sticky_sidebars;
  
	let anim = smooth ? 'smooth' : 'auto';
  if($("#article-system")[0] !== undefined){
      

      $("html, body").animate({
        scrollTop: $("#article-system").offset().top - 90
      }, // second param is how many time, does it need to scroll down
        1000);
    }
// scrolling top function
$("#scroll-top").click(function(){
  $("html, body")[0].scrollIntoView({
      behavior: "smooth",
      block: "start",
    });
});

$(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });


if($(".django-ckeditor-widget")[0] !== undefined){
  $(".django-ckeditor-widget").attr("display", "block");
  CKEDITOR.on("instanceReady", function(event) {
  $(".django-ckeditor-widget").attr("display", "block");
});
}

// $('input:text').each(
//     function(i,el) {
//         if (!el.value || el.value == '') {
//             el.placeholder = 'placeholdertext';
//             /* or:
//             el.placeholder = $('label[for=' + el.id + ']').text();
//             */
//         }
//     });

// height = $(".navbar").offset().top;
// console.log(height);
// all_sticky_sidebars = $(".sticky-sidebar");
// all_sticky_sidebars.css("top", height+10);



// send jqery message chat
// if($("#chat-message-input")[0] !== undefined){
//   const chatSocket = new WebSocket(
//     'ws://'
//     + window.location.host
//     + '/ws/chat/'

//     );
//   $("#chat-message-input").focus();
//   $("#chat-message-input").keypress(function(event){
//     var keycode = (event.keycode ? event.keycode : event.which);
//     if(keycode == '13'){
//       $("#chat-message-submit").click();
//     }
//   });
// }




});




// sticky-sidebar class, property top: ()px;



// $("#article-system")[0].find($(this).attr('href')).offset().top - 100;
      //$("#article-system")[0].scrollIntoView({
        //behavior: anim,
        //block: "start",
      //});


// if already on that place on the page, don'scroll, else scroll to that place, when page loads

    // $(".btn").click(function(){
    // 	$.ajax({
    // 		url: '',
    // 		type: 'get',
    // 		data: {
    // 			button_text: $(this).text()
    // 		},
    // 		success: function(response){
    // 			$(".btn").text(response.seconds)
    // 		}
    // 	});
    // });

// function ScrollTipFunction() {
//   document.body.scrollTop = 0; // For Safari
//   document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
// } 

//.removeClass('sticky-sidebar').css(
//   "position", "sticky",
//   "top", height+30,
//   "margin-bottom", "20",
//   );





