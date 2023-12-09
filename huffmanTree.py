# this python file initializes the huffman tree and other huffcompress functions
from huffmanNode import HuffmanNode

class HuffmanTree:
    # create huffman node with specified symbol and frequency
    def createHuffmanNode(self, symbol, frequency):
        return HuffmanNode(symbol, frequency)
    
    def compress(self, inputStr):
        pass

    def serialize(self, root):
        pass

    def decompress(self, inputCode, serialCode):
        pass
