# Huffcompress

![huffcompress-logo-2](https://github.com/aagarwal32/Huffcompress/assets/152243328/ecdfbf05-b85a-4260-a27c-ced7cb2c9615)

## Description

<p>
  Huffcompress is a file compression and decompression tool that works on plain text (programming files, text files, etc.). It works based off the Huffman Coding algorithm that assigns smaller binary codes to characters that appear more often in a given string. Larger binary codes are assigned to characters that appear less often. This is all thanks to the functionality provided by binary trees and a min-heap based priority queue. The priority queue prioritizes characters with the lowest frequency which results in those characters at the bottom of the tree. During tree traversal, this creates larger binary prefix codes for the low frequency characters and smaller binary prefix codes for the high frequency characters. 
  
  As a result, this code provides the instructions to compress the string by up to ~50% or a 2:1 compression ratio! A serialized string that identifies the huffman tree in postorder notation is also generated for decompression. All data needed for decompression is packed into the compressed file itself as binary digits and unpacked back into a string during decompression.
</p>

<p>
  After a file is compressed, a ".huff" extension is added. Only files with ".huff" extension added during compression can be decompressed.
</p>

### GUI
<p align="center">
<img alt="huffcompress gui" src="https://github.com/aagarwal32/Huffcompress/assets/152243328/26cd28f5-1b37-42f4-9dcb-ca908b4f8da0">
</p>
<p>
  A simple, user-friendly GUI allows users to easily choose a file to compress/decompress. This tool is robust with comprehensive error-checking that displays error-message boxes for incompatible operating systems, file types, and more. 
</p>

<p>
  After successful compression, a message box displays the percent compressed as shown in the image below:
</p>

<p align="center">
  <img alt="huffcompress percent compressed gui" src="https://github.com/aagarwal32/Huffcompress/assets/152243328/4eca78f0-9d62-418e-ae01-09fde81d2f09">
</p>

## Installation (macOS and Windows)

1. Download the zipped file from the ```Releases``` section
2. Using the command line, navigate to the ```root directory``` of the program. For ex: cd path/to/huffcompress
3. To ensure you have the required 3rd-party libraries for this tool, run ```pip install -r requirements.txt```
4. Finally, run HuffcompressGUI.py script in the command line by typing ```python3 HuffcompressGUI.py```  

## Collaborators
<ul>
  <li>Arjun Agarwal (<a href="https://www.linkedin.com/in/agw02/">LinkedIn</a>)</li>
  <li>Harshavardan Yuvaraj (<a href="https://www.linkedin.com/in/harsha-yuvaraj/">LinkedIn</a>)</li>
</ul>

## First Release (In progress)
<ul>
  <li>File compression........ completed.</li>
  <li>File decompression........ completed.</li>
  <li>GUI that allows users to use this tool........ completed.</li>
</ul>
