import random
def jumbled(n):
    jumble1=list(n)
    random.shuffle(jumble1)
    return ''.join(jumble1)
    
print(jumbled("dineshkumar"))