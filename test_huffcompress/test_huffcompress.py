import sys
import os
import unittest
# insert your path to huffcompress here
sys.path.insert(0, os.path.abspath('/Users/arjuna/Documents/VScode/Projects/PythonAI/huffcompress'))
from compress_file import HuffFile

# compressed file extension name
COMPRESSED_FILE_EXTENSION = ".huff"

class TestHuffCompress(unittest.TestCase):

    # test if file contents before compression equal file contents after
    # compression and decompression. Small text file ~ 1KB
    def test_huffcompress_1(self, filename="test_small_file.txt"):
        hf = HuffFile()
        with open(filename, "r") as f:
            BEFORE = f.read()
        hf.compress_file(filename)
        hf.decompress_file(filename + COMPRESSED_FILE_EXTENSION)
        with open(filename, "r") as f:
            AFTER = f.read()

        self.assertEqual(BEFORE, AFTER)
    
    # test if file contents before compression equal file contents after
    # compression and decompression. Large text file ~ 11.1MB
    def test_huffcompress_2(self, filename="test_large_file.txt"):
        hf = HuffFile()
        with open(filename, "r") as f:
            BEFORE = f.read()
        hf.compress_file(filename)
        hf.decompress_file(filename + COMPRESSED_FILE_EXTENSION)
        with open(filename, "r") as f:
            AFTER = f.read()

        self.assertEqual(BEFORE, AFTER)

    # test if file contents before compression equal file contents after
    # compression and decompression. Large html file ~ 356KB
    def test_huffcompress_3(self, filename="test_large_html_file.html"):
        hf = HuffFile()
        with open(filename, "r") as f:
            BEFORE = f.read()
        hf.compress_file(filename)
        hf.decompress_file(filename + COMPRESSED_FILE_EXTENSION)
        with open(filename, "r") as f:
            AFTER = f.read()

        self.assertEqual(BEFORE, AFTER)

    # test error-handling if file has no contents ~ zero bytes
    def test_huffcompress_4(self, filename="test_zero_text_file.txt"):
        hf = HuffFile()
        with self.assertRaises(ValueError):
            hf.compress_file(filename) and hf.decompress_file(filename)

    # test error-handling if file is a pdf 
    # (not suitable for compression with this tool)
    def test_huffcompress_5(self, filename="test_incorrect_file_type_1.pdf"):
        hf = HuffFile()
        with self.assertRaises(ValueError):
            hf.compress_file(filename) and hf.decompress_file(filename)

    # test error-handling if file is an image 
    # (not suitable for compression with this tool)
    def test_huffcompress_6(self, filename="test_incorrect_file_type_2.jpg"):
        hf = HuffFile()
        with self.assertRaises(ValueError):
            hf.compress_file(filename) and hf.decompress_file(filename)

    # test error-handling if file is an excel file 
    # (not suitable for compression with this tool)
    def test_huffcompress_7(self, filename="test_incorrect_file_type_3.xls"):
        hf = HuffFile()
        with self.assertRaises(ValueError):
            hf.compress_file(filename) and hf.decompress_file(filename)

    # test error-handling if compress_file and decompress_file are given 
    # incorrect file types
    def test_huffcompress_8(self, filename="test_small_file.txt"):
        hf = HuffFile()
        with self.assertRaises(ValueError):
            hf.compress_file(filename+COMPRESSED_FILE_EXTENSION)
        with self.assertRaises(ValueError): 
            hf.decompress_file(filename)


if __name__ == "__main__":
    unittest.main()