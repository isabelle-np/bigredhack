// Form made with help by Bhakti Al Akbar via CodePen available to everyone

var $firstButton = $(".first"),
  $secondButton = $(".second"),
  $thirdButton = $(".third"),
  $input = $("input"),
  $name = $(".name"),
  $more = $(".more"),
  $yourname = $(".yourname"),
  $reset = $(".reset"),
  $ctr = $(".container"),
  $annual = $(".annual"),
  $hourly = $(".hourly"),
  $shared = $(".shared"),
  $one = $(".one"),
  $two = $(".two"),
  $three = $(".three"),
  $economic = $(".economic"),
  $modest = $(".modest"),
  $average = $(".average"),
  $trendy = $(".trendy"),
  $yes = $(".yes"),
  $no = $(".no"),
  $none = $(".none"),
  $low = $(".low"),
  $ave = $(".ave"),
  $high = $(".high");

  

$firstButton.on("click", function(e){
  $(this).text("Saving...").delay(900).queue(function(){
    $ctr.addClass("center slider-two-active").removeClass("full slider-one-active");
  });
  e.preventDefault();
});

$secondButton.on("click", function(e){
  $(this).text("Saving...").delay(900).queue(function(){
    $ctr.addClass("full slider-three-active").removeClass("center slider-two-active slider-one-active");
  });
  e.preventDefault();
});

$thirdButton.on("click", function(e){
    $(this).text("Saving...").delay(900).queue(function(){
      $ctr.addClass("full slider-three-active").removeClass("center slider-two-active slider-one-active");
      $name = $name.val();
      if($name == "") {
        $yourname.html("Anonymous!");
      }
      else { $yourname.html($name+"!"); }
    });
    e.preventDefault();
  });

  $annual.on("click", function(e) {
      $(this).addClass("activeradio");
      $hourly.removeClass("activeradio");
      $(this).children("span").css('color', '#fd8a10');
      $hourly.children("span").css('color', '#fff');
  });

  $hourly.on("click", function(e) {
    $(this).addClass("activeradio");
    $annual.removeClass("activeradio");
    $(this).children("span").css('color', '#fd8a10');
    $annual.children("span").css('color', '#fff');
});

$shared.on("click", function(e) {
    $(this).addClass("activeradio");
    $one.removeClass("activeradio");
    $one.children("span").css('color', '#fff');
    $two.removeClass("activeradio");
    $two.children("span").css('color', '#fff');
    $three.removeClass("activeradio");
    $three.children("span").css('color', '#fff');
    $(this).children("span").css('color', '#fd8a10');
    
});

$one.on("click", function(e) {
    $(this).addClass("activeradio");
    $(this).children("span").css('color', '#fd8a10');
    $shared.removeClass("activeradio");
    $shared.children("span").css('color', '#fff');
    $two.removeClass("activeradio");
    $two.children("span").css('color', '#fff');
    $three.removeClass("activeradio");
    $three.children("span").css('color', '#fff');
});

$two.on("click", function(e) {
    $(this).addClass("activeradio");
    $(this).children("span").css('color', '#fd8a10');
    $shared.removeClass("activeradio");
    $shared.children("span").css('color', '#fff');
    $one.removeClass("activeradio");
    $one.children("span").css('color', '#fff');
    $three.removeClass("activeradio");
    $three.children("span").css('color', '#fff');
});

$three.on("click", function(e) {
    $shared.removeClass("activeradio");
    $one.removeClass("activeradio");
    $two.removeClass("activeradio");
    $(this).addClass("activeradio");
    $(this).children("span").css('color', '#fd8a10');
    $shared.children("span").css('color', '#fff');
    $one.children("span").css('color', '#fff');
    $two.children("span").css('color', '#fff');
});

$economic.on("click", function(e) {
    $(this).addClass("activeradio");
    $(this).children("span").css('color', '#fd8a10');
    $modest.removeClass("activeradio");
    $modest.children("span").css('color', '#fff');
    $average.removeClass("activeradio");
    $average.children("span").css('color', '#fff');
    $trendy.removeClass("activeradio");
    $trendy.children("span").css('color', '#fff');
});

$modest.on("click", function(e) {
    $(this).addClass("activeradio");
    $(this).children("span").css('color', '#fd8a10');
    $economic.removeClass("activeradio");
    $economic.children("span").css('color', '#fff');
    $average.removeClass("activeradio");
    $average.children("span").css('color', '#fff');
    $trendy.removeClass("activeradio");
    $trendy.children("span").css('color', '#fff');
});

$average.on("click", function(e) {
    $(this).addClass("activeradio");
    $(this).children("span").css('color', '#fd8a10');
    $economic.removeClass("activeradio");
    $economic.children("span").css('color', '#fff');
    $modest.removeClass("activeradio");
    $modest.children("span").css('color', '#fff');
    $trendy.removeClass("activeradio");
    $trendy.children("span").css('color', '#fff');
});

$trendy.on("click", function(e) {
    $(this).addClass("activeradio");
    $(this).children("span").css('color', '#fd8a10');
    $economic.removeClass("activeradio");
    $economic.children("span").css('color', '#fff');
    $modest.removeClass("activeradio");
    $modest.children("span").css('color', '#fff');
    $average.removeClass("activeradio");
    $average.children("span").css('color', '#fff');
});

$yes.on("click", function(e) {
    $(this).addClass("activeradio");
    $no.removeClass("activeradio");
    $(this).children("span").css('color', '#fd8a10');
    $no.children("span").css('color', '#fff');
});

$no.on("click", function(e) {
    $(this).addClass("activeradio");
    $yes.removeClass("activeradio");
    $(this).children("span").css('color', '#fd8a10');
    $yes.children("span").css('color', '#fff');
});

$none.on("click", function(e) {
    $(this).addClass("activeradio");
    $(this).children("span").css('color', '#fd8a10');
    $low.removeClass("activeradio");
    $low.children("span").css('color', '#fff');
    $ave.removeClass("activeradio");
    $ave.children("span").css('color', '#fff');
    $high.removeClass("activeradio");
    $high.children("span").css('color', '#fff');
});

$low.on("click", function(e) {
    $(this).addClass("activeradio");
    $(this).children("span").css('color', '#fd8a10');
    $none.removeClass("activeradio");
    $none.children("span").css('color', '#fff');
    $ave.removeClass("activeradio");
    $ave.children("span").css('color', '#fff');
    $high.removeClass("activeradio");
    $high.children("span").css('color', '#fff');
});

$ave.on("click", function(e) {
    $(this).addClass("activeradio");
    $(this).children("span").css('color', '#fd8a10');
    $none.removeClass("activeradio");
    $none.children("span").css('color', '#fff');
    $low.removeClass("activeradio");
    $low.children("span").css('color', '#fff');
    $high.removeClass("activeradio");
    $high.children("span").css('color', '#fff');
});

$high.on("click", function(e) {
    $(this).addClass("activeradio");
    $(this).children("span").css('color', '#fd8a10');
    $none.removeClass("activeradio");
    $none.children("span").css('color', '#fff');
    $low.removeClass("activeradio");
    $low.children("span").css('color', '#fff');
    $ave.removeClass("activeradio");
    $ave.children("span").css('color', '#fff');
});