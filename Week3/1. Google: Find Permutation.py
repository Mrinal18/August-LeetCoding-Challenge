"""
By now, you are given a secret signature consisting of character 'D' and 'I'. 'D' represents a decreasing relationship between two numbers, 'I' represents an increasing relationship between two numbers. And our secret signature was constructed by a special integer array, which contains uniquely all the different number from 1 to n (n is the length of the secret signature plus 1). For example, the secret signature "DI" can be constructed by array [2,1,3] or [3,1,2], but won't be constructed by array [3,2,4] or [2,1,3,4], which are both illegal constructing special string that can't represent the "DI" secret signature.

On the other hand, now your job is to find the lexicographically smallest permutation of [1, 2, ... n] could refer to the given secret signature in the input.

Example 1:
Input: "I"
Output: [1,2]
Explanation: [1,2] is the only legal initial spectial string can construct secret signature "I", where the number 1 and 2 construct an increasing relationship.
"""


"""
Approach #1 Using Stack [Accepted]
Let's revisit the important points of the given problem statement. For a given nn, we need to use all the integers in the range (1,n)(1,n) to generate a lexicographically smallest permutation of these nn numbers which satsfies the pattern given in the string ss.

Firstly, we note that the lexicographically smallest permutation that can be generated(irrelevant of the given pattern ss) using the nn integers from (1,n)(1,n) is [1, 2, 3,.., n][1,2,3,..,n](say minmin). Thus, while generating the required permutation, we can surely say that the permutation generated should be as close as possible to minmin.

Now, we can also note that the number generated will be the smallest possible only if the digits lying towards the most significant positions are as small as possible while satisfying the given pattern. Now, to understand how these observations help in providing the solution of the given problem, we'll look at a simple example.

Say, the given pattern ss is "DDIIIID". This corresponds to n=8n=8. Thus, the minmin permutation possible will be [1, 2, 3, 4, 5, 6, 7, 8]. Now, to satisfy the first two "DD" pattern, we can observe that the best course of action to generate the smallest arrangement will be to rearrange only 1, 2, 3, because these are the smallest numbers that can be placed at the three most significant positions to generate the smallest arrangement satisfying the given pattern till now, leading to the formation of [3, 2, 1, 4, 5, 6, 7, 8] till now. We can note that placing any number larger than 3 at any of these positions will lead to the generation of a lexicographically larger arrangement as discussed above.

We can also note that irrespective of how we rearrange the first three 1, 2, 3, the relationship of the last number among them with the next number always satisfies the criteria required for satisfying the first I in ss. Further, note that, the pattern generated till now already satisfies the subpattern "IIII" in ss. This will always be satisfied since the minmin number considered originally always satisfies the increasing criteria.

Now, when we find the last "D" in the pattern ss, we again need to make rearrangements in the last two positions only and we need to use only the numbers 7, 8 in such rearrangements at those positions. This is because, again, we would like to keep the larger number towards the least significant possible as much as possible to generate the lexicographically smallest arrangement. Thus, to satisfy the last "D" the best arrangement of the last two numbers is 8, 7 leading to the generation of [3, 2, 1, 4, 5, 6, 8, 7] as the required output.

Based on the above example, we can summarize that, to generate the required arrangement, we can start off with the minmin number that can be formed for the given nn. Then, to satisfy the given pattern ss, we need to reverse only those subsections of the minmin array which have a D in the pattern at their corresponding positions.

To perform these operations, we need not necessarily create the minmin array first, because it simply consists of numbers from 11 to nn in ascending order.

To perform the operations discussed above, we can make use of a stackstack. We can start considering the numbers ii from 11 to nn. For every current number, whenver we find a D in the pattern ss, we just push that number onto the stackstack. This is done so that, later on, when we find the next I, we can pop off these numbers from the stack leading to the formation of a reversed (descending) subpattern of those numbers corrresponding to the D's in ss(as discussed above).

When we encounter an I in the pattern, as discussed above, we push the current number as well onto the stackstack and then pop-off all the numbers on the stackstack and append these numbers to the resultant pattern formed till now.

Now, we could reach the end of the pattern ss with a trail of D's at the end. In this case, we won't find an ending I to pop-off the numbers on the stackstack. Thus, at the end, we push the value nn on the stack and then pop all the values on the stackstack and append them to the resultant pattern formed till now. Now, if the second last character in ss was an I, nn will be appended at the end of the resultant arrangement correctly. If the second last character was a D, the reversed pattern appended at the end of the resultant arrangement will be reversed including the last number nn. In both the cases, the resultant arrangement turns out to be correct.

"""


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        ## RC ##
		## APPROACH : STACK ##
        ## LOGIC ##
        ## 1. When we get D, we push and when we get I, we calculate previous maximum value and calculate the next number i.e prev + 1 and add to current I position and as only D's are in the stack and they have lower precedence than I, we pop all incrementing the prev value updated
        ## 2. To simplify the things, I have appended I at the end. ( if there are any D's left in the stack, this will take care and also we are missing out the last number, i.e len(s), so include that aswell we need I at the end)
		
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##

        ## EXAMPLE : "DDIIDDID"	##
		## STACK TRACE ##
        # D [0, 0, 0, 0, 0, 0, 0, 0, 0] [('D', 0)]
        # D [0, 0, 0, 0, 0, 0, 0, 0, 0] [('D', 0), ('D', 1)]
        # I [3, 2, 1, 0, 0, 0, 0, 0, 0] []
        # I [3, 2, 1, 4, 0, 0, 0, 0, 0] []
        # D [3, 2, 1, 4, 0, 0, 0, 0, 0] [('D', 4)]
        # D [3, 2, 1, 4, 0, 0, 0, 0, 0] [('D', 4), ('D', 5)]
        # I [3, 2, 1, 4, 7, 6, 5, 0, 0] []
        # D [3, 2, 1, 4, 7, 6, 5, 0, 0] [('D', 7)]
        # I [3, 2, 1, 4, 7, 6, 5, 9, 8] []

        
        stack = []
        # indicates the value of the last element that is put in the ans array
        prev = 0
        ans = [0] *(len(s)+1)
        for i, ch in enumerate(s + "I"):
            if( ch == "I" ):
                prev = prev + 1
                ans[i] = prev
                while( stack ):
                    prev += 1
                    ans[stack.pop()] = prev
            else:
                stack.append(i)
            # print(ch, ans, stack)
        return ans
    
        ## OTHER SOLUTION ##
        # Reversing the subarray: we first fill all the answer array with 1 to n sequentially, then from the first occurance of D to first occurance of I, we reverse all values including the Dth and Ith position.
