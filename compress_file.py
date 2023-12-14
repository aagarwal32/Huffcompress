import os
from huffman_tree import HuffmanTree
import numpy as np

# set marker value to separate different sections of compressed data
MARKER_VALUE = 255
# compressed file extension name
COMPRESSED_FILE_EXTENSION = ".huff"

class HuffFile:

    def __init__(self):
        pass

    # make sure file is appropriate before compressing/decompressing
    def _validate_file(self, filename):
        # confirm filename is valid
        if not filename:
            raise ValueError("Error! File not declared properly.")
        # confirm file exists
        if not os.path.exists(filename):
            raise ValueError("Error! File does not exist.")
        # confirm file is readable
        if not os.access(filename, os.R_OK):
            raise ValueError("Error! File is not readable.")
        # confirm file is not empty
        if os.path.getsize(filename) == 0:
            raise ValueError("Error! File is empty.")


    # compresses file to contain binary code, serial code, and file length
    # needed for decompression

    # bit string is a string of 0s and 1s from compress function in 
    # huffman_tree.py

    # serial code is the instructions for recreating the huffman tree from 
    # compress function in huffman_tree.py

    # filename is the name of the file being compressed
    def compress_file(self, filename):
        
        self._validate_file(filename)
        
        # open file and read input data
        with open(filename, "r") as file:
            input_data = file.read()

        # obtain bit_string and serial_code from compress function
        ht = HuffmanTree()
        bit_string, serial_code = ht.compress(input_data)

        # convert bit string to NumPy array of integers
        bit_array = np.array(list(map(int, bit_string)))

        # pack binary data
        # takes bit array and packs each element into 8-bit chunks
        pack_data = np.packbits(bit_array)

        # get length of bit string and pack into 32-bit chunk
        bit_length = np.array([len(bit_string)], dtype=np.uint32)

        # convert serial code string to bytes using UTF-8 encoding
        serial_data = np.array(list(serial_code.encode("utf-8")))

        # marker to separate different sections of compressed data
        marker = np.array([MARKER_VALUE], dtype=np.uint8)

        # concatenate bit length, serial code, and packed data
        # separated by markers
        compressed_data = np.concatenate([pack_data, marker, 
                                          bit_length.tobytes(), marker,
                                          serial_data, marker])

        # write compressed data to file
        compressed_data.tofile(filename + COMPRESSED_FILE_EXTENSION)