# this python file initializes the huffman tree and other huffcompress functions
from huffmanNode import HNode
import heapq


class HuffmanTree:
    def __init__(self):
        self.__heap = []


    # creates nodes containing character and frequency data and pushes them into a priority queue
    def prioritizeNodes(self, inputStr):
        # dictionary to store frequency of each character
        freq = {}
        for char in inputStr:
            freq[char] = freq.get(char, 0) + 1

        # create nodes containing character and frequency data and push into priority queue
        for char, frequency in freq.items():
            heapq.heappush(self.__heap, HNode(char, frequency))


    # assigns binary '0' for left child and binary '1' for right child
    def getPrefixCodes(self, root, prefixCodes, code):
        if root.isLeaf():
            prefixCodes[root.getSymbol()] = code
            return

        self.getPrefixCodes(root.getLeft(), prefixCodes, code + "0")
        self.getPrefixCodes(root.getRight(), prefixCodes, code + "1")


    # compress creates binary tree and obtains compressed binary code from the input string
    def compress(self, inputStr):
        self.prioritizeNodes(inputStr)

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

        # get prefix codes for each character
        prefixCodes = {}
        self.getPrefixCodes(root, prefixCodes, "")

        # assign prefix code for each character in input string
        code_string = ""
        for char in inputStr:
            code_string += prefixCodes[char] 

        return code_string


    def serialize(self, root):
        pass


    def decompress(self, inputCode, serialCode):
        pass


def main():
    # temp input string
    input_str = "aaaabbbcc"
    huffcompress = HuffmanTree()
    print(huffcompress.compress(input_str))

if __name__ == "__main__":
    main()

