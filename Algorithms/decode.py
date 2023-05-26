import sys

def decryptRailFence(message, key):
    #recreate table using 2D array
    key = int(key)
    railtable = [['\n' for i in range(len(message))]
                for j in range(key)]

    down = False
    row, col = 0, 0
        
    for i in range(len(message)):
        
        if (row == 0): 
            down = True
        elif (row == key - 1):
            down = False

        railtable[row][col] = "-"
        col += 1
            
        if (down == True):
            row += 1
        else:
            row -= 1

    #run through matrix left right, top bottom and replace "-" placeholder with ciphertext

    #read the zig/zag similar to encode


if __name__ == "__main__":

