# this python file initializes the huffman tree and other huffcompress functions
from huffmanNode import HNode
import heapq


class HuffmanTree:
    def __init__(self):
        self.__heap = []


    # creates nodes containing character and frequency data and pushes them into a priority queue
    def prioritize_nodes(self, inputStr):
        # dictionary to store frequency of each character
        freq = {}
        for char in inputStr:
            freq[char] = freq.get(char, 0) + 1

        # create nodes containing character and frequency data and push into priority queue
        for char, frequency in freq.items():
            heapq.heappush(self.__heap, HNode(char, frequency))


    # assigns binary '0' for left child and binary '1' for right child
    def getprefixcodes(self, root, prefixcodes, code):
        if root.isLeaf():
            prefixcodes[root.getSymbol()] = code
            return

        self.getprefixcodes(root.getLeft(), prefixcodes, code + "0")
        self.getprefixcodes(root.getRight(), prefixcodes, code + "1")


    # compress creates binary tree and obtains compressed binary code from the input string
    def compress(self, inputStr):
        self.prioritize_nodes(inputStr)

        # pop two nodes from priority queue, create parent node, and push parent node into priority queue
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
        prefixcodes = {}
        self.getprefixcodes(root, prefixcodes, "")

        # assign prefix code for each character in input string
        code_string = ""
        for char in inputStr:
            code_string += prefixcodes[char]

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
        
        serial = ""
        while len(stack2) > 0:
            top = stack2.pop()
            if top.isLeaf():
                serial += "L" + top.getSymbol()
            if top.isParent():
                serial += "B"

        return serial


    def decompress(self, inputCode, serialCode):
        pass


def main():
    # temp input string
    input_str = "aaaabbbcc"
    huffcompress = HuffmanTree()
    print(huffcompress.compress(input_str))

if __name__ == "__main__":
    main()

