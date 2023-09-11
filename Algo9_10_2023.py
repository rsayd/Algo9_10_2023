"""
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Is there a quick way to determine if they aren't an anagram before spending more time?

Given two strings
return whether or not they are anagrams
"""

const strA1 = "yes";
const strB1 = "eys";
const expected1 = true;

const strA2 = "yes";
const strB2 = "eYs";
const expected2 = true;

const strA3 = "no";
const strB3 = "noo";
const expected3 = false;

const strA4 = "silent";
const strB4 = "listen";
const expected4 = true;

"""
 * Determines whether s1 and s2 are anagrams of each other.
 * Anagrams have all the same letters but in different orders.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether s1 and s2 are anagrams.
"""
function isAnagram(s1, s2) {}

"""
Given a string that may have extra spaces at the start and the end,
return a new string that has the extra spaces at the start and the end trimmed (removed)
do not remove any other spaces.
"""

const str1 = "   hello world     ";
const expected1 = "hello world";

"""
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
"""
function trim(str) {}







function isAnagram(s1, s2) {
    return (s1.toLowerCase().split('').sort().join('') == s2.toLowerCase().split('').sort().join('')) ? true : false
}
[8:51 AM]
function count(string) {
    let characterCount = {};
    string.split('').forEach(function(char){
        
    for (let i = 0; i < string.length; i++) {
        if (characterCount.hasOwnProperty(string[i])) 
        characterCount[string[i]]++;
        else characterCount[string[i]] = 1;
        }
    })
    
    return characterCount;
    }

function isAnagram2(callback, str1, str2) {

    str1 = callback(str1.toLowerCase())
    str2 = callback(str2.toLowerCase())
    const keys1 = Object.keys(str1)
    const keys2 = Object.keys(str2)

    if (keys1.length !== keys2.length) {
        return false
    }

    for (const key of keys1) {
        if (str1[key] !== str2[key]) {
            return false
        }
    }

    return true
}



