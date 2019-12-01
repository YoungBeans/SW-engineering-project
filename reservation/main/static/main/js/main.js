

$('.starRev span').click(function(){
    $(this).parent().children('span').removeClass('on');
    $(this).addClass('on').prevAll('span').addClass('on');
    var starValue = document.getElementsByClassName('input starR on');
    var inputValue = document.getElementById('starInput');

    inputValue.value = starValue.length;
    return false;
  });
