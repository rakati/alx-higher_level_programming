$('DIV#toggle_header').click(function () {
  if ($('header').is('.red')) {
    $('header').attr('class', 'green');
  } else {
    $('header').attr('class', 'red');
  }
});
