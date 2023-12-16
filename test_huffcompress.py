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
        INPUT_TEXT = """The light blinded him. It was dark and he thought he was the only one in the area, but the light shining in his eyes proved him wrong. It came from about 100 feet away and was shining so directly into his eyes he couldn't make out anything about the person holding the light. There was only one thing to do in this situation. He reached into his pocket and pulled out a flashlight of his own that was much stronger than the one currently blinding him. He turned it on and pointed it into the stranger's eyes.
        What was beyond the bend in the stream was unknown. Both were curious, but only one was brave enough to want to explore. That was the problem. There was always one that let fear rule her life.
        The alarm went off at exactly 6:00 AM as it had every morning for the past five years. Barbara began her morning and was ready to eat breakfast by 7:00 AM. The day appeared to be as normal as any other, but that was about to change. In fact, it was going to change at exactly 7:23 AM.
        “Ingredients for life,” said the backside of the truck. They mean food, but really food is only 1 ingredient of life. Life has so many more ingredients such as pain, happiness, laughter, joy, tears, and smiles. Life also has hard work, easy play, sleepless nights, and sunbathing by the ocean. Love, hatred, envy, self-assurance, and fear could be just down aisle 3 ready to be bought when needed. How I wish I could pull ingredients like these off shelves in a store.
        It's an unfortunate reality that we don't teach people how to make money (beyond getting a 9 to 5 job) as part of our education system. The truth is there are a lot of different, legitimate ways to make money. That doesn't mean they are easy and that you won't have to work hard to succeed, but it does mean that if you're willing to open your mind a bit you don't have to be stuck in an office from 9 to 5 for the next fifty years o your life.
        It was going to rain. The weather forecast didn't say that, but the steel plate in his hip did. He had learned over the years to trust his hip over the weatherman. It was going to rain, so he better get outside and prepare.
        Sitting in the sun, away from everyone who had done him harm in the past, he quietly listened to those who roamed by. He felt at peace in the moment, hoping it would last, but knowing the reprieve would soon come to an end. He closed his eyes, the sun beating down on face and he smiled. He smiled for the first time in as long as he could remember.
        The answer was within her reach. It was hidden in a box and now that box sat directly in front of her. She'd spent years searching for it and could hardly believe she'd finally managed to find it. She turned the key to unlock the box and then gently lifted the top. She held her breath in anticipation of finally knowing the answer she had spent so much of her time in search of. As the lid came off she could see that the box was empty.
        There were a variety of ways to win the game. James had played it long enough to know most of them and he could see what his opponent was trying to do. There was a simple counterattack that James could use and the game should be his. He began deploying it with the confidence of a veteran player who had been in this situation a thousand times in the past. So, it was with great surprise when his opponent used a move he had never before seen or anticipated to easily defeat him in the game."""
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