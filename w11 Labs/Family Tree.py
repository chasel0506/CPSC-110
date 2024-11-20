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
        self.name     = name
        self.partners = set()
        self.children = set()
        self.parents  = set()

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

    def addParent(self, child_name, parent_name):
        """
        Purpose: Add a parent to a child node.
        Example: tree = FamilyTree("Root Person")
                 tree.addParent("Child 1", "Parent A")
                 "Parent A" in tree.nodes["Child 1"].parents -> True
        """
        child   = self.add_node(child_name)
        parent  = self.add_node(parent_name)

        if len(child.parents) >= 2:
            raise ValueError("A child cannot have more than two parents.")

        child.parents.add(parent)
        parent.children.add(child)

    def addChild(self, parent_name, child_name):
        """
        Purpose: Add a child to a parent node.
        Example: tree = FamilyTree("Root Person")
                 tree.addChild("Root Person", "Child 1")
                 "Child 1" in tree.nodes["Root Person"].children -> True
        """
        parent  = self.add_node(parent_name)
        child   = self.add_node(child_name)

        if len(child.parents) >= 2:
            raise ValueError("A child cannot have more than two parents.")

        child.parents.add(parent)
        parent.children.add(child)

    def addPartner(self, parent_name, partner_name):
        """
        Purpose: Add a partner to a parent node.
        Example: tree = FamilyTree("Root Person")
                 tree.addPartner("Root Person", "Spouse A")
                 "Spouse A" in tree.nodes["Root Person"].partners -> True
        """
        parent  = self.add_node(parent_name)
        partner = self.add_node(partner_name)

        parent.partners.add(partner)
        partner.partners.add(parent)

    def addSibling(self, child_name, sibling_name):
        """
        Purpose: Add a sibling to a child node.
        Example: tree = FamilyTree("Root Person")
                 tree.addSibling("Child 1", "Sibling 1")
                 "Sibling 1" in tree.nodes["Root Person"].children -> True
        """
        child   = self.add_node(child_name)
        sibling = self.add_node(sibling_name)

        shared_parents = child.parents
        if len(shared_parents) == 0:
            raise ValueError("Cannot add a sibling to a node with no parents.")

        for parent in shared_parents:
            parent.children.add(sibling)
            sibling.parents.add(parent)

    def display_tree_graphviz(self):
        lines = ["graph TD;"]
        
        added_edges = set()
        
        for node in self.nodes.values():
            node_label = node.name.replace(" ", "")
            lines.append(f"    {node_label}[{node.name}];")
            
            for partner in node.partners:
                partner_label = partner.name.replace(" ", "")
                edge = tuple(sorted([node_label, partner_label]))
                if edge not in added_edges:
                    lines.append(f"    {node_label} === {partner_label};")
                    added_edges.add(edge)
                
            for child in node.children:
                child_label = child.name.replace(" ", "")
                lines.append(f"    {node_label} --> {child_label};")
        
        return "\n".join(lines)

# Build the family tree as before
family_tree = FamilyTree("Great-Grandpa John")

# Generation 1 (Depth 1)
family_tree.addPartner("Great-Grandpa John", "Great-Grandma Mary")

# Generation 2 (Depth 2)
family_tree.addChild("Great-Grandpa John", "Grandpa Mike")
family_tree.addChild("Great-Grandma Mary", "Grandpa Mike")
family_tree.addChild("Great-Grandpa John", "Grandma Emma")
family_tree.addChild("Great-Grandma Mary", "Grandma Emma")

# Generation 3 (Depth 3)
family_tree.addPartner("Grandpa Mike", "Grandma Lucy")
family_tree.addPartner("Grandma Emma", "Grandpa Alex")

family_tree.addChild("Grandpa Mike", "Mother Kate")
family_tree.addChild("Grandma Lucy", "Mother Kate")
family_tree.addChild("Grandma Emma", "Father Leo")
family_tree.addChild("Grandpa Alex", "Father Leo")

family_tree.addChild("Grandpa Mike", "Mother Zoe")
family_tree.addChild("Grandma Lucy", "Mother Zoe")

# Generation 4 (Depth 4)
family_tree.addPartner("Mother Kate", "Father Tom")
family_tree.addPartner("Father Leo", "Mother Lily")

family_tree.addChild("Mother Kate", "Child 1")
family_tree.addChild("Father Tom", "Child 1")
family_tree.addChild("Mother Kate", "Child 2")
family_tree.addChild("Father Tom", "Child 2")
family_tree.addChild("Father Leo", "Child 3")
family_tree.addChild("Mother Lily", "Child 3")

family_tree.addChild("Mother Zoe", "Child 4")
family_tree.addChild("Mother Zoe", "Child 5")

# Adding siblings, partners, and expanding width
family_tree.addSibling("Child 1", "Child 6")
family_tree.addPartner("Child 2", "Child 2 Partner")
family_tree.addPartner("Child 3", "Child 3 Partner")

# Display the family tree in Graphviz format
print(family_tree.display_tree_graphviz())
