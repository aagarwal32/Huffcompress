# this python file contains the node class for huffcompress
import heapq

class HuffmanNode:
    # initialize node with data symbol, frequency, and left and right NULL pointers
    def __init__(self, symbol, frequency):
        self.__symbol = symbol
        self.__frequency = frequency
        self.__left = None
        self.__right = None