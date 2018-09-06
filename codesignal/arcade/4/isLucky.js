function isLucky(n) {
    let str = n + '';
    let sum1 = 0;
    let sum2 = 0;
    let arr = str.split('');
    [1, 4, 0, 5]
    for(let i = 0; i < arr.length; i++) {
        if(i < arr.length / 2) {
            sum1 += parseInt(arr[i]);
        } else {
            sum2 += parseInt(arr[i]);
        }
    }
    return sum1 == sum2;
}

console.log(isLucky(1230));

function isLucky(n) {
  var a=(n+"").split(""),half=a.length/2,l=0,r=0
  while(a.length>half) r+= +a.pop()
  while(a.length) l+= +a.pop()
  return l===r
}
