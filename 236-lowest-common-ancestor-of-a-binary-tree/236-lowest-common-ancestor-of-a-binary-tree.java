/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    TreeNode result = null;
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        recurseTreeHelper(root, p, q);
        return result;
    }
    private boolean recurseTreeHelper(TreeNode currentNode, TreeNode p, TreeNode q) {
        if(currentNode == null)
            return false;
        int l = recurseTreeHelper(currentNode.left, p, q) ? 1 : 0;
        int r = recurseTreeHelper(currentNode.right, p, q) ? 1 : 0;
        int mid = currentNode == p || currentNode == q ? 1 : 0;
        int total = l + r + mid;
        if (total >= 2)
            result = currentNode;
        return total == 1 ? true : false; 
    }

}