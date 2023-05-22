def encryptRailTableFence(message, key):

    railtable = [['\n' for i in range(len(message))]
                for j in range(key)]
     
    down = False
    row, col = 0, 0
     
    for i in range(len(message)):
        
        if (row == 0): 
			down = True
		elif (row == key - 1):
			down = False

        railtable[row][col] = message[i]
        col += 1
         
        if (down == True):
			row += 1
		else:
			row -= 1

    result = []
    for i in range(key):
        for j in range(len(message)):
            if railtable[i][j] != '\n':
                result.append(railtable[i][j])
    return("" . join(result))

if __name__ == "__main__":
    print(encryptRailFence("attack at once", 2))
    print(encryptRailFence("defend the east wall", 3))