# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cursor = head
        prev = None

        while(cursor is not None):
            temp = cursor.next
            cursor.next = prev
            prev = cursor
            cursor = temp
        return prev

'''
Reversing a linked list 
'''
