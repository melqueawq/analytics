let now = new Date()
let image = new Image(1, 1);
image.src = location.protocol + '//127.0.0.1:5000/entry?' +
    '1' + '*' + now.getTime() +
    '*' + window.location + '*' + document.referrer;