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

        railtable[row][col] = "."
        col += 1
            
        if (down == True):
            row += 1
        else:
            row -= 1

    #run through matrix left right, top bottom and replace "-" placeholder with ciphertext
    index = 0
    for i in range(key):
        for j in range(len(message)):
            if railtable[i][j] == ".":
                # print(message[index])
                railtable[i][j] = message[index]
                index+=1
    # print(railtable)

    #read the zig/zag, similar to encode
    result = []
    down = False
    row, col = 0, 0
        
    for i in range(len(message)):
        
        if (row == 0): 
            down = True
        elif (row == key - 1):
            down = False

        result.append(railtable[row][col])
        col += 1
            
        if (down == True):
            row += 1
        else:
            row -= 1

    return("" . join(result))


if __name__ == "__main__":
    # print(decryptRailFence("cruyuyescrtifnbeis","3"))
    print("Your encrypted message was: " + sys.argv[1])
    print("The original message is: " + decryptRailFence(sys.argv[1], sys.argv[2]))

