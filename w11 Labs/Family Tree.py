from cs110 import expect, summarize

class FamilyNode:
    def __init__(self, name):
        """
        Purpose: Initialize a FamilyNode with a name, partners, children, and parents.
        Example: node = FamilyNode("Family")
                 node.name     -> "Family"
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
        Example: tree = FamilyTree("Father")
                 tree.root.name -> "Father"
        """
        self.nodes = {}
        self.root = self.add_node(root_name)

    def add_node(self, name):
        """
        Purpose: Add a new node to the family tree.
        Example: tree = FamilyTree("Father")
                 tree.add_node("Me")
                 "A" in tree.nodes -> True
        """
        if name not in self.nodes:
            self.nodes[name] = FamilyNode(name)
        return self.nodes[name]

    def addParent(self, child_name, parent_name):
        """
        Purpose: Add a parent to a child node.
        Example: tree = FamilyTree("Father")
                 tree.addParent("Me", "Father") -> True
        """
        child   = self.add_node(child_name)
        parent  = self.add_node(parent_name)

        if len(child.parents) >= 2:
            return False  

        child.parents.add(parent)
        parent.children.add(child)
        return True
        
    def addChild(self, parent_name, child_name):
        """
        Purpose: Add a child to a parent node.
        Example: tree = FamilyTree("Father")
                 tree.addChild("Me", "Child") -> True
        """
        parent  = self.add_node(parent_name)
        child   = self.add_node(child_name)

        if len(child.parents) >= 2:
            return False  

        if parent not in child.parents:
            child.parents.add(parent)
        if child not in parent.children:
            parent.children.add(child)
        return True

    def addPartner(self, parent_name, partner_name):
        """
        Purpose: Add a partner to a parent node.
        Example: tree = FamilyTree("Father")
                 tree.addPartner("Father", "Mother")
        """
        parent  = self.add_node(parent_name)
        partner = self.add_node(partner_name)

        if partner not in parent.partners:
            parent.partners.add(partner)
        if parent not in partner.partners:
            partner.partners.add(parent)

    def addSibling(self, child_name, sibling_name):
        """
        Purpose: Add a sibling to a child node.
        Example: tree = FamilyTree("Father")
                 tree.addSibling("Me", "Sister")
        """
        child   = self.add_node(child_name)
        sibling = self.add_node(sibling_name)

        shared_parents = child.parents
        if len(shared_parents) == 0:
            return False

        for parent in shared_parents:
            parent.children.add(sibling)
            sibling.parents.add(parent)
        return True

    def display(self):
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

family_tree.addPartner("Great-Grandpa John", "Great-Grandma Mary")

family_tree.addChild("Great-Grandpa John", "Grandpa Mike")
family_tree.addChild("Great-Grandma Mary", "Grandpa Mike")
family_tree.addChild("Great-Grandpa John", "Grandma Emma")
family_tree.addChild("Great-Grandma Mary", "Grandma Emma")

family_tree.addPartner("Grandpa Mike", "Grandma Lucy")
family_tree.addPartner("Grandma Emma", "Grandpa Alex")

family_tree.addChild("Grandpa Mike", "Mother Kate")
family_tree.addChild("Grandma Lucy", "Mother Kate")
family_tree.addChild("Grandma Emma", "Father Leo")
family_tree.addChild("Grandpa Alex", "Father Leo")

family_tree.addChild("Grandpa Mike", "Mother Zoe")
family_tree.addChild("Grandma Lucy", "Mother Zoe")

family_tree.addPartner("Mother Kate", "Father Tom")
family_tree.addPartner("Father Leo", "Mother Lily")

family_tree.addChild("Mother Kate", "A")
family_tree.addChild("Father Tom", "A")
family_tree.addChild("Mother Kate", "B")
family_tree.addChild("Father Tom", "B")
family_tree.addChild("Father Leo", "C")
family_tree.addChild("Mother Lily", "C")

family_tree.addChild("Mother Zoe", "D")
family_tree.addChild("Mother Zoe", "E")
family_tree.addChild("Mother Zoe", "F")
family_tree.addChild("Mother Zoe", "G")
family_tree.addChild("Mother Zoe", "H")

family_tree.addSibling("A", "I")
family_tree.addPartner("B", "B-P")
family_tree.addPartner("C", "C-P")
print(family_tree.display())



#------------------------------------------------------------------------------------------------------------------------#
# Test FamilyNode creation                                                                                               #
#------------------------------------------------------------------------------------------------------------------------#
node = FamilyNode("Family")
expect(node.name, "Family")
expect(node.partners, set())
expect(node.children, set())
expect(node.parents,  set())

#------------------------------------------------------------------------------------------------------------------------#
# Test FamilyTree initialization                                                                                         #
#------------------------------------------------------------------------------------------------------------------------#
tree = FamilyTree("Father")
expect(tree.root.name, "Father")
expect("Father" in tree.nodes, True)  

#------------------------------------------------------------------------------------------------------------------------#
# Test add_node                                                                                                          #
#------------------------------------------------------------------------------------------------------------------------#
tree.add_node("Me")
expect("Me" in tree.nodes, True)
expect(tree.nodes["Me"].name, "Me")

#------------------------------------------------------------------------------------------------------------------------#
# Test addPartner                                                                                                        #
#------------------------------------------------------------------------------------------------------------------------#
expect(tree.addPartner("Father", "Mother"),   None)

#------------------------------------------------------------------------------------------------------------------------#
# Test addChild                                                                                                          #
#------------------------------------------------------------------------------------------------------------------------#
expect(tree.addChild("Me", "Child"),          True)

#------------------------------------------------------------------------------------------------------------------------#
# Test addParent                                                                                                         #
#------------------------------------------------------------------------------------------------------------------------#
expect(tree.addParent("Me", "Father"),        True)
expect(tree.addParent("Me", "Mother"),        True)
expect(tree.addParent("Me", "Other A"),       False)

#------------------------------------------------------------------------------------------------------------------------#
# Test addSibling                                                                                                        #
#------------------------------------------------------------------------------------------------------------------------#
expect(tree.addSibling("Me", "Sister"),       True)
expect(tree.addSibling("Other A", "Other B"), False)
print(tree.display())

#------------------------------------------------------------------------------------------------------------------------#
summarize()


