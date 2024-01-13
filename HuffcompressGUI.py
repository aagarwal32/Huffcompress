"""
Huffcompress GUI Interface 

Welcome to Huffcompress, a file compression and decompression tool 
designed with a graphical user interface (GUI) using Tkinter. 
Huffcompress employs the Huffman algorithm to achieve efficient 
and lossless compression of text files, providing a 2:1 compression ratio.


Running the GUI

Before launching the GUI, ensure Python 3 is installed on your system. 
To run HuffcompressGUI.py, please follow these steps:

  1. Navigate to the directory where the Huffman program files are located using the command line: cd path/to/huffman/program

                                                      (or)
                                                      
     Add the Huffman program directory to the system's PATH variable for more convenient access.

  2. Then, execute the following command: python HuffcompressGUI.py
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import ImageTk, Image
from os import stat, path
from compress_file import HuffFile, CompressionError, COMPRESSED_FILE_EXTENSION

# background color - hex format
bgColor = "#e4e8f0"

# Create the main window
mainWin = tk.Tk()
mainWin.title("HuffCompress - Lossless Compression Tool")
mainWin.geometry("400x200")  # Set the size of the window
mainWin.iconbitmap('./assets/logo.ico') # Set the icon logo of HuffCompress
mainWin.configure(bg=bgColor)  # Set the background color to a shade of royal blue
mainWin.resizable(False, False)  # Lock the window size

# Loading our logo and placing it in the main window
logo = ImageTk.PhotoImage(Image.open('./assets/logo.png').resize((120,90)))
logoContainer = tk.Label(image=logo)
logoContainer.configure(bg=bgColor, height="60")  # Set the background color to a shade of royal blue
logoContainer.pack(side="top", anchor="nw") # Position the logo top-left side of the main window

# Styles for buttons
style1 = ttk.Style() # For compress button
style2 = ttk.Style() # For decompress button
style1.configure('W.TButton', font=('Helvetica', 16, 'bold italic'), foreground='#5dbea3')
style2.configure('C.TButton', font=('Helvetica', 16, 'bold italic'), foreground='#4681f4')

# Listener for compress button
def compressFile():
    # Open a file dailog for the user to select the file to be compressed
    target_file =  filedialog.askopenfilename(title="Choose a file to compress")
     
    # Displays an error message and exits function when the user does not choose a file to compress
    if(target_file == ''):
       messagebox.showerror("Error", "No file chosen!")
       return

    # Size of the file before compression (in bytes)
    original_size = stat(target_file)

    # Compress the file
    hf = HuffFile()
    try:
      new_path = hf.compress_file(target_file)
    except CompressionError as e: 
       messagebox.showerror("Error", str(e))
       return
    

    # Size of the file after compression (in bytes)
    compressed_size = stat(new_path + "/" + path.basename(target_file) + COMPRESSED_FILE_EXTENSION)

    # Display a compression successful message
    messagebox.showinfo('Compression Successful!', f"File size reduced by {round(((original_size.st_size-compressed_size.st_size))/original_size.st_size*100)}%")
    

# Listener for decompress button
def decompressFile():
    # Open a file dailog for the user to select the file to be decompressed
    target_file =  filedialog.askopenfilename(title="Choose a file to decompress", filetypes=((".huff","*.huff"),))

    # Displays an error message and exits function when the user does not choose a file to compress
    if(target_file == ''):
       messagebox.showerror("Error", "No file chosen!")
       return

    # Decompress the file
    hf = HuffFile()
    try:
      hf.decompress_file(target_file)
    except Exception as e: 
      messagebox.showerror('Error', "An error occurred during decompression: " + e)
      return

    # Display a decompression successful message
    messagebox.showinfo('Decompression Successful!', f"Your file has been decompressed!")


# Create the buttons for compression & decompression
compressBtn = ttk.Button(mainWin, text="Compress a File", width=20, style='W.TButton', command=compressFile)
compressBtn.pack(padx=(100,0), pady=(10,0))
decompressBtn = ttk.Button(mainWin, text="Decompress a File", width=20, style='C.TButton', command=decompressFile)
decompressBtn.pack(padx=(100,0), pady=(10,0))


# Run the Tkinter event loop
mainWin.mainloop()
