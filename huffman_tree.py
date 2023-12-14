# this python file initializes the huffman tree and other huffcompress functions
from huffman_node import HNode
import heapq


class HuffmanTree:
    def __init__(self):
        self.__heap = []


    # creates nodes containing character and frequency data and pushes them
    # into a priority queue
    def prioritize_nodes(self, input_string):
        # dictionary to store frequency of each character
        freq = {}
        for char in input_string:
            freq[char] = freq.get(char, 0) + 1

        # create nodes containing character and frequency data and push into
        # priority queue
        for char, frequency in freq.items():
            heapq.heappush(self.__heap, HNode(char, frequency))


    # assigns binary '0' for left child and binary '1' for right child
    def get_prefix_codes(self, root, prefix_codes, code):
        if root.isLeaf():
            prefix_codes[root.getSymbol()] = code
            return

        self.get_prefix_codes(root.getLeft(), prefix_codes, code + "0")
        self.get_prefix_codes(root.getRight(), prefix_codes, code + "1")


    # compress creates binary tree and obtains compressed binary code from
    # the input string
    def compress(self, input_string):
        if not input_string:
            raise ValueError("Error! File is empty.")
        self.prioritize_nodes(input_string)

        # pop two nodes from priority queue, create parent node, and push
        # parent node into priority queue
        while len(self.__heap) > 1:
            min_1 = heapq.heappop(self.__heap)
            min_2 = heapq.heappop(self.__heap)

            parent = HNode(None, min_1.getFrequency() + min_2.getFrequency())
            parent.setLeft(min_1)
            parent.setRight(min_2)

            heapq.heappush(self.__heap, parent)

        # last node in priority queue is the root node
        root = heapq.heappop(self.__heap)
        root.setParent(None)

        serial_code = self.serialize(root)

        # get prefix codes for each character
        prefix_codes = {}
        self.get_prefix_codes(root, prefix_codes, "")

        # assign prefix code for each character in input string
        code_string = ""
        for char in input_string:
            code_string += prefix_codes[char]

        return code_string, serial_code 


    def serialize(self, root):
        stack1 = []
        stack2 = []
        
        # pop nodes from first stack until empty
        stack1.append(root)
        while len(stack1) > 0:
            node = stack1.pop()
            stack2.append(node)

            # explore sub trees of each node and add to stack 1
            if node.getLeft() != None:
                stack1.append(node.getLeft())
            if node.getRight() != None:
                stack1.append(node.getRight())
        
        # create serial code by examining nodes in stack 2
        serial = ""
        while len(stack2) > 0:
            top = stack2.pop()
            if top.isLeaf():
                serial += "L" + top.getSymbol()
            if top.isParent():
                serial += "B"

        return serial


    def decompress(self, input_code, serial_code):
        if not input_code or not serial_code:
            raise ValueError("Error! File is empty.")

        stack = []
        root_node = None

        # use serial code to reconstruct huffman tree
        i = 0
        while i < len(serial_code):
            # if branch (B), pop two nodes from stack and create parent node
            if serial_code[i] == "B":
                right_child = stack.pop()
                left_child = stack.pop()

                parent = HNode(None, None)
                parent.setLeft(left_child)
                parent.setRight(right_child)

                stack.append(parent)
            # if leaf (L), create leaf node and push into stack
            elif serial_code[i] == "L":
                i += 1
                symbol = serial_code[i]
                leaf = HNode(symbol, None)
                stack.append(leaf)
            i += 1
        
        # last node in stack is the root node
        if len(stack) > 0:
            root_node = stack.pop()

        # decompress input code using huffman tree
        decompressed = ""
        current = root_node

        # perform left traversal if bit is 0, right traversal if bit is 1
        for bit in input_code:
            if bit == "0":
                current = current.getLeft()
            else:
                current = current.getRight()

            # if current node is leaf, add character to decompressed string
            if current.isLeaf():
                decompressed += current.getSymbol()
                # reset current node to root node for next traversal
                current = root_node
        
        return decompressed
