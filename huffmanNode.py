# this python file contains the node class for huffcompress

class HNode:
    # initialize node with symbol and frequency data
    # set left and right pointers to None
    def __init__(self, symbol, frequency):
        self.__symbol = symbol
        self.__frequency = frequency
        self.__left = None
        self.__right = None
        self.__parent = None

    # getters
    def getSymbol(self):
        return self.__symbol
    
    def getFrequency(self):
        return self.__frequency
    
    # setters
    def setSymbol(self, symbol):
        self.__symbol = symbol
    
    def setFrequency(self, frequency):
        self.__frequency = frequency

    def setLeft(self, left):
        self.__left = left

    def setRight(self, right):
        self.__right = right

    def setParent(self, parent):
        self.__parent = parent

    bool = isRoot = lambda self: self.__parent == None
    bool = isParent = lambda self: self.__left != None or self.__right != None
    bool = isLeaf = lambda self: self.__left == None and self.__right == None
