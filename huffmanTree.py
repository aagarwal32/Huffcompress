# this python file initializes the huffman tree and other huffcompress functions
from huffmanNode import HNode
import heapq

class HuffmanTree:
    # this function creates nodes containing character and frequency data and pushes them into a priority queue
    def prioritizeNodes(self, inputStr):
        # dictionary to store frequency of each character
        freq = {}
        for char in inputStr:
            freq[char] = freq.get(char, 0) + 1

        # create nodes containing character and frequency data and push into priority queue
        for char, frequency in freq.items():
            heapq.heappush(self.__heap, HNode(char, frequency))

    # compress creates binary tree and obtains compressed binary code from the input string
    def compress(self, inputStr):
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


    def serialize(self, root):
        pass

    def decompress(self, inputCode, serialCode):
        pass
