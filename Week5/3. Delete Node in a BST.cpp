/*
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
*/ 


/*
**Intuition**

There are three possible situations here :

Node is a leaf, and one could delete it straightforward : node = null.


Node is not a leaf and has a right child. Then the node could be replaced by its successor which is somewhere lower in the right subtree. Then one could proceed down recursively to delete the successor.


Node is not a leaf, has no right child and has a left child. That means that its successor is somewhere upper in the tree but we don't want to go back. Let's use the predecessor here which is somewhere lower in the left subtree. The node could be replaced by its predecessor and then one could proceed down recursively to delete the predecessor.
bla

Algorithm

If key > root.val then delete the node to delete is in the right subtree root.right = deleteNode(root.right, key).

If key < root.val then delete the node to delete is in the left subtree root.left = deleteNode(root.left, key).

If key == root.val then the node to delete is right here. Let's do it :

If the node is a leaf, the delete process is straightforward : root = null.

If the node is not a leaf and has the right child, then replace the node value by a successor value root.val = successor.val, and then recursively delete the successor in the right subtree root.right = deleteNode(root.right, root.val).

If the node is not a leaf and has only the left child, then replace the node value by a predecessor value root.val = predecessor.val, and then recursively delete the predecessor in the left subtree root.left = deleteNode(root.left, root.val).

Return root.
*/


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
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if( !root )
        return nullptr;
    
    if( root->val == key ){
        if( !root->right )
            return root->left;
        else{
            TreeNode* n = root->right;
            while( n->left )
                n = n->left;
            swap( n->val , root->val );
            
            root->right = deleteNode( root->right , key );
            return root;
        }
    }
    
    if( root->val > key )
        root->left = deleteNode( root->left , key );
    if( root->val < key )
        root->right = deleteNode( root->right , key );
    return root;
    }
};
