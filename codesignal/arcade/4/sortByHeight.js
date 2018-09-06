let input = [-1, 150, 190, 170, -1, -1, 160, 180];
let output = [-1, 150, 160, 170, -1, -1, 180, 190];

function sortByHeight(a) {
    let positiveArray = a.filter((item) => item > 0);
    positiveArray.sort((a, b) => a - b);
    console.log(positiveArray);
    for(let i = 0; i < a.length; i++) {
        if(a[i] > 0) {
            a[i] = positiveArray.shift();
        }
    }
    return a;
}

// function sortByHeight(a) {
//   var s = a.filter(h => h > 0).sort((a, b) => a - b)
//   return a.map(p => {
//       if (p !== -1) {
//           return s.shift();
//       }
      
//       return -1;
//   })
// }

sortByHeight([4, 2, 9, 11, 2, 16]);

// tests
// [-1, -1, -1, -1, -1]
// [-1]
// [4, 2, 9, 11, 2, 16] - [2, 2, 4, 9, 11, 16]
// [2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1] - [1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2]
// [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3] - [1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77]