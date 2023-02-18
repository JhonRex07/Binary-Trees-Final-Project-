# PROJECT ON DATA STRUCTURES AND ALGORITHMS
# Programmed by JHON REX B. JUSAYAN

from tkinter import *

main_window = Tk()
main_window.title("Python Binary Tree")
main_window.geometry("400x275")

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def Node(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.Node(data)
            else:
                self.left = BinaryTreeNode(data)
        else:
            if self.right:
                self.right.Node(data)
            else:
                self.right = BinaryTreeNode(data)
    
    def minimum(self):
        if self.left is None:
            return self.data
        return self.left.minimum()
    
    def maximum(self):
        if self.right is None:
            return self.data
        return self.right.maximum()
    
    def in_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def pre_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

def build_tree(elements):
    root = BinaryTreeNode(elements[0])
    
    for i in range(1, len(elements)):
        root.Node(elements[i])

    return root

def number():
    numbers = entry1.get().split()
    label2.configure(text="NUMBERS: " + str(numbers))
    
    numbers_tree = build_tree(numbers)
    label3.configure(text="MINIMUM: " + numbers_tree.minimum())

    numbers_tree = build_tree(numbers)
    label4.configure(text="MAXIMUM: " + numbers_tree.maximum())

    numbers_tree = build_tree(numbers)
    label5.configure(text="IN-ORDER TRAVERSAL: " + str(numbers_tree.in_order_traversal()))

    numbers_tree = build_tree(numbers)
    label6.configure(text="PRE-ORDER TRAVERSAL: " + str(numbers_tree.pre_order_traversal()))

    numbers_tree = build_tree(numbers)
    label7.configure(text="POST-ORDER TRAVERSAL: " + str(numbers_tree.post_order_traversal()))
    
if __name__ == '__main__':
    label1 = Label(main_window, text="ENTER NUMBERS:", font=('Bold', 12))
    label1.place(height=100, width=415)

    entry1 = Entry(main_window, font=('Bold', 12))
    entry1.place(height=35, width=300, x=50)

    result_button1 = Button(main_window, text="SHOW RESULTS", command=number)
    result_button1.place(height=25, width=225, x=80, y=70)

    label2 = Label(main_window, text="NUMBERS: ")
    label2.place(height=30, x=35, y=100)

    label3 = Label(main_window, text="MINIMUM: ")
    label3.place(height=25,  x=35, y=130)

    label4 = Label(main_window, text="MAXIMUM: ")
    label4.place(height=25, x=200, y=130)

    label5 = Label(main_window, text="IN-ORDER TRAVERSE: ")
    label5.place(height=30, x=35, y=160)

    label6 = Label(main_window, text="PRE-ORDER TRAVERSE: ")
    label6.place(height=30, x=35, y=190)

    label7 = Label(main_window, text="POST-ORDER TRAVERSE: ")
    label7.place(height=30, x=35, y=220)

mainloop()