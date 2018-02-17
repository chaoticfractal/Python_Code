"""
This is a simple Node class that is then implemented into both a single and 
double linked list 
"""

class ListNode:  
    def __init__(self, data):
        self.data = data
        #This stores data     
        self.next = None
        #This references the next item 
        self.previous = None
        #This referneces the previous item 
        return

    def has_value(self, value):
        #This method comapares the value with the node data 
        if self.data == value:
            return True
        else:
            return False

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return
    
    def add_list_item(self, item):
        #This adds an item at the end of the list 
        if not isinstance(item, ListNode):
            item = ListNode(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item    
        
        self.tail = item
        
        return
    
    def list_length(self):
        #This returns the number of list items
        count = 0
        current_node = self.head
        
        while current_node is not None:
            count = count + 1
            #Jump to next node 
            current_node = current_node.next    
        
        return count
    
    def output_list(self):
        #This outputs the list 
        current_node = self.head
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        
        return
    
    def unordered_search(self, value):
        #This searches the linked list for a node that has this value
        
        current_node = self.head
        node_id = 1
        #These define the current node and position 
        
        results = []
        #This is a list of the results 
        
        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
                
            current_node = current_node.next
            node_id = node_id + 1 
            #This part jumps to linked node from the results list
            
        return results
    
    def remove_list_item_by_id(self, item_id):
        #This removes the item using the item id 
        
        current_id = 1 
        current_node = self.head
        previous_node = None
        
        while current_node is not None:
            if current_id == item_id:
                #This is for when we are dealing with the fisrt node 
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    #This is the end of the search
                    return
            
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1 
            #This is for interating though the whole list 
            
        return
    
"""    
node1 = ListNode(15) 
node2 = ListNode(8.2)
item3 = "Berlin"
node4 = ListNode(15)

track = SingleLinkedList()
print("track length: %i" % track.list_length())

for current_item in [node1, node2, item3, node4]:
    track.add_list_item(current_item)
    print("track length: %i" % track.list_length())
    track.output_list()
"""

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 
        return 
    
    def list_length(self):
        #returns the length of the list 
        count = 0
        current_node = self.head
        
        while current_node is not None:
            count = count + 1 
            current_node = current_node.next
            
        return count
    
    def output_list(self):
        #This outputs the value of the node 
        current_node = self.head
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next 
            
        return 
    
    def unordered_search(self, value):
        #This searches the list for the node that has the value that is given
        current_node = self.head
        node_id = 1
        results = []
        
        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
                
            current_node = current_node.next
            node_id = node_id + 1
            #This jumps to the linked node 
            
        return results
    
    def add_list_item(self, item):
        #This adds an item at the end of the lsit 
        
        if isinstance(item, ListNode):
            if self.head is None:
                self.head = item
                item.previous is None 
                item.next = None
                self.tail = item 
            else: 
                self.tail.next = item 
                item.previous = self.tail
                self.tail = item 
                
            return
        
    def remove_list_item_by_id(self, item_id):
        #Removes the item with the item id 
        
        current_id = 1
        current_node = self.head
        
        while current_node is not None:
            previous_node = current_node.previous
            next_node = current_node.next
            
            if current_id == item_id:
                #This is if this is the first node
                if previous_node is not None:
                    previous_node.next = next_node 
                    if next_node is not None:
                        next_node.previous = previous_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.previous = None
                #Here we don't have to look any further
                
                return
            
            current_node = next_node
            current_id = current_id + 1 
            
        return
    
node1 = ListNode(15)  
node2 = ListNode(8.2)  
node3 = ListNode("Berlin")  
node4 = ListNode(15)

track = DoubleLinkedList()  
print("track length: %i" % track.list_length())

for current_node in [node1, node2, node3, node4]:  
    track.add_list_item(current_node)
    print("track length: %i" % track.list_length())
    track.output_list()

results = track.unordered_search(15)  
print(results)

track.remove_list_item_by_id(4)  
track.output_list()    
    
    
                        
                        
        
        
            


 
        
    
    
    




    