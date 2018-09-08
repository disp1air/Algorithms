// Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

// For inputArray = [2, 4, 1, 0], the output should be arrayMaximalAdjacentDifference(inputArray) = 3

function max_adjacent(arr) {
    let diff = 0;

    for (let i = 1; i < arr.length; i++) {
        let x = Math.abs(arr[i] - arr[i - 1]);
        if (x > diff) {
            diff = x;
        }
    }

    return diff;
}

function arrayMaximalAdjacentDifference(arr) {
  return Math.max(...arr.slice(1).map((x,i)=>Math.abs(x-arr[i])))
}

console.log(max_adjacent([2, 4, 1, 0]) == 3);
console.log(max_adjacent([1, 1, 1, 1]) == 0);
console.log(max_adjacent([-1, 4, 10, 3, -2]) == 7);
console.log(max_adjacent([10, 11, 13]) == 2);
console.log(max_adjacent([-2, -2, -2, -2, -2]) == 0);
console.log(max_adjacent([-1, 1, -3, -4]) == 4);