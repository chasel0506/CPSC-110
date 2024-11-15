import math
from dataclasses import dataclass
from typing import Any, List
from functools import reduce
from cs110 import expect, summarize

@dataclass
class Shape:
    id            : str
    lat           : float 
    lon           : float  
    sequence      : int
    dist_traveled : float = 0
    next          : "Shape" = None 

    def dist(self, other: 'Shape') -> float:
        """Calculate distance between this shape and another shape."""
        dlat = self.lat - other.lat
        dlon = self.lon - other.lon
        return math.sqrt(dlat ** 2 + dlon ** 2)

@dataclass
class Node:
    data: Shape
    next: 'Node' = None

@dataclass
class LinkedList:
    head: Node = None

    def add(self, shape: Shape):
        """Add a shape to the end of the linked list."""
        new_node = Node(data=shape)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def calculate_distance(self) -> float:
        """Calculate the total distance of the shapes in the linked list."""
        total_distance = 0.0
        current = self.head
        while current and current.next:
            total_distance += current.data.dist(current.next.data)
            current = current.next
        return total_distance
    
def parse_row_to_shape(row: str) -> Shape:
    """
    Convert a comma-separated string row into a Shape instance.
    Example: parse_row_to_shape("292022,49.257645,-123.17228,1,0") -> Shape(id="292022", lat=49.257645, lon=-123.17228, sequence=1, dist_traveled=0)
    """
    columns       = row.strip().split(',')
    id            = columns[0]
    lat           = float(columns[1])
    lon           = float(columns[2])
    sequence      = int(columns[3])
    dist_traveled = float(columns[4])

    return Shape(
        id=id,
        lat=lat,
        lon=lon,
        sequence=sequence,
        dist_traveled=dist_traveled,
        next=None
    )

def parse_shapes(file_path: str) -> List[LinkedList]:
    shape_linked_lists = {}

    with open(file_path, 'r') as file:
        for line in file.readlines()[1:]: 
            shape = parse_row_to_shape(line)
            if shape.id not in shape_linked_lists:
                shape_linked_lists[shape.id] = LinkedList()
            shape_linked_lists[shape.id].add(shape)

    return list(shape_linked_lists.values())


def longest(linked_lists: List[LinkedList]) -> float:
    """
    Purpose: Calculate the longest route distance from a list of shape linked lists.
    Example: longest([LinkedList1, LinkedList2]) -> 25.0
    """
    distances = list(map(lambda linked_list: linked_list.calculate_distance(), linked_lists))
    return max(distances)

def shortest(linked_lists: List[LinkedList]) -> float:
    """
    Purpose: Calculate the shortest route distance from a list of shape linked lists.    
    Example: shortest([LinkedList1, LinkedList2]) -> 22.0
    """
    distances = list(map(lambda linked_list: linked_list.calculate_distance(), linked_lists))
    return min(distances)

def average(linked_lists: List[LinkedList]) -> float:
    """
    Purpose: Calculate the average route length from a list of shape linked lists.
    Example: average([LinkedList1, LinkedList2]) -> 23.5
    """
    distances = list(map(lambda linked_list: linked_list.calculate_distance(), linked_lists))
    return reduce(lambda a, b: a + b, distances, 0) / len(distances) if distances else 0

if __name__ == "__main__":
    shape_linked_lists = parse_shapes("shapes.txt")
    print(f"There are {len(shape_linked_lists)} shape linked lists.")
    print(f"Longest route        : {longest(shape_linked_lists)}")
    print(f"Shortest route       : {shortest(shape_linked_lists)}")
    print(f"Average route length : {average(shape_linked_lists)}")

#------------------------------------------------------------------------------#
# Test Setup
#------------------------------------------------------------------------------#

# Example shapes to test
shape_1 = Shape(id="1", lat=0.0, lon=0.0, sequence=1, dist_traveled=0)
shape_2 = Shape(id="1", lat=3.0, lon=4.0, sequence=2, dist_traveled=1)
shape_3 = Shape(id="1", lat=11.0, lon=19.0, sequence=3, dist_traveled=2)
shape_4 = Shape(id="2", lat=5.0, lon=12.0, sequence=1, dist_traveled=0)
shape_5 = Shape(id="2", lat=12.0, lon=36.0, sequence=2, dist_traveled=3)

# LinkedLists for testing
linked_list_1 = LinkedList(head=None)
linked_list_1.add(shape_1)
linked_list_1.add(shape_2)
linked_list_1.add(shape_3)

linked_list_2 = LinkedList(head=None)
linked_list_2.add(shape_4)
linked_list_2.add(shape_5)

#------------------------------------------------------------------------------#
# Test LinkedList.calculate_distance
#------------------------------------------------------------------------------#
expect(linked_list_1.calculate_distance(), 22.0)  # (0,0)(3,4) + (3,4)(11,19) -> 5 + 17
expect(linked_list_2.calculate_distance(), 25.0)  # (5,12)(12,36) -> 25

#------------------------------------------------------------------------------#
# Test longest
#------------------------------------------------------------------------------#
expect(longest([linked_list_1, linked_list_2]), 25.0)  

#------------------------------------------------------------------------------#
# Test shortest
#------------------------------------------------------------------------------#
expect(shortest([linked_list_1, linked_list_2]), 22.0)  

#------------------------------------------------------------------------------#
# Test average
#------------------------------------------------------------------------------#
expect(average([linked_list_1, linked_list_2]), 23.5)

summarize()
