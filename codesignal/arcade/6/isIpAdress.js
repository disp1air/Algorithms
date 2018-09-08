// IPv4 addresses are represented in dot-decimal notation, which consists of four decimal numbers, 
// each ranging from 0 to 255 inclusive, separated by dots, e.g., 172.16.254.1.

// Given a string, find out if it satisfies the IPv4 address naming rules.

// For inputString = "172.16.254.1", the output should be isIPv4Address(inputString) = true;
// For inputString = "172.316.254.1", the output should be isIPv4Address(inputString) = false.

function isIPv4Address(inputString) {
    let arr = inputString.split('.');
    if (arr.length !== 4) {
      return false;
    }
    return arr.every(i => i !== '' && +i < 256 && parseInt(i) >= 0);
}

// var  r=s.split(".")
// return r.length===4&&r.every(x=>x!=""&&!isNaN(x)&&x>=0&&x<256)

console.log(isIPv4Address('123.65.7.123') == true);
console.log(isIPv4Address('0.0.0.0') == true);
console.log(isIPv4Address('123.65.7.323') == false);
console.log(isIPv4Address('123.65.-7.123') == false);
