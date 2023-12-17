# this python file initializes the huffman tree and other huffcompress functions
from huffman_node import HNode
import heapq


class HuffmanTree:
    """
    This class provides methods for prioritizing nodes based on the frequency
    of each character, building the Huffman tree, assigning prefix codes to 
    each character, serializing, and deserializing the Huffman tree.
    """

    def __init__(self):
        self.__heap = []


    def prioritize_nodes(self, input_string):
        """
        Creates nodes containing character and frequency data and 
        pushes them into a priority queue.

        Args:
            input_string (str): The string to be compressed.

        Returns:
            None
        """

        # dictionary to store frequency of each character
        freq = {}
        for char in input_string:
            freq[char] = freq.get(char, 0) + 1

        # create nodes containing character and frequency data and push into
        # priority queue
        for char, frequency in freq.items():
            heapq.heappush(self.__heap, HNode(char, frequency))


    def get_prefix_codes(self, root, prefix_codes, code):
        """
        This function traverses the Huffman tree and assigns a prefix code to 
        each character -- determined by the path from the root to the leaf 
        node representing the character (with '0' for left and '1' for right).

        Args:
            root (HNode): The root node of the Huffman tree.
            prefix_codes (dict): A dictionary to store the prefix codes for
            each character.
            code (str): The current prefix code

        Returns:
            None
        """

        if root.isLeaf():
            prefix_codes[root.getSymbol()] = code
            return

        self.get_prefix_codes(root.getLeft(), prefix_codes, code + "0")
        self.get_prefix_codes(root.getRight(), prefix_codes, code + "1")


    def compress(self, input_string):
        """
        This function compresses the input string by building the Huffman tree
        to obtain the code_string (concatenation of prefix codes) and the 
        serial code.

        Args:
            input_string (str): The string to be compressed.

        Raises:
            ValueError: If the input string is empty.

        Returns:
            code_string (str): input_string but with respective prefix codes
            serial_code (str): instructions to rebuild huffman tree
        """

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
        """
        This function uses two stacks to perform a post-order traversal of the 
        Huffman tree. The serialized string can be used to reconstruct the tree
        for decompression.

        Args:
            root (HNode): The root node of the Huffman tree.

        Returns:
            serial (str): The serialized Huffman tree.
        """

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
        """
        This function reconstructs the Huffman tree from the serialized code. 
        Then, it traverses the Huffman tree according to the input code to 
        decompress it back into the original string.

        Args:
            input_code (str): The compressed binary code.
            serial_code (str): The serialized Huffman tree.

        Raises:
            ValueError: If the input code or serialized code is empty.

        Returns:
            decompressed (str): The decompressed, original input string.
        """
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
