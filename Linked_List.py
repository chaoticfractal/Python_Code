"""
This is a simple linked list that is based off code off an online resource that
I am using to further my understanding of OOP and Data Structures 
"""

class ListNode:  
    def __init__(self, data):
        self.data = data
        #This stores data     
        self.next = None
        #This references the next item 
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
            #Jump to linked node 
            current_node = current_node.next
            
        return count
    
node1 = ListNode(15) 
node2 = ListNode(8.2)
item3 = "Berlin"
node4 = ListNode(15)

track = SingleLinkedList()
print("track length: %i" % track.list_length())






 
        
    
    
    
    
    
    
    
    