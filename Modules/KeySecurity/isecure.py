encdict = {'a': 'Z', 'b': 'a', 'c': 'b', 'd': 'c', 'e': 'd', 'f': 'e', 'g': 'f', 'h': 'g', 'i': 'h', 'j': 'i', 'k': 'j', 'l': 'k', 'm': 'l', 'n': 'm', 'o': 'n', 'p': 'o', 'q': 'p', 'r': 'q', 's': 'r', 't': 's', 'u': 't', 'v': 'u', 'w': 'v', 'x': 'w', 'y': 'x', 'z': 'y', '@': 'z', '£': '@', '$': '£', '%': '$', '^': '%', '&': '^', '*': '&', '(': '*', ')': '(', '<': ')', '>': 
               '<', '.': '>', ',': '.', '/': ',', '1': '/', '2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', '8': '7', '9': '8', '0': '9', '_': '0', '+': '_', '-': '+', '`': '-', '¬': '`', '|': '¬', '=': '|', ' ': '=', '!': ' ', 'A': '!', 'B': 'A', 'C': 'B', 'D': 'C', 'E': 'D', 'F': 'E', 'G': 'F', 'H': 'G', 'I': 'H', 'J': 'I', 'K': 'J', 'L': 'K', 'M': 'L', 'N': 'M', 'O': 'N', 'P': 'O', 'Q': 'P', 'R': 'Q', 'S': 'R', 'T': 'S', 'U': 'T', 'V': 'U', 'W': 'V', 'X': 'W', 'Y': 'X', 'Z': 'Y'}    
def machineencrypt(key):

   
   newkey = ""
   for i in key :
       for a in encdict.keys() :
           if i == a :
               newkey = newkey+encdict[a]
   return newkey

def machinedecrypt(key):
    oldkey = ""
    for i in key :
       for a,b in encdict.items() :
           if i == b :
               oldkey = oldkey+a

    return oldkey