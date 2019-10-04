function setCookie() {
    document.cookie =
        "uid=[!uid]; path=/; expires=Thu, 1-Jan-2030 00:00:00 GMT;";
}

function getCookie(name) {
    let cookie = document.cookie.split(";");
    for (const value in cookie) {
        spc = value.split("=");
        if (spc[0] == name) {
            return spc[1];
        }
    }
    return false;
}

let now = new Date();
let image = new Image(1, 1);

let uid = [!uid]

if (!getCookie("uid")) {
    setCookie();
}