'''
MERGE TWO SORTED LISTS 


You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

 Example 1: 
 Input: list1 = [1,2,4], list2 = [1,3,4]
 Output: [1,1,2,3,4,4]

 Example 2: 
 Input: list1 = [], list2 = []
 Output: []
 Example 3:

 Input: list1 = [], list2 = [0]
 Output: [0]
  

  Constraints: 
  The number of nodes in both lists is in the range [0, 50].
  -100 <= Node.val <= 100
  Both list1 and list2 are sorted in non-decreasing order.


'''

'''
    1) make new head, and runner
    2)while not null if l1.val < l2.val -> runner.next = l1; else -> runner.next = l2
    3) increment l1 and l2 and runner
    4) if either list has values after loop ends, set next to rest of that list


'''



head = run = ListNode()
while list1 and list2: #'while not null'
    if list1.val < list2.val:
        run = list1
        list1 = list1.next
    else:
        run = list2
        list2 = list2.next
    
    run = run.next

if list1:
    run.next = list1
else:
    run.next = list2
return head.next









