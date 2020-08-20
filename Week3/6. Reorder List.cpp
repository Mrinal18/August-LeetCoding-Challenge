/*
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

*/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

/*
Algorithm

1. Take the input LL and divide it into two list from the middle 
2. After getting the two list, reverse the second list 
3. Merge the LL back and forth for same indeces

eg 

1->2->3->4->5->6->7->8

1->2->3->4->NULL
5->6->7->8->NULL


1->2->3->4->NULL
8->7->6->5->NULL

1->8->2->7->3->6->4->5->NULL
*/

class Solution {
 public:
  void reorderList(ListNode* head) {
    if (!head || !head->next || !head->next->next) return;
    ListNode *slow = head, *fast = head, *head1 = head, *head2, *tmp1, *tmp2;
    while (fast && fast->next) {
      slow = slow->next;
      fast = fast->next->next;
    }
    head2 = slow->next;
    slow->next = nullptr;        // split list in half
    head2 = reverseList(head2);  // reverse 2nd half
    while (head1 && head2) {
      tmp1 = head1->next;
      head1->next = head2;
      tmp2 = head2->next;
      head2->next = tmp1;
      head1 = tmp1;
      head2 = tmp2;
    }
  }

 private:
  ListNode* reverseList(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* curr = head;
    ListNode* tmp;
    while (curr) {
      tmp = curr->next;
      curr->next = prev;
      prev = curr;
      curr = tmp;
    }
    return prev;
  }
};
