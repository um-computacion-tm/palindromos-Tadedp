def isPalindromeRecursive(word):
    finalIndex = len(word) - 1
    word = word.lower()
    if finalIndex <= 0:
        return True
    
    elif finalIndex == 1 and word[0] == word[1]:
        return True
    
    elif word[0] != word[finalIndex]:
        return False
    
    return isPalindromeRecursive(word[1 : finalIndex])

if __name__ == '__main__':
    pass