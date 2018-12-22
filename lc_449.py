# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # using prior reversal
        import json
        ans = []
        def rev(ans, root):
            if not root:
                return
            ans.append(root.val)
            rev(ans, root.left)
            rev(ans, root.right)
        
        rev(ans, root)
        return json.dumps(ans)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        import json
        data = json.loads(data)
        return self.deser(data)
    
    def deser(self, data):    
        if not data:
            return None
        
        root = TreeNode(data[0])
        i = 1
        while i < len(data) and data[i] < data[0]:
            i += 1
        root.left = self.deser(data[1:i])
        root.right = self.deser(data[i:])
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))