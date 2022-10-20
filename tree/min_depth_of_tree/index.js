/**
 * [Problem ref]{@link https://leetcode.com/problems/minimum-depth-of-binary-tree/}
 * @description Given a binary tree, find its minimum depth.
 * The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
 * Note: A leaf is a node with no children.
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
const minDepth = function (root) {
  if (!root) return 0;

  let min = Number.POSITIVE_INFINITY;

  function traverse(root, level) {
    if (!root) return;

    traverse(root.left, level + 1);

    if (!root.left && !root.right && level < min) {
      min = level
    }

    traverse(root.right, level + 1)
  }

  traverse(root, 1);

  return min;
};