/** product: calculate the product of an array of numbers. */

function product(nums, i = 0) {
  if (i === nums.length) return 1;
  return nums[i] * product(nums, i + 1);
}

console.log(product([2, 3, 4])); // 24

/** longest: return the length of the longest word in an array of words. */

function longest(words, i = 0) {
  if (i === words.length) return 0;
  return Math.max(words[i].length, longest(words, i + 1));
}

console.log(longest(["hello", "hi", "hola"])); // 5

/** everyOther: return a string with every other letter. */

function everyOther(str, i = 0) {
  if (i >= str.length) return "";
  return str[i] + everyOther(str, i + 2);
}

console.log(everyOther("hello")); // "hlo"

/** isPalindrome: checks whether a string is a palindrome or not. */

function isPalindrome(str, left = 0, right = str.length -1) {
  if (left >= right) return true;
  if (str[left] !== str[right]) return false;
  return isPalindrome(str, left + 1, right - 1);
}

console.log(isPalindrome("tacocat")); // true
console.log(isPalindrome("tacodog")); // false

/** findIndex: return the index of val in arr (or -1 if val is not present). */

function findIndex(arr, str, i = 0) {
  if (i === arr.length) return -1;
  if (arr[i] === str) return i;
  return findIndex(arr, str, i + 1);
}

let animals = ["duck", "cat", "pony"];
console.log(findIndex(animals, "cat")); // 1
console.log(findIndex(animals, "porcupine")); // -1

/** revString: return a copy of a string, but in reverse. */

function revString(str, i = str.length - 1) {
  if (i < 0) return "";
  return str[i] + revString(str, i - 1);
}

console.log(revString("porcupine")); // 'enipucrop'

/** gatherStrings: given an object, return an array of all of the string values. */

function gatherStrings(obj) {
  let strings = [];
  for (let key in obj) {
    if (typeof obj[key] === 'string') {
      strings.push(obj[key]);
    } else if (typeof obj[key] === 'object') {
      strings = strings.concat(gatherStrings(obj[key]));
    }
  }
  return strings;
}

let nestedObj = {
  firstName: "Lester",
  favoriteNumber: 22,
  moreData: {
    lastName: "Testowitz"
  },
  funFacts: {
    moreStuff: {
      anotherNumber: 100,
      deeplyNestedString: {
        almostThere: {
          success: "you made it!"
        }
      }
    },
    favoriteString: "nice!"
  }
};

console.log(gatherStrings(nestedObj)); // ["Lester", "Testowitz", "you made it!", "nice!"]

/** binarySearch: given a sorted array of numbers, and a value,
 * return the index of that value (or -1 if val is not present). */

function binarySearch(arr, val) {
  function helper(arr, val, left, right) {
    if (left > right) return -1; // Base case: value not found

    const mid = Math.floor((left + right) / 2);

    if (arr[mid] === val) return mid; // Value found at mid
    else if (arr[mid] < val) return helper(arr, val, mid + 1, right); // Search right half
    else return helper(arr, val, left, mid - 1); // Search left half
  }

  return helper(arr, val, 0, arr.length - 1); // Initial call
}

// Test cases
console.log(binarySearch([1, 2, 3, 4], 1)); // 0
console.log(binarySearch([1, 2, 3, 4], 3)); // 2
console.log(binarySearch([1, 2, 3, 4], 5)); // -1

module.exports = {
  product,
  longest,
  everyOther,
  isPalindrome,
  findIndex,
  revString,
  gatherStrings,
  binarySearch
};
