class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class TreeManager:
    def __init__(self):
        self.root = None
    
    def count_nodes(self, node):
        if not node:
            return 0
        count = 1
        for child in node.children:
            count += self.count_nodes(child)
        return count
    
    def get_height(self, node):
        if not node:
            return 0
        if len(node.children) == 0:
            return 1
        max_height = 0
        for child in node.children:
            max_height = max(max_height, self.get_height(child))
        return max_height + 1
    
    def count_leaves(self, node):
        if not node:
            return 0
        if len(node.children) == 0:
            return 1
        leaf_count = 0
        for child in node.children:
            leaf_count += self.count_leaves(child)
        return leaf_count
    
    def find_node(self, node, value):
        if not node or not value:
            return None
        if node.value == value:
            return node
        for child in node.children:
            found = self.find_node(child, value)
            if found:
                return found
        return None
    
    def add_node(self, new_node_name, parent_name=None):
        if not new_node_name.strip():
            return "❌ Node name cannot be empty"
        
        new_node_name = new_node_name.strip()
        parent_name = parent_name.strip() if parent_name else None
        
        # Check if node already exists
        if self.root and self.find_node(self.root, new_node_name):
            return f"❌ Node '{new_node_name}' already exists"
        
        if not self.root:
            if parent_name:
                return "❌ Cannot set parent for root node"
            self.root = TreeNode(new_node_name)
            return f"✅ Root node '{new_node_name}' created"
        else:
            if not parent_name:
                return "❌ Parent node required (root already exists)"
            parent = self.find_node(self.root, parent_name)
            if not parent:
                return f"❌ Parent '{parent_name}' not found"
            parent.children.append(TreeNode(new_node_name))
            return f"✅ Node '{new_node_name}' added to '{parent_name}'"
    
    def delete_helper(self, node, target):
        if not node:
            return False
        for i in range(len(node.children)):
            if node.children[i].value == target:
                node.children.pop(i)
                return True
            else:
                found = self.delete_helper(node.children[i], target)
                if found:
                    return True
        return False
    
    def delete_node(self, target):
        if not target.strip():
            return "❌ Please enter node name to delete"
        
        target = target.strip()
        
        if not self.root:
            return "❌ Tree is empty"
        
        if self.root.value == target:
            self.root = None
            return f"🗑️ Root node '{target}' and entire tree deleted"
        else:
            deleted = self.delete_helper(self.root, target)
            if deleted:
                return f"🗑️ Node '{target}' and its subtree deleted"
            else:
                return f"❌ Node '{target}' not found"
    
    def clear_tree(self):
        if not self.root:
            return "❌ Tree is already empty"
        
        confirm = input("Are you sure you want to clear the entire tree? (y/n): ")
        if confirm.lower() != 'y':
            return "❌ Operation cancelled"
        
        self.root = None
        return "🔄 Tree cleared successfully"
    
    def display_stats(self):
        total_nodes = self.count_nodes(self.root)
        height = self.get_height(self.root)
        leaf_count = self.count_leaves(self.root)
        
        print(f"\n📊 Tree Statistics:")
        print(f"Total Nodes: {total_nodes}")
        print(f"Tree Height: {height}")
        print(f"Leaf Count: {leaf_count}")
    
    def display_tree(self, node=None, level=0, prefix=""):
        if node is None:
            node = self.root
        
        if not node:
            print("🌳 Tree is empty")
            return
        
        if level == 0:
            print("🌳 Tree Structure:")
        
        print(f"{prefix}├── {node.value}")
        
        for i, child in enumerate(node.children):
            is_last = (i == len(node.children) - 1)
            new_prefix = prefix + ("    " if is_last else "│   ")
            child_prefix = prefix + ("└── " if is_last else "├── ")
            print(f"{child_prefix}{child.value}")
            
            if child.children:
                for j, grandchild in enumerate(child.children):
                    is_last_grandchild = (j == len(child.children) - 1)
                    grandchild_prefix = new_prefix + ("└── " if is_last_grandchild else "├── ")
                    self._display_subtree(grandchild, new_prefix, grandchild_prefix)
    
    def _display_subtree(self, node, base_prefix, node_prefix):
        print(f"{node_prefix}{node.value}")
        for i, child in enumerate(node.children):
            is_last = (i == len(node.children) - 1)
            child_prefix = base_prefix + ("└── " if is_last else "├── ")
            new_base = base_prefix + ("    " if is_last else "│   ")
            self._display_subtree(child, new_base, child_prefix)

def main():
    tree = TreeManager()
    
    print("🌳 Tree Manager Console")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Add node")
        print("2. Delete node") 
        print("3. Display tree")
        print("4. Show statistics")
        print("5. Clear tree")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            node_name = input("Enter node name: ")
            parent_name = input("Enter parent name (leave empty for root): ")
            if not parent_name:
                parent_name = None
            result = tree.add_node(node_name, parent_name)
            print(result)
            
        elif choice == '2':
            node_name = input("Enter node name to delete: ")
            result = tree.delete_node(node_name)
            print(result)
            
        elif choice == '3':
            tree.display_tree()
            
        elif choice == '4':
            tree.display_stats()
            
        elif choice == '5':
            result = tree.clear_tree()
            print(result)
            
        elif choice == '6':
            print("👋 Goodbye!")
            break
            
        else:
            print("❌ Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()