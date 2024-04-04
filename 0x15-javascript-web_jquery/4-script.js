// Toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header
$(document).ready(function () {
  $('#toggle_header').click(function () {
    const headerElement = $('header');
    if (headerElement.hasClass('red')) {
      headerElement.removeClass('red').addClass('green');
    } else {
      headerElement.removeClass('green').addClass('red');
    }
  });
});
