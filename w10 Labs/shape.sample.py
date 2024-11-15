import time
import random
from cs110 import expect, summarize

class Shape:
    def __init__(self, position):
        self.position = position
        
    def __lt__(self, other):
        return self.position < other.position

    def __le__(self, other):
        return self.position <= other.position

    def __eq__(self, other):
        return self.position == other.position

    def __ne__(self, other):
        return self.position != other.position

    def __gt__(self, other):
        return self.position > other.position

    def __ge__(self, other):
        return self.position >= other.position
    
    def __repr__(self):
        return str(self.position) 

def selection_sort(shapes):
    n = len(shapes)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if shapes[j] < shapes[min_index]:
                min_index = j
        shapes[i], shapes[min_index] = shapes[min_index], shapes[i]
        
        '''
        if i % 1000 == 0:  
            progress = (i / (n - 1)) * 100
            print(f"Work Progress       : {progress:.0f}%")
        '''
        
    return shapes


def generate_shapes_list(size):
    return [Shape(random.randint(0, 10000)) for _ in range(size)]


sizes = [100, 1000, 10000, 100000]
for size in sizes:
    shapes = generate_shapes_list(size)

    # Timing Selection Sort
    start_time = time.time()                       # Record the start time for Selection Sort
    sorted_shapes = selection_sort(shapes.copy())  # Use a copy to keep the original unsorted list
    selection_time = time.time() - start_time      # Calculate the time taken by Selection Sort

    # Timing Bilte-in
    start_time = time.time()                       # Record the start time for Python's built-in sort
    sorted(shapes)  
    builtin_time = time.time() - start_time        # Calculate the time taken by the built-in sort

    print(f"List Size           : {size}")
    print(f"Selection Sort Time : {selection_time:.10f} seconds")
    print(f"built-in Time       : {builtin_time:.10f} seconds")
    print(f"Sorted List         : {sorted_shapes}\n")
    


#------------------------------------------------------------------------------------------------------------------------#
# Test Shape comparisons                                                                                                 #
#------------------------------------------------------------------------------------------------------------------------#

shape1 = Shape(5)
shape2 = Shape(10)
expect(shape1 <  shape2, True)
expect(shape1 >  shape2, False)
expect(shape1 == shape2, False)
expect(shape1 <= shape2, True)
expect(shape1 >= shape2, False)


#------------------------------------------------------------------------------------------------------------------------#
# Test selection_sort with sorted and unsorted lists                                                                     #
#------------------------------------------------------------------------------------------------------------------------#

shapes_sorted   = [Shape(1), Shape(2), Shape(3), Shape(4), Shape(5)]
shapes_unsorted = [Shape(5), Shape(3), Shape(1), Shape(4), Shape(2)]

expect(selection_sort(shapes_sorted.copy()),    shapes_sorted)   
expect(selection_sort(shapes_unsorted.copy()),  shapes_sorted) 


#------------------------------------------------------------------------------------------------------------------------#
# Test selection_sort with duplicates                                                                                    #
#------------------------------------------------------------------------------------------------------------------------#

shapes_with_duplicates       = [Shape(5), Shape(3), Shape(1), Shape(4), Shape(3)]
expected_sorted_duplicates   = [Shape(1), Shape(3), Shape(3), Shape(4), Shape(5)]
expect(selection_sort(shapes_with_duplicates.copy()), expected_sorted_duplicates)


#------------------------------------------------------------------------------------------------------------------------#
summarize()
