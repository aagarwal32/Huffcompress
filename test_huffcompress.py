import unittest
from huffman_tree import HuffmanTree

class TestHuffCompress(unittest.TestCase):
    def test_decompress1(self):
        hc = HuffmanTree()
        INPUT_TEXT = "Hello World!"
        code, serial = hc.compress(INPUT_TEXT)
        DECOMPRESSED_TEXT = hc.decompress(code, serial)
        self.assertEqual(INPUT_TEXT, DECOMPRESSED_TEXT)
    
    def test_decompress2(self):
        hc = HuffmanTree()
        INPUT_TEXT = """In computer science and information theory, a Huffman code is a 
                        particular type of optimal prefix code that is commonly used for lossless data 
                        compression. The process of finding and/or using such a code proceeds by means 
                        of Huffman coding, an algorithm developed by David A. Huffman while he was a 
                        Sc.D. student at MIT, and published in the 1952 paper "A Method for the 
                        Construction of Minimum-Redundancy Codes". The output from Huffman's algorithm 
                        can be viewed as a variable-length code table for encoding a source symbol 
                        (such as a character in a file). The algorithm derives this table from the 
                        estimated probability or frequency of occurrence (weight) for each possible 
                        value of the source symbol. As in other entropy encoding methods, more common 
                        symbols are generally represented using fewer bits than less common symbols. 
                        Huffman's method can be efficiently implemented, finding a code in time linear 
                        to the number of input weights if these weights are sorted. However, although 
                        optimal among methods encoding symbols separately, Huffman coding is not always 
                        optimal among all compression methods."""
        code, serial = hc.compress(INPUT_TEXT)
        DECOMPRESSED_TEXT = hc.decompress(code, serial)
        self.assertEqual(INPUT_TEXT, DECOMPRESSED_TEXT)

    def test_decompress3(self):
        hc = HuffmanTree()
        INPUT_TEXT = """77772342342____LLLBBB_____&&&&2992//sl??!@#$%^&*()_+|}{":?><,./"""
        code, serial = hc.compress(INPUT_TEXT)
        DECOMPRESSED_TEXT = hc.decompress(code, serial)
        self.assertEqual(INPUT_TEXT, DECOMPRESSED_TEXT)

    def test_decompress4(self):
        hc = HuffmanTree()
        INPUT_TEXT = """LLLBBB"""
        code, serial = hc.compress(INPUT_TEXT)
        DECOMPRESSED_TEXT = hc.decompress(code, serial)
        self.assertEqual(INPUT_TEXT, DECOMPRESSED_TEXT)

    def test_compress_with_empty_input(self):
        hc = HuffmanTree()
        with self.assertRaises(ValueError):
            hc.compress("")

    def test_decompress_with_empty_input(self):
        hc = HuffmanTree()
        with self.assertRaises(ValueError):
            hc.decompress("", "")

    if __name__ == "__main__":
        unittest.main()