/*
The problem can be boiled down to taking the sum of the first odd frequency and the max even frequency for each other character.

Lets take a look at the following two examples:
Example 1
abccccdd
a:1, b:1, c:4, d:2
longest palindrome is equal to 1+0+4+2
Notice that I ignore the second odd value.

Example 2
aaabbcddd
a:3, b:2, c:1, d:3
longest palindrome is equal to 3+2+0+2
Notice that I ignore the second odd value and then trim down 3 to 2.

Take note that all odd numbers have 0x1 bit set, so I wanted to create a mask to get the max even value while encompassing all possible values in this solution. A naive mask would be 0xFFFFFFFE, but we are given the max length of the string as being 1010, so we can do better!

To take advantage of the max length of the string being 1,010, we need a bitmask that covers the case where the string has a single one character and 1009 of another character. This case has both odd values.
1010 in binary is 0011 1111 0010
0x3fe in binary is 0011 1111 1110

Now everything is set for implementing the solution!

*/

public int LongestPalindrome(string s) {
    if(string.IsNullOrEmpty(s)) return 0;
    
    int[] frequencies = new int[128];
    foreach(var c in s) {
        frequencies[c]++;
    }
    bool oddFound = false;
    var longestPalindrome = 0;
    // smallest mask excluding 0x1 that is larger than the max length of str 1010 is 0x3fe
    var evenMask = 0x3fe;
    foreach(var frequency in frequencies) {
        if(!oddFound && (frequency & 1) == 1) {
            oddFound = true;
            longestPalindrome += frequency;
        }
        else longestPalindrome += frequency & evenMask;
    }
    return longestPalindrome;
}
