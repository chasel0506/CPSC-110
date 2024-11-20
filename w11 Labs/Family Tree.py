class FamilyNode:
    def __init__(self, name):
        """
        Purpose: Initialize a FamilyNode with a name, partners, children, and parents.
        Example:
                 node = FamilyNode("John")
                 node.name     -> "John"
                 node.partners -> set()
                 node.children -> set()
                 node.parents  -> set()
        """
        self.name = name
        self.partners = set()
        self.children = set()
        self.parents = set()

class FamilyTree:
    def __init__(self, root_name):
        """
        Purpose: Initialize the FamilyTree with a root node.
        Example: tree = FamilyTree("Root Person")
                 tree.root.name -> "Root Person"
        """
        self.nodes = {}
        self.root = self.add_node(root_name)

    def add_node(self, name):
        """
        Purpose: Add a new node to the family tree.
        Example: tree = FamilyTree("Root Person")
                 tree.add_node("Child 1")
                 "Child 1" in tree.nodes -> True
        """
        if name not in self.nodes:
            self.nodes[name] = FamilyNode(name)
        return self.nodes[name]

    def add_parent(self, child_name, parent_name):
        """
        Purpose: Add a parent to a child node.
        Example: tree = FamilyTree("Root Person")
                 tree.add_parent("Child 1", "Parent A")
                 "Parent A" in tree.nodes["Child 1"].parents -> True
        """
        child = self.add_node(child_name)
        parent = self.add_node(parent_name)

        if len(child.parents) >= 2:
            raise ValueError("A child cannot have more than two parents.")

        child.parents.add(parent)
        parent.children.add(child)

    def add_child(self, parent_name, child_name):
        """
        Purpose: Add a child to a parent node.
        Example: tree = FamilyTree("Root Person")
                 tree.add_child("Root Person", "Child 1")
                 "Child 1" in tree.nodes["Root Person"].children -> True
        """
        parent = self.add_node(parent_name)
        child = self.add_node(child_name)

        if len(child.parents) >= 2:
            raise ValueError("A child cannot have more than two parents.")

        child.parents.add(parent)
        parent.children.add(child)

    def add_partner(self, parent_name, partner_name):
        """
        Purpose: Add a partner to a parent node.
        Example: tree = FamilyTree("Root Person")
                 tree.add_partner("Root Person", "Spouse A")
                 "Spouse A" in tree.nodes["Root Person"].partners -> True
        """
        parent = self.add_node(parent_name)
        partner = self.add_node(partner_name)

        parent.partners.add(partner)
        partner.partners.add(parent)

    def add_sibling(self, child_name, sibling_name):
        """
        Purpose: Add a sibling to a child node.
        Example: tree = FamilyTree("Root Person")
                 tree.add_sibling("Child 1", "Sibling 1")
                 "Sibling 1" in tree.nodes["Root Person"].children -> True
        """
        child = self.add_node(child_name)
        sibling = self.add_node(sibling_name)

        shared_parents = child.parents
        if len(shared_parents) == 0:
            raise ValueError("Cannot add a sibling to a node with no parents.")

        for parent in shared_parents:
            parent.children.add(sibling)
            sibling.parents.add(parent)

    def display_tree(self, node=None, level=0):
        """
        Purpose: Display the family tree starting from the given node.
        Example: tree = FamilyTree("Root Person")
                 tree.add_child("Root Person", "Child 1")
                 tree.display_tree()
            Output: Root Person
                    Child 1
        """
        if node is None:
            node = self.root

        indent = "  " * level
        print(f"{indent}{node.name}")

        # Display partners
        if node.partners:
            print(f"{indent}  Partners:")
            for partner in node.partners:
                print(f"{indent}    - {partner.name}")

        # Display children
        if node.children:
            print(f"{indent}  Children:")
            for child in node.children:
                self.display_tree(child, level + 1)

        # Display parents (optional)
        if level == 0 and node.parents:  # Only show parents for root for context
            print(f"{indent}  Parents:")
            for parent in node.parents:
                print(f"{indent}    - {parent.name}")
            
family_tree = FamilyTree("Great Grandparent 1")

# Generation 1 (Depth 1)
family_tree.add_partner("Great Grandparent 1", "Great Grandparent 2")

# Generation 2 (Depth 2)
family_tree.add_child("Great Grandparent 1", "Grandparent 1")
family_tree.add_child("Great Grandparent 2", "Grandparent 1")
family_tree.add_child("Great Grandparent 1", "Grandparent 2")
family_tree.add_child("Great Grandparent 2", "Grandparent 2")

# Generation 3 (Depth 3)
family_tree.add_partner("Grandparent 1", "Grandparent 1 Partner")
family_tree.add_partner("Grandparent 2", "Grandparent 2 Partner")

family_tree.add_child("Grandparent 1", "Parent 1")
family_tree.add_child("Grandparent 1 Partner", "Parent 1")
family_tree.add_child("Grandparent 2", "Parent 2")
family_tree.add_child("Grandparent 2 Partner", "Parent 2")

family_tree.add_child("Grandparent 1", "Parent 3")
family_tree.add_child("Grandparent 1 Partner", "Parent 3")

# Generation 4 (Depth 4)
family_tree.add_partner("Parent 1", "Parent 1 Partner")
family_tree.add_partner("Parent 2", "Parent 2 Partner")

family_tree.add_child("Parent 1", "Child 1")
family_tree.add_child("Parent 1 Partner", "Child 1")
family_tree.add_child("Parent 1", "Child 2")
family_tree.add_child("Parent 1 Partner", "Child 2")
family_tree.add_child("Parent 2", "Child 3")
family_tree.add_child("Parent 2 Partner", "Child 3")

family_tree.add_child("Parent 3", "Child 4")
family_tree.add_child("Parent 3", "Child 5")

# Adding siblings, partners, and expanding width
family_tree.add_sibling("Child 1", "Child 6")
family_tree.add_partner("Child 2", "Child 2 Partner")
family_tree.add_child("Child 2", "Grandchild 1")
family_tree.add_child("Child 2 Partner", "Grandchild 1")

family_tree.add_partner("Child 3", "Child 3 Partner")
family_tree.add_child("Child 3", "Grandchild 2")
family_tree.add_child("Child 3 Partner", "Grandchild 2")

family_tree.add_child("Child 6", "Grandchild 3")

# Display the entire family tree
family_tree.display_tree()