import hashlib
import datetime
import copy

class MinimalBlock():
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hashing()
        
    def coloured(self,r, g, b, text):
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

    def hashing(self):
        key = hashlib.sha256()
        key.update(str(self.index).encode('utf-8'))
        key.update(str(self.timestamp).encode('utf-8'))
        key.update(str(self.data).encode('utf-8'))
        key.update(str(self.previous_hash).encode('utf-8'))
        return key.hexdigest()
    
    def disp(self,r,g,b):
        print("Index :",self.coloured(r,g,b,self.index))
        print("Timestamp :",self.coloured(r,g,b,self.timestamp))
        print("Data :",self.coloured(r,g,b,self.data))
        print("Previous_hash :",self.coloured(r,g,b,self.previous_hash))
        print("Hash :",self.coloured(r,g,b,self.hash))
        print('\n')