#-*- coding:utf-8
# 基本思想: bst的中序遍历代表了整个树，然后再从该有序列表中反推出来bst
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