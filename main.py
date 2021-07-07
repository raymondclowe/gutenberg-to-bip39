
#!/usr/bin/env python3
"""
This is a really bad way to create a Bitcoin bip39 seed phrase

You specify a gutenberg text, either by ID or by title, with an optional
starting point and this code will create a bip39 seed phrase with a valid 
checksum.  Using this to open a wallet will create a wallet that you can
always get back to simply by remembering what book you started with, but
so can anybody else.

Optionally you can enter your own text, such as the opening page of Harry
Potter, and it will create a seed using only those words that are accepted
in the word list. 

Once again this is a terrible idea but it does mean you can get to a wallet
in the future simply by knowing the name of the book and without writing 
down or memorizing the seed phrase.
"""

__author__ = "Raymond Lowe"
__version__ = "0.1.0"
__license__ = "none"

import argparse
import requests
import os

keyword_list_url = "https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt"
gutenberg_url = "https://www.gutenberg.org/files/~n/~n-0.txt"

def main(args):
    """ Main entry point of the app """

    keyword_list = requests.request("GET", keyword_list_url).text.split('\n')
    g_id = str(args['gutenberg'])
    if g_id == 0:
        if (not os.path.exists(args['file'])) or (os.path.getsize(args['file']) == 0):
            raise Exception
        else:
            # read the text file
            
    else:
        # read text from url, clip off gutenberg intro boiler plate

    # break text into words
    # for each word see if it is in the wordlist
    # keep going until got enough words
    # output all the words, highlighting the ones from the wordlist,
    # calculate the checksum and output that too, highlighted
    


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Optional argument flag which defaults to False
    parser.add_argument("-g", "--gutenberg", action="store",
                        default=0, help="Gutenberg project ID")
    parser.add_argument("-f", "--file", action="store",
                        default="file.txt", help="filename for source text")

    args = parser.parse_args()
    main(args)