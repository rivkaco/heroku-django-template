// $(".green-box").click(
// alert("hello")
// );

$(".clickable").click(function() {
    console.log("clicked");
    $(".empty-post").show();
    $(".approve-message").show();
    $(".clickable").hide();
    $(".no-messages").hide();
});


$( ".leave-message" ).click(function() {
    $(".empty-post").hide();
    $(".approve-message").hide();
    $(".clickable").show();
});

