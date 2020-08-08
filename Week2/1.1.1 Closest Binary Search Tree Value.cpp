/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
 
 /*
 Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
*/

class Solution {
public:
    
    //We will be taking the absolute differnece of the value of root and the current value of node. 
    //we have to find the minimum difference value. This step is done using binary search.
    
    //go left if target is smaller than current root value, and go right otherwise. Choose the closest to target value at each step.
    int closestValue(TreeNode* root, double target) {
        int val , closest = root->val;
        
        while(root != NULL){
            val = root->val;
            closest = abs(val - target) < abs(closest - target ) ? val : closest;
            
            root = target < root->val ? root->left : root->right;
        }
        
        
        return closest; 
    }
};
