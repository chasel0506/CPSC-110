class FamilyNode:
    def __init__(self, name):
        """
        Initialize a FamilyNode with a name, partners, children, and parents.
        :param name: str
        """
        self.name = name
        self.partners = set()
        self.children = set()
        self.parents = set()

class FamilyTree:
    def __init__(self, root_name):
        """
        Initialize the FamilyTree with a root node.
        :param root_name: str
        """
        self.nodes = {}
        self.root = self.add_node(root_name)

    def add_node(self, name):
        """
        Add a new node to the family tree.
        :param name: str
        :return: FamilyNode
        """
        if name not in self.nodes:
            self.nodes[name] = FamilyNode(name)
        return self.nodes[name]

    def add_parent(self, child_name, parent_name):
        """
        Add a parent to a child node.
        :param child_name: str
        :param parent_name: str
        :return: None
        """
        # HtDF step 1: Signature, purpose, examples written above
        # HtDF step 2: Header
        # HtDF step 3: Stub (Implemented directly)
        child = self.add_node(child_name)
        parent = self.add_node(parent_name)

        # HtDF step 4: Template
        if len(child.parents) >= 2:
            raise ValueError("A child cannot have more than two parents.")

        child.parents.add(parent)
        parent.children.add(child)

    def add_child(self, parent_name, child_name):
        """
        Add a child to a parent node.
        :param parent_name: str
        :param child_name: str
        :return: None
        """
        parent = self.add_node(parent_name)
        child = self.add_node(child_name)

        if len(child.parents) >= 2:
            raise ValueError("A child cannot have more than two parents.")

        child.parents.add(parent)
        parent.children.add(child)

    def add_partner(self, parent_name, partner_name):
        """
        Add a partner to a parent node.
        :param parent_name: str
        :param partner_name: str
        :return: None
        """
        parent = self.add_node(parent_name)
        partner = self.add_node(partner_name)

        parent.partners.add(partner)
        partner.partners.add(parent)

    def add_sibling(self, child_name, sibling_name):
        """
        Add a sibling to a child node.
        :param child_name: str
        :param sibling_name: str
        :return: None
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
        Display the family tree starting from the given node.
        :param node: FamilyNode
        :param level: int
        :return: None
        """
        if node is None:
            node = self.root

        print("  " * level + node.name)
        for partner in node.partners:
            print("  " * (level + 1) + f"(Partner: {partner.name})")

        for child in node.children:
            self.display_tree(child, level + 1)

# Example usage to create a non-trivial family tree
family_tree = FamilyTree("Root Person")

# Adding family members
family_tree.add_partner("Root Person", "Spouse A")
family_tree.add_child("Root Person", "Child 1")
family_tree.add_child("Spouse A", "Child 1")

family_tree.add_child("Root Person", "Child 2")
family_tree.add_child("Spouse A", "Child 2")

family_tree.add_partner("Child 1", "Partner B")
family_tree.add_child("Child 1", "Grandchild 1")
family_tree.add_child("Partner B", "Grandchild 1")

family_tree.add_child("Child 1", "Grandchild 2")
family_tree.add_child("Partner B", "Grandchild 2")

family_tree.add_sibling("Child 1", "Sibling 1")

family_tree.display_tree()
