class Slivik:

    def __init__(self):

        self.size = 0
        self.capacity = 1
        self.first_element = None
        self.last_element = None

    class Node:

        def __init__(self, value):

            self.value = value
            self.next = None

    def append (self, value):

        new_mode = self.Node(value)

        if self.first_element is None:
            self.first_element = new_node        
            self.first_element = new_node

        else: 
            self.last_element.next = new_node  
            self.last_element = new_node 

        self.size += 1

        def __str__(self):

            element = []
            current = self.first_element
            
            while current:
                element.append(current.value)
                current = current.next
            return "[" +','.join(str(e) for e in element) + "]"    

marray = Slivik()
#print(marray)
marray.append('хелоу ворлд')
print(marray)