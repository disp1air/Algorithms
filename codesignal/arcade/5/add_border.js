function add_border(arr) {
    let first_and_last_string = '*'.repeat(arr[0].length + 2);
    let newArr = arr.map(item => '*' + item + '*');
    let res = [];
    return res.concat(first_and_last_string, newArr, first_and_last_string);
}