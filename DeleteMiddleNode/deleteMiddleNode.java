/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteMiddle(ListNode head) {
        if (head.next == null)
            return null;
        ListNode fast = head;
        ListNode slow = head;
        ListNode behindSlow = head;
        boolean moveBehind = false;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (moveBehind) {
                behindSlow = behindSlow.next;
            }
            moveBehind = true;
        }
        behindSlow.next = slow.next;
        return head;
    }
}
