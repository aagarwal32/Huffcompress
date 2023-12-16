import os
from huffman_tree import HuffmanTree
import numpy as np

# set marker value to separate different sections of compressed data
MARKER_VALUE = 255
MARKER_OCCURANCE = 100
MARKER_SEQUENCE = np.array([MARKER_VALUE]*MARKER_OCCURANCE, dtype=np.uint8)
# compressed file extension name
COMPRESSED_FILE_EXTENSION = ".huff"

class HuffFile:

    def __init__(self):
        pass

    # makes sure file is appropriate before compressing/decompressing
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


    def is_text_file(self, filename):
        """
        Checks if a file is a text file.

        Args:
            filename (str): The name of the file to check.

        Returns:
            bool: True if the file is a text file, False otherwise.
        """
        try:
            with open(filename, "r") as file:
                file.read(1024)
        except UnicodeDecodeError:
            return False
        return True
    

    def find_marker_sequence(self, data, marker_sequence):
        marker_length = len(marker_sequence)
        return [i for i in range(len(data) - marker_length + 1) 
            if np.array_equal(data[i:i+marker_length], marker_sequence)]


    # compresses file to contain binary code, serial code, and file length
    # needed for decompression

    # bit string is a string of 0s and 1s from compress function in 
    # huffman_tree.py

    # serial code is the instructions for recreating the huffman tree from 
    # compress function in huffman_tree.py

    # filename is the name of the file being compressed
    def compress_file(self, filename):
        
        # validate if file exists, is readable, and is not empty
        self._validate_file(filename)

        # validate if file is of the right type
        if not self.is_text_file(filename):
            raise ValueError("Error! File is not a plain text file.")
        
        # open file and read input data
        with open(filename, "r") as file:
            input_data = file.read()

        # obtain bit_string and serial_code from compress function
        ht = HuffmanTree()
        bit_string, serial_code = ht.compress(input_data)

        # convert bit string to NumPy array of integers
        code_bit_array = np.array(list(map(int, bit_string)))
        # pack binary data
        # takes bit array and packs each element into 8-bit chunks
        pack_code_data = np.packbits(code_bit_array)

        # get length of bit string and pack into 64-bit chunk
        bit_length = np.array([len(bit_string)], dtype=np.uint64)
        bit_len_bytes = np.frombuffer(bit_length.tobytes(), dtype=np.uint8)

        # converts each character in serial_code to binary. The binary string
        # is then converted to an array of bits which is then packed into
        # 8-bit chunks
        serial_data_bin = ''.join(format(ord(ch), '08b') for ch in serial_code)
        serial_data_bit_array = np.array(list(map(int, serial_data_bin)))
        pack_serial_data = np.packbits(serial_data_bit_array)

        # marker to separate different sections of compressed data
        # marker = np.array([MARKER_VALUE], dtype=np.uint8) # remove

        # concatenate bit length, serial code, and packed data
        # separated by markers
        compressed_data = np.concatenate([pack_code_data, MARKER_SEQUENCE, 
                                          bit_len_bytes, MARKER_SEQUENCE,
                                          pack_serial_data, MARKER_SEQUENCE])

        # write compressed data to a new file
        compressed_data.tofile(filename + COMPRESSED_FILE_EXTENSION)


    """
    This function decompresses a given file with COMPRESSED_FILE_EXTENSION

    Args: 
        filename (str): The name of the file to decompress

    Returns:
        str: The name of the decompressed file 
    """
    def decompress_file(self, filename):
        
        self._validate_file(filename)
        # confirm file is of correct extension
        original_filename, file_extension = os.path.splitext(filename)
        if file_extension != COMPRESSED_FILE_EXTENSION:
            raise ValueError("Error! File is not of type" + 
                             COMPRESSED_FILE_EXTENSION)
        
        # open file and read compressed data
        # read binary file
        read_data = np.fromfile(filename, dtype=np.uint8)

        # Finds elements that are equal to MARKER_VALUE
        # Args: array, value to compare to
        # Returns: array of indices where value is found
        marker_location = self.find_marker_sequence(read_data, MARKER_SEQUENCE)
        
        print("Marker locations:", marker_location) # remove

        # extract packed data, length data, and serial data
        packed_data = read_data[:marker_location[0]]
        length_data = read_data[marker_location[0] + 
                                MARKER_OCCURANCE:marker_location[1]]
        serial_data = read_data[marker_location[1] + 
                                MARKER_OCCURANCE:marker_location[2]]

        print("length data:", length_data)  # remove

        # unpack data (bit_string)
        unpacked_data = np.unpackbits(packed_data)
        # get length data of bit_string back from file
        original_length = np.frombuffer(length_data, dtype=np.uint64)[0]
        # revive bit_string of length original_length
        unpacked_data_str = ''.join(map(str, unpacked_data[:original_length]))

        # unpack data (serial_code)
        unpacked_serial_data = np.unpackbits(serial_data)
        # convert serial data back to string
        unpacked_serial_data_str = ''.join(map(str, unpacked_serial_data))
        # split serial data string into 8-bit chunks
        unpacked_serial_data_chunks = [unpacked_serial_data_str[i:i+8] for i in 
                                       range(0, len(unpacked_serial_data_str), 8)]

        # convert each 8-bit binary number back to serial code character
        # for each binary chunk, convert to integer, convert integer to char
        # revive serial_code string
        serial_data_str = ''.join(chr(int(chunk, 2)) for chunk in 
                                  unpacked_serial_data_chunks)
        
        # create instance of huffman tree to call decompression
        ht = HuffmanTree()
        print("unpacked data:", unpacked_data_str)
        print("serial data:", serial_data_str)
        decompressed_data = ht.decompress(unpacked_data_str, serial_data_str)
        # write to compressed file the decompressed string
        # decompress file
        with open(original_filename, 'w') as f:
            f.write(decompressed_data)


def main():
    hf = HuffFile()
    # hf.compress_file("test1.txt")
    hf.decompress_file("test1.txt.huff")

if __name__ == "__main__":
    main()
