function craftUrl(url) {
  return 'https://kutabareindian.pythonanywhere.com/?url=' + url
}

function updateLink(url) {
  theLink = document.getElementById('link')
  theLink.href = url
  theLink.innerHTML = url
}

var elem = document.getElementById('inputField');
elem.addEventListener('keypress', function(e){
  if (e.keyCode == 13) {
    url = elem.value
    newUrl = craftUrl(url)
    updateLink(newUrl)
  }
});
