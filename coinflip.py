import random


def main():
    coinflip = random.randint(0,1)
    
    if coinflip == 0:
        result = 'heads'
    else:
        result = 'tails'
        
    return result