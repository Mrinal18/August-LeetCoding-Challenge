/*

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.


*/ 

/*
Algorithm
First thing first, we need to create alphabet array abc that will store count of each separate letter.
We have 26 upper and 26 lower case letters, so size 52 is enough to address all letters.

Now we just need to sum up all letters' count, but we only interested in even counts.
That's why I use mask, it thows away the 1 at the end of the number (in binary format), making number even.

And for the result we just check if our count is equals s.size() then just return length.
If length < s.size() then we could put one more letter in the middle of our polindrome.
*/


class Solution {
public:
    int longestPalindrome(string s) {
        uint64_t bits{0};
    int ans{0};
    for (char c : s) {
        uint64_t mask = 1ull << (c - 'A'); // find the bit for the char
        ans += bits & mask ? 2 : 0; // if the bit already has 1, add 2 to ans
        bits ^= mask; // mark the bit: 1=>0, 0=>1
    }
    return ans + (bits ? 1 : 0); // adds 1 if there is any extra left
    }
};
