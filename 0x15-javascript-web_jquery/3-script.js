// Adds the class red to the <header> element when
// the user clicks on the tag DIV#red_header
// using JQuery

$('DIV#red_header').on('click', function () {
  $('header').addClass('red');
});