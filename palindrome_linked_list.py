# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cursor = head
        prev = None
        fast = head
        slow = head

        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next

        if(fast is None):
            while(slow is not None):
                temp = slow.next
                slow.next = prev
                prev = slow
                slow = temp
            slow = prev
        else:
            slow = slow.next
            while(slow is not None):
                temp = slow.next
                slow.next = prev
                prev = slow
                slow = temp
            slow = prev

        while(slow is not None):
            if(slow.val != cursor.val):
                return False
            slow = slow.next
            cursor = cursor.next
        return True
'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:
Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''
