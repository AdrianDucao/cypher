#!/usr/bin/env python3
import string

class cypher:
    def __init__(self, shift, msg):
        self.shift = shift
        self.msg = msg

    def scramble(self):
        letters = list(string.ascii_lowercase)
        
        for i in range(self.shift):
            #to be continued...

if __name__ == '__main__':
    
    shift = input('Enter Shift:')
    msg = input('Enter message:')
    
    send = cypher(shift, msg)
    
    if shift != '' and msg != '':
        send.scramble()
