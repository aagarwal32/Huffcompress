# this python file contains the node class for huffcompress
import heapq

class HuffmanNode:
    def __init__(self, symbol, frequency):
        self.__symbol = symbol
        self.__frequency = frequency
        self.__left = None
        self.__right = None

class HuffmanTree:
    def createHuffmanNode(self, symbol, frequency):
        return HuffmanNode(symbol, frequency)

