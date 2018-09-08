// You are given an array of integers. On each move you are allowed to increase exactly 
// one of its element by one. Find the minimal number of moves required to obtain a strictly 
// increasing sequence from the input.

// For inputArray = [1, 1, 1], the output should be arrayChange(inputArray) = 3.

function arrayChange(inputArray) {
//  let currentValue = 0;
  let result = 0;
  
  for (let i = 1; i < inputArray.length; i++) {
      if (inputArray[i] <= inputArray[i - 1]) {
          currentValue = inputArray[i - 1] - inputArray[i] + 1;
          inputArray[i] += currentValue;
          result += currentValue;
      }
  }

  return result;
}

console.log(arrayChange([1, 1, 1]));
console.log(arrayChange([-1000, 0, -2, 0]));
// [2, 1, 10, 1] - 12
// [2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15] - 13