import string
import random

N = 7

                             
def captha() :
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
    return res
    
