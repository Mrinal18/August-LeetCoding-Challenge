/*
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

*/
/*
intuition:

to calculat the decimal value of a number , lets say '1337' we do  the following:
1. '1' = 1
2. '13' = (1 * 10) + 3
3. '133' =  (13 * 10) + 3
4. '1337' = (133 * 10) + 7

So, instead of us using the 10th base we can make using of 26th base by replacing the 10s by 26 and processing using the same pattern.

Eg
"LEET"

1. 'L' = 12
2. 'LE' = (12 * 26 ) + 5  = 317
3. 'LEE' = (317 * 26) + 5 = 8247
4. 'LEET' = (8247 * 26) + 20 = 214442
. You can do this by converting a character to its ASCII value and subtracting ASCII value of character 'A' from that value. By doing so, you will get results from 0 (for A) to 25 (for Z). Since we are indexing from 1, we can just add 1 up to the result.


Complexity:
TC: O(N)
SC: O(1)


*/
class Solution {
public:
    int titleToNumber(string s) {
        int cnum = 0;
        
        for(int i = 0; i < s.length(); i++){
            cnum = cnum * 26;
            
            cnum += s[i] - 'A' + 1;
        }
        
        return cnum;
    }
};

