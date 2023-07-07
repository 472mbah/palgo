class tree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
    def add (self, value):
        
        if self.value == None:
            self.value = value
        elif value > self.value:
            if self.right == None:
                self.right = tree(value)
            else:
                self.right.add(value)
        else:
            if self.left == None:
                self.left = tree(value)
            else:
                self.left.add(value)

    def print (self):
        if self.left != None:
            self.left.print()
        
        print('Value', self.value)

        if self.right != None:
            self.right.print()

binary_tree = tree()
arr = [1, 13, 3, 15, 12, 6, -2, 8, 9, 10, 20, -100, 34, 10]
size = len(arr)
for k in range(size):
    binary_tree.add(arr[size - k - 1])
binary_tree.print()
'''
Returns:
Value -100
Value -2
Value 1
Value 3
Value 6
Value 8
Value 9
Value 10
Value 10
Value 12
Value 13
Value 15
Value 20
Value 34
'''