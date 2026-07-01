/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  let remainder = false;
  let v3 = l1.val + l2.val;
  if (v3 > 9) remainder = true;
  v3 %= 10;
  let finalNum = new ListNode(v3);
  l1 = l1.next;
  l2 = l2.next;

  let currentNode = finalNum;
  while (l1 || l2 || remainder) {
    let v1 = l1 ? l1.val : 0;
    let v2 = l2 ? l2.val : 0;
    let v3 = v1 + v2 + (remainder ? 1 : 0);
    remainder = false;

    if (v3 > 9) remainder = true;
    v3 %= 10;

    currentNode.next = new ListNode(v3);

    currentNode = currentNode.next;
    l1 ? (l1 = l1.next) : null;
    l2 ? (l2 = l2.next) : null;
  }
  return finalNum;
};
