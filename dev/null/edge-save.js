// Save button for Edge, haven't done much testing yet
javascript:
var anchor = document.createElement('a');
anchor.href = window.location.href;
anchor.target = '_blank';
anchor.download = window.location.href.match('.*\/(.*)\/?')[1];
anchor.click();
