# Huffcompress

![huffcompress-logo](https://github.com/aagarwal32/Huffcompress/assets/152243328/4f7e0296-5e59-4f5c-8cb9-6f40884572d6)

## Description

<p>
  Huffcompress is a file compression and decompression tool that works only on plain text (programming files, text files, etc.). It works based off the Huffman Coding algorithm that assigns smaller binary codes to characters that appear more often in a given string. Larger binary codes are assigned to characters that appear less often. This is all thanks to the functionality provided by binary trees and a min-heap based priority queue. The priority queue prioritizes characters with the lowest frequency which results in those characters at the bottom of the tree. During tree traversal, this creates larger binary prefix codes for the low frequency characters and smaller binary prefix codes for the high frequency characters. 
  
  As a result, this code provides the instructions to compress the string by ~50% or a 2:1 compression ratio! A serialized string that identifies the huffman tree in postorder notation is also generated for decompression. All data needed for decompression is packed into the compressed file itself as binary digits and unpacked back into a string during decompression.
</p>

<p>
  After a file is compressed, a ".huff" extension is added. Only files with ".huff" extension added during compression can be decompressed.
</p>

## Collaborators
<ul>
  <li>Arjun Agarwal (<a href="https://www.linkedin.com/in/agw02/">LinkedIn</a>)</li>
  <li>Harshavardan Yuvaraj (<a href="https://www.linkedin.com/in/harsha-yuvaraj/">LinkedIn</a>)</li>
</ul>

## First Release (In progress)
<ul>
  <li>File compression........ completed.</li>
  <li>File decompression........ completed.</li>
  <li>GUI that allows users to use this tool....... in-progress.</li>
</ul>
