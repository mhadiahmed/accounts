$(document).ready(function(){
	$(".mark-Down").each(function(){
		var content = $(this).text()
		var markDown = marked(content)
		$(this).html(markDown)
	});


	var ItemsTitle = $("#id_title");
	function setTitile(value){
		$("#title-pr").text(value)
	}
	setTitile(ItemsTitle.val())
	ItemsTitle.keyup(function(){
		var newContent = $(this).val()
		setTitile(newContent)
	});
// date
	var itemsDate = $("#id_date");
	function setDate(value){
		$("#date-pr").text(value)
	}
	setDate(itemsDate.val())
	itemsDate.keyup(function(){
		var newContent = $(this).val()
		setDate(newContent)
	});
// image
	var itemImage = $("#id_image");
	function setImage(value){
		$("#img-pr").text(value)
	}
	setImage(itemImage.val())
	itemImage.keyup(function(){
		var newContent = $(this).val()
		setImage(newContent)
	});

// price
	var itemsPrice = $("#id_price");
	function setPrice(value){
		$("#price-id").text(value)
	}
	setPrice(itemsPrice.val())
	itemsPrice.keyup(function(){
		var newContent = $(this).val()
		setPrice(newContent)
	});
// dis
	var itemsDis = $("#id_dis");
	function setDis(value){
		$("#dis-pr").text(value)
	}
	setDis(itemsDis.val())
	itemsDis.keyup(function(){
		var newContent = $(this).val()
		setDis(newContent)
	});

	$(".coment-r-btn").click(function(event){
		event.preventDefault();
		$(this).parent().next(".comment-Reply").toggle();

	});







});

	//jQuery for page scrolling feature - requires jQuery Easing plugin

// $(window).load(function() {
//     $(".loader").fadeOut("slow");
// })
$(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
});

//jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $(document).on('click', 'a.page-scroll', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});
